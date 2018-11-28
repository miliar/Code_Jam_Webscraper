#define INF 2000000
#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

int main()
{
	long long f[100][100],N,K,B,T,i,j,k,test,numtest,pos[100],speed[100],ans;
	
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	cin >> numtest;
	for(test=1;test<=numtest;test++)
	{
		cin >> N >> K >> B >> T;
		for(i=1;i<=N;i++) cin >> pos[i];
		for(i=1;i<=N;i++) cin >> speed[i];
			
		for(i=1;i<=N;i++)
			for(j=0;j<=K;j++) f[i][j]=INF;
		for(i=1;i<=N;i++) if(speed[i]*T+pos[i]>=B) f[i][1]=N-i;
		for(i=N;i>=1;i--) if(speed[i]*T+pos[i]>=B) 
			for(j=2;j<=K;j++) 
				for(k=i+1;k<=N;k++) if(f[k][j-1]+N-i-j+1<f[i][j]) f[i][j]=f[k][j-1]+N-j-i+1;
		ans=INF;
		if(K==0) ans=0;
		for(i=N;i>=1;i--) if(f[i][K]<ans) ans=f[i][K];
		if(ans>INF/2) cout <<"Case #"<<test <<": IMPOSSIBLE" << endl;
		else cout <<"Case #" << test << ": " << ans << endl;		
	}
	return 0;
}
