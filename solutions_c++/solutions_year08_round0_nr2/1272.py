#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
using namespace std;

typedef struct __TIME_TABLE__{
	int begin;
	int end;
	char NAME;
}t_Table;

bool cmp(const t_Table t1, const t_Table t2){
	return t1.begin < t2.begin;
}

void main()
{
	int t_case,
		T_CASE=1;
	
	int i,j;
	int NA,NB;
	int TR;
	int HH,MM, _begin, _end;
	vector<t_Table> table;


	scanf("%d", &t_case);
	for(i=0; i < t_case; ++i){		
		
		scanf("%d", &TR);		
		scanf("%d %d", &NA, &NB);

		t_Table row;
		for(j=0; j < NA; ++j){
			scanf("%2d:%2d ", &HH,&MM);
			_begin = HH*60+MM;
			scanf("%2d:%2d", &HH,&MM);
			_end = HH*60+MM;
			row.begin = _begin;
			row.end = _end;
			row.NAME = 'A';
			table.push_back(row);
		}

		for(j=0; j < NB; ++j){
			scanf("%2d:%2d ", &HH,&MM);
			_begin = HH*60+MM;
			scanf("%2d:%2d", &HH,&MM);
			_end = HH*60+MM;
			
			row.begin = _begin;
			row.end = _end;
			row.NAME = 'B';
			table.push_back(row);
		}
		
		sort(table.begin(), table.end(), cmp);

		deque<pair<int,char> > QA;
		deque<pair<int,char> > QB;
		int table_size = NA+NB;
		for(j=0; j < table_size; ++j){
			if( table[j].NAME == 'A' ){
				if( !QA.empty() && QA.front().first+TR <= table[j].begin ){
					--NA;
					QB.push_back(make_pair(table[j].end, QA.front().second));
					QA.pop_front();
				}else 
					QB.push_back(make_pair(table[j].end, 'A' ));
			}else if( table[j].NAME == 'B' ){
				if( !QB.empty() && QB.front().first+TR <= table[j].begin ){
					--NB;
					QA.push_back(make_pair(table[j].end, QB.front().second));
					QB.pop_front();
				}else
					QA.push_back(make_pair(table[j].end, 'B'));
			}
			sort(QA.begin(), QA.end());
			sort(QB.begin(), QB.end());
		}
		printf("Case #%d: %d %d\n", T_CASE++, NA, NB);
		table.clear();
		
	}


}