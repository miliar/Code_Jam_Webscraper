#include<fstream>
#include<iostream>
#include<string>
#include<set>
#include<cassert>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
	ifstream is("2010Round1B\\B.txt");	
	ofstream os("2010Round1B\\Bo.txt");
	int C;
	while(is>>C)
	{
		for (int i = 1; i <= C; ++i)
		{
			int N, K, B, T;  is>>N>>K>>B>>T;
			vector<int> X(N), V(N);
			for (int x = 0; x < N; ++x)
				is>>X[x];
			for (int x = 0; x < N; ++x)
				is>>V[x];

			os<<"Case #"<<i<<": ";

			vector<bool> can(N, false);
			for (int x = 0; x < N; ++x)
				if (((long long)V[x])*T>=B-X[x])
					can[x] = true;
			vector<int> M(N, 0);
			for (int x = N-1; x >= 0; --x)
				if (can[x]){
					for (int y = x+1; y < N; ++y){
							if (V[y]<V[x] && !can[y])
							if (((long long)V[x])*(B-X[y]) > ((long long)V[y])*(B-X[x]))
								M[x]++;
					}
				}
				else
					M[x] = 100;
			sort(M.begin(), M.end());

			if (K>0 && M[K-1] == 100)
				os<<"IMPOSSIBLE"<<endl;
			else{
				int res = 0;
				for (int x = 0; x < K; ++x)
					res += M[x];

				os<<res<<endl;
			}
		}
	}

}