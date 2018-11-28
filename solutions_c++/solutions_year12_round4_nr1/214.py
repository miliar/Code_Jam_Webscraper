#include<fstream>
#include<iostream>
#include<algorithm>
#include<queue>
#include<vector>
using namespace std;
int main(){
	ifstream in("A.in"); ofstream out("A.out");
	int T;
	in>>T;

	for (int t=0;t<T;t++){
		int N;
		in>>N;
		int d[N], len[N];
		int dp[N];
		for (int n=0;n<N;n++){
			in>>d[n]>>len[n];
			dp[n] = -1;
		}
		int D;
		in>>D;
		dp[0] = 2*d[0];
		for (int i=0;i<N;i++){
			for (int j=i+1; (j<N)&&(d[j]<=dp[i]); j++){
				int swing = min(d[j]-d[i],len[j]);
				if (d[j]+swing>dp[j]){
					dp[j]=d[j]+swing;
				}
			}
		}
		bool cando = false;
		for (int i=0;i<N;i++){
			if (dp[i]>=D) cando = true;
		}
		out<<"Case #"<<t+1<<": ";
		if (cando) out<<"YES\n";
		else out<<"NO\n";
	}
	

}
