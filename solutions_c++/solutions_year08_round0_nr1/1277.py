#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

void main()
{
	int t_case=0;
	int T_CASE=1;
	int S, Q;
	vector<string> se;
	vector<bool> se_valid;
	vector<string> query;

	int i,j,k;
	int cost;

	string str;
	char buffer[256];
	
	scanf("%d\n",&t_case);
	for(i=0; i < t_case; ++i){		
		scanf("%d\n", &S);

		for(j=0; j < S; ++j){		
			fgets(buffer, 256, stdin);
			buffer[ (int)strlen(buffer)-1 ] = 0;
			str = buffer;
			se.push_back(str);
			se_valid.push_back(true);
		}
		
		scanf("%d\n", &Q);
		for(j=0; j < Q; ++j){
			fgets(buffer, 256, stdin);
			buffer[ (int)strlen(buffer)-1 ] = 0;
			str = buffer;
			query.push_back(str);
		}
		if( Q == 0 ) printf("Case #%d: 0\n", T_CASE++);
		else{
			int current_invalid=0, ret;
			cost = 0;
			j=0;
			do{
				for(k=0; k < S; ++k){
					if( se_valid[ k ] && query[j] != se[k] )
						++current_invalid;
					else{
						if( query[j] == se[k] ) ret = k;
						se_valid[ k ] = false;
					}
				}
				if( current_invalid == 0 ){
					++cost;
					for(k=0; k < S; ++k) se_valid[k] = true;
					se_valid[k] = false;
				}else
					++j;

				current_invalid=0;				
			}while(j < Q);	

			printf("Case #%d: %d\n", T_CASE++, cost);
		}

		se.clear();
		se_valid.clear();
		query.clear();
	}


}