//Fruit of Light
//FoL CC
//Apple Strawberry

#include<cstdio>
#include<algorithm>
#include<vector>

using namespace std;

#define For(i, to) for(int i = 0; i<to; ++i)
#define ForEach(it, i) for(typeof i.begin() it = i.begin(); it!=i.end(); ++it)

char cog[100][5], coz[100][5], text[200];
int G,Z,L,t;
int is[200];
vector<char> q;

int main(){
	scanf("%d", &t);
	For(T,t){
		scanf("%d", &G);
		For(i, G) scanf("%s",cog[i]);
		scanf("%d", &Z);
		For(i, Z) scanf("%s",coz[i]);		
		scanf("%d", &L);
		scanf("%s",text);
		q.clear();
		For(o, 200) is[o] = 0;
		For(j, L){			
			q.push_back(text[j]);
			bool trs = 0;
			if (q.size()>=2){
				For(i, G) if((q[q.size()-1]==cog[i][0] && q[q.size()-2]==cog[i][1])
					 ||(q[q.size()-1]==cog[i][1] && q[q.size()-2]==cog[i][0])){
					is[q[q.size()-2]]--;
					q.pop_back();
					q.pop_back();
					q.push_back(cog[i][2]);
					trs = 1;
					break;
				}
			}
			if (trs) continue;
			is[text[j]]++;
			For(i, Z) if ((is[coz[i][0]]>0) && (is[coz[i][1]]>0)) {
				For(o, 200) is[o] = 0;
				q.clear();
				break;
			}	
		}
		printf("Case #%d: [",T+1);
		For(i, (int)q.size()-1) printf("%c, ",q[i]);
		if (q.size() > 0) printf("%c]\n",q[q.size()-1]);
		else  printf("]\n");
	}
}