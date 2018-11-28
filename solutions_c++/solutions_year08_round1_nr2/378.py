#include<iostream>
#include<vector>
using namespace std;

int stak[3000],bol[3000];
int tc,n,m,i,j,sisa,bnyk,x,y,z;
vector<int> suka[3000][2];
bool ketemu;

void dfs(int crnt) {
	int i,j;
	//cout<<"crnt: "<<crnt<<endl;
	//getchar();
	if((crnt>n)&(sisa==0)) {
		for(i=1;i<crnt;i++) printf(" %d",stak[i]);
		cout<<endl;
		ketemu=1;
	}
	else if(crnt>n) {}
	else {
		if(!ketemu) {
			for(i=0;i<2;i++) {
				if(ketemu) break;
				stak[crnt]=i;
				for(j=0;j<suka[crnt][i].size();j++) {
					bol[suka[crnt][i][j]]++;
					if(bol[suka[crnt][i][j]]==1) sisa--;
				}
				dfs(crnt+1);
				for(j=0;j<suka[crnt][i].size();j++) {
					bol[suka[crnt][i][j]]--;
					if(bol[suka[crnt][i][j]]==0) sisa++;
				}
			}
		}
	}
}	
	
int main() {
	freopen("milk.out","w",stdout);
	cin>>tc;
	for(x=1;x<=tc;x++) {
		cout<<"Case #"<<x<<":";
		cin>>n>>m;
		for(i=0;i<=n;i++) {
			suka[i][0].clear();
			suka[i][1].clear();
		}
		for(i=1;i<=m;i++) {
			bol[i]=0;
			cin>>bnyk;
			for(j=0;j<bnyk;j++) {
				cin>>z>>y;
				suka[z][y].push_back(i);
			}
		}
		ketemu=0;
		sisa=m;
		dfs(1);
		if(!ketemu) cout<<" IMPOSSIBLE"<<endl;
	}
}

