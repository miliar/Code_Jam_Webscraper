#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int n,m,tc;
string dic[10011];
queue<string> q;
string push;
int hasil;

int main(){
	int i,j,ii;
	char dumi;
	
	scanf("%d %d %d%c",&n,&m,&tc,&dumi);
	for (i=0;i<m;i++){
		cin >> dic[i];
	}
	scanf("%c",&dumi);
	sort(dic,dic+m);
	for (ii=0;ii<tc;ii++){
		hasil=0;
		vector<char> haha[10000];
		for (j=0;j<n;j++){
			scanf("%c",&dumi);
			if (dumi=='('){
				scanf("%c",&dumi);
				while(dumi!=')'){	
					haha[j].push_back(dumi);
					scanf("%c",&dumi);
				}
			} else {
				haha[j].push_back(dumi);
			}
			sort(haha[j].begin(),haha[j].end());
		}
		scanf("%c",&dumi);	
		j=0;
		//printf("%d*(*(&\n",haha[0].size());
		for (i=0;i<haha[0].size();i++){
			push=haha[0][i];
			//cout << push;
			//puts("~~~");
			while (j<m && haha[0][i]>dic[j][0]) 
				j++;
			//cout << j << endl;
			if (j<m && push[0]==dic[j][0])
				q.push(push);	
		}
		j=0;
		int lvl=1;
		while (!q.empty()){
			string top=q.front();
			q.pop();
			//cout << top << endl;
			
			if (top.length() > lvl) {
				j=0;
				lvl++;	
			}
			
			if (lvl==n){
				hasil++;
				continue;
			}
			for (i=0;i<haha[lvl].size();i++){
				push=top+haha[lvl][i];
				while (j<m && push>dic[j].substr(0,lvl+1)) 
					j++;
				if (j<m && push==dic[j].substr(0,lvl+1))
					q.push(push);
			}
			
		}
		printf("Case #%d: ",ii+1);
		printf("%d\n",hasil);
	}
	return 0;	
}
