#include<iostream>
#include<vector>
#include<utility>
#include<algorithm>

using namespace std;

int main(){
	int C; cin >> C;
	for(int t=1; t<=C; t++){
		int N, M;
		cin >> N >> M;
		bool shake[2008];
		memset(shake,0,sizeof(shake));
		int malt[2008], nomalt[2008];
		memset(malt,-1,sizeof(malt));
		memset(nomalt,0,sizeof(nomalt));
		//input
		bool cust[2008][2008][2];
		memset(cust,0,sizeof(cust));
		for(int i=0; i<M; i++){
			int T; cin >> T;
			for(int j=0; j<T; j++){
				int x,y; cin >> x >> y;
				x--;
				cust[i][x][y]=1;
				if(y)malt[i]=x;
				else nomalt[i]++;
			}
		}

		bool caredfor[2008];
		memset(caredfor,0,sizeof(caredfor));
		int impossible=0;
		while(1){
			int needmalt=-1;
			for(int i=0; i<M; i++){
				if(nomalt[i]==0 && !caredfor[i]){
					if(malt[i]!=-1)
						needmalt=i;
					else impossible=1;
					break;
				}
			}
			if(impossible)break;
			if(needmalt==-1)break;
			
			shake[malt[needmalt]]=1;
			for(int i=0; i<M; i++){
				if(cust[i][malt[needmalt]][0]==1){
					cust[i][malt[needmalt]][0]=0;
					nomalt[i]--;
				}
			}
			caredfor[needmalt]=1;
		}

		cout << "Case #" << t << ": ";
		if(impossible)cout << "IMPOSSIBLE\n";
		else{
			for(int i=0; i<N; i++)
				cout << shake[i] << " ";
			cout << "\n";
		}
	}
}
