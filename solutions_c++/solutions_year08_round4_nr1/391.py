#include<iostream>
#include<cstdlib>
#include<cmath>
using namespace std;

#define MAXM 10005
int N, M, iM;
int G[MAXM], C[MAXM];
int minc[MAXM][2];

int main(){
	cin >> N;
	for(int t=1; t<=N; t++){
		cin >> M;
		int V; cin >> V;
		iM = (M-1)/2;
		for(int i=1; i<=iM; i++)
			cin >> G[i] >> C[i];
		memset(minc,-1,sizeof(minc));
		for(int i=iM+1; i<=M; i++){
			int I; cin >> I;
			minc[i][I]=0;
		}

		for(int i=iM; i>0; i--)for(int j=0; j<2; j++){
			for(int ln=0; ln<2; ln++)for(int rn=0; rn<2; rn++){
				int c;
				if(minc[i*2][ln]!=-1 && minc[i*2+1][rn]!=-1){
					c=-1;
					if( (ln || rn) == j){
						if(G[i]==0)
							c = minc[i*2][ln] + minc[i*2+1][rn];
						else if(G[i]==1 && C[i]==1)
							c = minc[i*2][ln] + minc[i*2+1][rn] + 1;
					}
					if(c!= -1 && (minc[i][j]==-1 || c < minc[i][j]))
						minc[i][j]=c;

					c=-1;
					if( (ln && rn) == j){
						if(G[i]==1)
							c = minc[i*2][ln] + minc[i*2+1][rn];
						else if(G[i]==0 && C[i])
							c = minc[i*2][ln] + minc[i*2+1][rn] + 1;
					}
					if(c!= -1 && (minc[i][j]==-1 || c < minc[i][j]))
						minc[i][j]=c;
				}
			}	
		}

		cout << "Case #" << t << ": ";
		if(minc[1][V]!=-1)cout << minc[1][V] << "\n";
		else cout << "IMPOSSIBLE\n";
	}
}
