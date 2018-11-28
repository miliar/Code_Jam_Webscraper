# include <iostream>
# include <cstdio>
# include <algorithm>
# include <cmath>
# include <string>
# include <vector>
using namespace std;

int G[30000];
int C[30000];
int state[30000];
int M,V;

int ans[30000][2];

int solve(int a,  int b){

	if(ans[a][b] < 1000000) return ans[a][b];

	if(a > (M-1)/2){
		if(state[a]==b)ans[a][b] = 0;
		return ans[a][b];
	}


	if(G[a]==0){

		if(b==0){
			ans[a][b] = min(ans[a][b], solve(2*a,0) + solve(2*a+1,0));
		}else{
			ans[a][b] = min(ans[a][b], solve(2*a,0) + solve(2*a+1,1));
			ans[a][b] = min(ans[a][b], solve(2*a,1) + solve(2*a+1,0));
			ans[a][b] = min(ans[a][b], solve(2*a,1) + solve(2*a+1,1));
		}

	}else{
		if(b==0){
			ans[a][b] = min(ans[a][b], solve(2*a,0) + solve(2*a+1,0));
			ans[a][b] = min(ans[a][b], solve(2*a,0) + solve(2*a+1,1));
			ans[a][b] = min(ans[a][b], solve(2*a,1) + solve(2*a+1,0));
		}else{
			ans[a][b] = min(ans[a][b], solve(2*a,1) + solve(2*a+1,1));
		}
	}
	
	if(C[a]==1){

			if(G[a]==1){

				if(b==0){
					ans[a][b] = min(ans[a][b], solve(2*a,0) + solve(2*a+1,0) + 1);
				}else{
					ans[a][b] = min(ans[a][b], solve(2*a,0) + solve(2*a+1,1) + 1);
					ans[a][b] = min(ans[a][b], solve(2*a,1) + solve(2*a+1,0) + 1);
					ans[a][b] = min(ans[a][b], solve(2*a,1) + solve(2*a+1,1) + 1);
			}

			}else{
				if(b==0){
					ans[a][b] = min(ans[a][b], solve(2*a,0) + solve(2*a+1,0) + 1);
					ans[a][b] = min(ans[a][b], solve(2*a,0) + solve(2*a+1,1) + 1);
					ans[a][b] = min(ans[a][b], solve(2*a,1) + solve(2*a+1,0) + 1);
				}else{
					ans[a][b] = min(ans[a][b], solve(2*a,1) + solve(2*a+1,1) + 1);
			}
	}


	}

	return ans[a][b];




}



int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int TT;

	cin >> TT;
	


	for(int tt = 1; tt <= TT; tt++){
		
		cin >> M >> V;

		for(int i = 1; i <= (M-1)/2; i++){
			cin >> G[i] >> C[i];
		}

		for(int i = (M-1)/2 + 1; i <= M; i++){
			cin >> state[i];
		}

		for(int i = 0; i < 30000; i++) ans[i][0] = ans[i][1] = 1000000;


		solve(1,V);

		if(ans[1][V] >= 1000000)cout << "Case #" << tt <<": IMPOSSIBLE" << endl;
		else cout << "Case #" << tt <<": " << ans[1][V] << endl;
	}




}

