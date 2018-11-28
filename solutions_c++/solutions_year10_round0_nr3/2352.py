#include<iostream>
#include<fstream>
using namespace std;

int main(){
	ifstream is("2010Qua\\C.txt");	
	ofstream os("2010Qua\\Co.txt");
	int C;
	while(is>>C)
	{
		for (int i = 1; i <= C; ++i)
		{
			int R, K, N;  is>>R>>K>>N;
			int G[1005]; int T = 0;
			for (int j = 0; j < N; ++j){
				is>>G[j];	T += G[j];
			}
			os<<"Case #"<<i<<": ";
			if (T <= K)
			{
				os << ((long long)T) * R<<endl;
				continue;
			}

			int M[1005];  memset(M, 0, sizeof(M));
			int next[1005];  
			int f = 0;
			for (int j = 0; j < N; ++j){
				if (M[0]+G[j] <= K)
					{M[0] += G[j];	f = j;}
				else break;
			}
			next[0] = (f+1)%N;
			for (int j = 1; j < N; ++j){
				M[j] = M[j-1];
				M[j] -= G[j-1];
//				cout<<j<<","<<M[j]<<endl;
				for (;;){
					if (M[j] + G[(f+1)%N] > K) break;
					else {
						f = (f+1)%N;
						M[j] += G[f];
					}
				}
//				cout<<j<<"."<<M[j]<<endl;
				next[j] = (f+1)%N;
			}

			long long memo[31][1005];  memset(memo, 0, sizeof(memo));
			int nxt[31][1005];
			for (int j = 0; j < N; ++j){
				memo[0][j] = M[j], nxt[0][j] = next[j];
//				cout<<memo[0][j]<<" ";
			}
//			cout<<endl;
			for (int round = 1; round < 31; round ++)
			{
				for (int j = 0; j < N; ++j){
					memo[round][j] = memo[round-1][j] + memo[round-1][nxt[round-1][j]];
					int t = nxt[round-1][j];
					nxt[round][j] = nxt[round-1][t];
//					cout<<memo[round][j]<<" ";
				}
//				cout<<endl;
			}

			long long res = 0;
			int st = 0;
			for (int j = 0; j < 31; ++j)
				if (R & (1<<j)){
					res += memo[j][st];
					st = nxt[j][st];
				}
			os<<res<<endl;
		}
	}

}