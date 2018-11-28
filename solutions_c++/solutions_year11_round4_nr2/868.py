#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

int T;
int R,C,D;
char c[16][16];
int cake[16][16];

int main()
{
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);

	scanf("%d",&T);
	int tt;
	for(tt=1;tt<=T;++tt)
	{
		printf("Case #%d: ",tt);
		scanf("%d %d %d",&R,&C,&D);
		int i,j;
		for(i=0;i<R;++i)
				scanf("%s",c[i]);
		for(i=0;i<R;++i)
			for(j=0;j<C;++j)
				cake[i][j]=c[i][j]-'0';
		int best=-1;
		for(i=0;i<R;++i)
			for(j=0;j<C;++j)
			{
				int k=1;

				while(true)
				{
					if(i-k<0 || j-k<0 || i+k>=R || j+k>=C) break;
					int sumx=0,sumy=0;
					int ii,jj;
					for(ii=i-k;ii<=i+k;++ii)
						for(jj=j-k;jj<=j+k;++jj)
						{
							sumx+=(cake[ii][jj]+D)*(ii-i);
							sumy+=(cake[ii][jj]+D)*(jj-j);
						}
					sumx-=(cake[i-k][j-k]+D)*(-k);
					sumx-=(cake[i-k][j+k]+D)*(-k);
					sumx-=(cake[i+k][j-k]+D)*k;
					sumx-=(cake[i+k][j+k]+D)*k;

					sumy-=(cake[i-k][j-k]+D)*(-k);
					sumy-=(cake[i-k][j+k]+D)*k;
					sumy-=(cake[i+k][j-k]+D)*(-k);
					sumy-=(cake[i+k][j+k]+D)*k;
					if(sumx==0 && sumy==0 && best<k*2+1) best=k*2+1;
					k++;
				}
				k=1;
				while(true)
				{
					if(i-k<0 || i+k+1>=R || j-k<0 || j+k+1>=C) break;
					int ii,jj;
					int sumx=0,sumy=0;
					for(ii=i-k;ii<=i;++ii)
						for(jj=j-k;jj<=j;++jj)
						{
							sumx+=(cake[ii][jj]+D)*(ii-i-1);
							sumy+=(cake[ii][jj]+D)*(jj-j-1);
						}
					sumx-=(cake[i-k][j-k]+D)*(k+1)*(-1);
					sumy-=(cake[i-k][j-k]+D)*(k+1)*(-1);
					for(ii=i+1;ii<=i+k+1;++ii)
						for(jj=j-k;jj<=j;++jj)
						{
							sumx+=(cake[ii][jj]+D)*(ii-i);
							sumy+=(cake[ii][jj]+D)*(jj-j-1);
						}
					sumx-=(cake[i+k+1][j-k]+D)*(k+1);
					sumy-=(cake[i+k+1][j-k]+D)*(k+1)*(-1);
					for(ii=i-k;ii<=i;++ii)
						for(jj=j+1;jj<=j+k+1;++jj)
						{
							sumx+=(cake[ii][jj]+D)*(ii-i-1);
							sumy+=(cake[ii][jj]+D)*(jj-j);
						}
					sumx-=(cake[i-k][j+k+1]+D)*(k+1)*(-1);
					sumy-=(cake[i-k][j+k+1]+D)*(k+1);
					for(ii=i+1;ii<=i+k+1;++ii)
						for(jj=j+1;jj<=j+k+1;++jj)
						{
							sumx+=(cake[ii][jj]+D)*(ii-i);
							sumy+=(cake[ii][jj]+D)*(jj-j);
						}
					sumx-=(cake[i+k+1][j+k+1]+D)*(k+1);
					sumy-=(cake[i+k+1][j+k+1]+D)*(k+1);
					if(sumx==0 && sumy==0 && best<(k+1)*2) best=(k+1)*2;
					++k;
				}
			}
		if(best==-1) printf("IMPOSSIBLE\n");
		else printf("%d\n",best);
	}
	return 0;
}
