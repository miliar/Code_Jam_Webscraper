#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<string>
#include<utility>
#include<map>
#include<vector>
using namespace std;

int TC, na, nb, n, i, j, k;
char sa[105][3], sb[105][2], s[105];
char change[30][30];
bool check[30][30], del[30][30];
int exist[30];
string ss;

int main(void){
	scanf("%d", &TC);
	for (int t = 1; t <= TC; t++){
		memset(check, 0, sizeof(check));
		memset(del, 0, sizeof(del));
		
		scanf("%d", &na);
		for (i = 0; i < na; i++){
			scanf("%s", sa[i]);
			int id1 = sa[i][0]-'A', id2 = sa[i][1]-'A';
			check[id1][id2] = check[id2][id1] = 1;
			change[id1][id2] = change[id2][id1] = sa[i][2];
		}
		scanf("%d", &nb);
		for (i = 0; i < nb; i++){
			scanf("%s", sb[i]);
			int id1 = sb[i][0]-'A', id2 = sb[i][1]-'A';
			del[id1][id2] = del[id2][id1] = 1;
		}
		scanf("%d", &n);
		scanf("%s", s);
		ss = s;
		
		while (true){
			vector<char> vs;
			vs.clear();
			memset(exist, 0, sizeof(exist));	
			for (i = 0; i < ss.length(); i++){
				vs.push_back(ss[i]);
				
				while (vs.size() >= 2){
					int id1 = vs[vs.size()-1]-'A', id2 = vs[vs.size()-2]-'A';
					if (check[id1][id2]){
						vs.pop_back();
						vs.pop_back();
						vs.push_back(change[id1][id2]);
					} else
						break;
				}
				
				if (vs.size() >= 2){
				int id2 = vs.back()-'A';
				for (j = 0; j < (int)vs.size()-1; j++){
					int id1 = vs[j]-'A';
					//printf("id1 = %c, id2 = %c\n", id1+'A', id2+'A');
					if (del[id1][id2]){
						//printf("OUEEEEYEYEYE\n");
						vs.clear();
						break;
					}
				}
				}
			}
			
			string st = "";
			for (i = 0; i < vs.size(); i++)
				st += vs[i];
			
			//printf("st = %s\n", st.c_str());
			if (st == ss)
				break;
			ss = "";
			ss = st;
		}
		printf("Case #%d: [", t);
		if (ss.length() > 0){
		for (i = 0; i < ss.length()-1; i++)
			printf("%c, ", ss[i]);
		printf("%c", ss[ss.length()-1]);	
		}
		printf("]\n");
	}
	
	return 0;
}


		
		
		
		
		