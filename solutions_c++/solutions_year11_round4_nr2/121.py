#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
#define oo 505
long long X[oo][oo],Y[oo][oo];
long long sX[oo][oo],sY[oo][oo];
long long S[oo][oo];
char ch[oo][oo];

int R,C,D;

inline void Readin()
{
	cin >> R >> C >> D;
	for (int i=1;i<=R;++i)
		cin >> ch[i]+1;
}

inline void Solve()
{
	memset(X,0,sizeof X);
	memset(sX,0,sizeof X);
	memset(Y,0,sizeof Y);
	memset(sY,0,sizeof Y);
	memset(S,0,sizeof Y);
	
	for (int i=1;i<=R;++i)
		for (int j=1;j<=C;++j)
		{
			X[i][j] += i*(ch[i][j]-'0'+D);
			Y[i][j] += j*(ch[i][j]-'0'+D);
		}
	
	for (int i=1;i<=R;++i)
		for (int j=1;j<=C;++j)
		{
			sX[i][j] = sX[i][j-1] + sX[i-1][j] - sX[i-1][j-1] + X[i][j];
			sY[i][j] = sY[i][j-1] + sY[i-1][j] - sY[i-1][j-1] + Y[i][j];
			S[i][j] = S[i][j-1] + S[i-1][j] -S[i-1][j-1] + (ch[i][j]-'0'+D);
		}
	
	int ans = 0;
	for (int k= min(R,C);k>=3;--k)
		for (int i= 0; i+k-1 <R;++i)
			for (int j=0; j+k-1 <C;++j)
			{
				long long x=0,y=0, s;
				x = sX[i+k][j+k] - sX[i][j+k] - sX[i+k][j] + sX[i][j];
				y = sY[i+k][j+k] - sY[i][j+k] - sY[i+k][j] + sY[i][j];
				
				x -= X[i+k][j+k] + X[i+1][j+1] + X[i+1][j+k] + X[i+k][j+1];
				y -= Y[i+k][j+k] + Y[i+1][j+1] + Y[i+1][j+k] + Y[i+k][j+1];
				
				s = S[i+k][j+k] - S[i][j+k] - S[i+k][j] + S[i][j];
				s -= ch[i+k][j+k] + ch[i+1][j+1] + ch[i+1][j+k] + ch[i+k][j+1] - 48*4 + D*4;
				
				x*=2,y*=2;
				
				if (x % s == 0 && y % s ==0)
				{
					if (x/s == (i+1 + i+k) && y/s == (j+1 + j+k))
					{
						ans = k;
						goto End;
					}
				}
			}
	End: ;
	
	if (ans) printf("%d\n",ans);
	else puts("IMPOSSIBLE");
}

int main()
{
	//freopen("i.txt","r",stdin);
	
	int Test,Case = 0;
	for (scanf("%d",&Test);Test--;)
	{
		printf("Case #%d: ",++Case);
		Readin();
		Solve();
	}
	return 0;
}
