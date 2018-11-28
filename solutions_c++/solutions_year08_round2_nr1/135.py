#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cmath>
using namespace std;
int kol[3][3],n,N,A,B,C,D,x,y,i,j,k,l,m;
long long ans,tmp,xx,yy;
int main()
{

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d\n",&N);
	for(j=0;j<N;j++)
	{
		scanf("%d%d%d%d%d%d%d%d\n",&n,&A,&B,&C,&D,&x,&y,&m);
		for(i=0;i<3;i++)
		{
			for(k=0;k<3;k++)
			{
				kol[i][k]=0;
			}
		}
		kol[x%3][y%3]++;
		xx=x;
		yy=y;
		for(i=1;i<n;i++)
		{
			xx=(A*xx+B)%m;
			yy=(C*yy+D)%m;
			kol[xx%3][yy%3]++;
		}
		ans=0;
		for(i=0;i<9;i++)
		{
			tmp=kol[i%3][i/3];
			tmp*=(kol[i%3][i/3]-1);
			tmp*=(kol[i%3][i/3]-2);
			tmp/=6;
			ans+=tmp;
		}
		for(i=0;i<7;i++)
		{
			for(k=i+1;k<8;k++)
			{
				for(l=k+1;l<9;l++)
				{
					if ((((i%3)+(k%3)+(l%3))%3==0)&&(((i/3)+(k/3)+(l/3))%3==0))
					{
						tmp=kol[i%3][i/3];
						tmp*=(kol[k%3][k/3]);
						tmp*=(kol[l%3][l/3]);
						ans+=tmp;					
					}
				}
			}
		}
		cout<<"Case #"<<j+1<<": "<<ans<<endl;
	}
	return 0;
}