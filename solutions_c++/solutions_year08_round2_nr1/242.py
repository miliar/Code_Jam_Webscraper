#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <set>
#include <algorithm>
using namespace std;

typedef long long LL;
typedef long double LD;

typedef vector<int> VI;

int main()
{
	int ttt;
	cin >> ttt;
	for(int cutest=1;cutest<=ttt;cutest++){
		LL n,A,B,C,D,x0,y0, M;
		
		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		
		vector<LL> x(n), y(n);
		
		LL xx=x0, yy=y0;
		for(int i=0;i<n;i++){
			x[i]=xx;
			y[i]=yy;
			
			xx=(A*xx+B)%M;
			yy=(C*yy+D)%M;
		}
		
		LL ans=0;
		
		for(int i=0;i<n;i++)
		for(int j=i+1;j<n;j++)
		for(int k=j+1;k<n;k++){
			LL tx= x[i]+x[j]+x[k];
			LL ty= y[i]+y[j]+y[k];
			
			if(tx%3 || ty%3)
				continue;
			ans++;
			
/*			printf(" %d %d %d --\n",i,j,k);
			printf("X: %Ld",	x[i]);
			printf(" %Ld",		x[j]);
			printf(" %Ld\n",	x[k]);
			
			printf("Y: %Ld",	y[i]);
			printf(" %Ld",		y[j]);
			printf(" %Ld\n",	y[k]);*/
		}
		printf("Case #%d: %Ld\n", cutest,ans);
	}

}
