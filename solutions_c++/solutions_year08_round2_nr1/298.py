#include<stdio.h>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<memory>
#include<math.h>
#include<time.h>
#include<string.h>
#include<algorithm>

using namespace std;

typedef vector<int> vi; 
typedef vector<string> vs; 

#define min(i,j) ((i)<(j)?(i):(j))
#define max(i,j) ((i)>(j)?(i):(j))
#define abx(i) ((i)>0?(i):(-(i)))
#define eps 1e-9

__int64 w[3][3];
__int64 a,b,c,d,x,y,m;
int n;
__int64 ans;

int main()
{
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
	int ncase;
	int i,j,k;
	int icase=1;
	for(scanf("%d",&ncase);ncase--;)
	{
		scanf("%d%I64d%I64d%I64d%I64d%I64d%I64d%I64d",&n,&a,&b,&c,&d,&x,&y,&m);
		memset(w,0,sizeof(w));
		w[x%3][y%3]++;
		for(i=1;i<n;i++)
		{
			x=(a*x+b)%m;
			y=(c*y+d)%m;
			w[x%3][y%3]++;
		}
		ans=0;
		for(i=0;i<9;i++)
			if(w[i/3][i%3])
				for(j=i+1;j<9;j++)
					if(w[j/3][j%3])
						for(k=j+1;k<9;k++)
							if(w[k/3][k%3])
								if(((i/3+j/3+k/3)%3==0)&&((i%3+j%3+k%3)%3==0))
								{
									ans+=w[i/3][i%3]*w[j/3][j%3]*w[k/3][k%3];
								}
		for(i=0;i<9;i++)
			if(w[i/3][i%3]>1)
			{
				for(j=0;j<9;j++)
					if(i!=j&&w[j/3][j%3]>0&&((i/3+j/3+i/3)%3==0)&&((i%3+j%3+i%3)%3==0))
					{
						ans+=w[i/3][i%3]*(w[i/3][i%3]-1)/2*w[j/3][j%3];
					}
			}
		for(i=0;i<9;i++)
			if(w[i/3][i%3]>2)
				ans+=w[i/3][i%3]*(w[i/3][i%3]-1)*(w[i/3][i%3]-2)/6;
		printf("Case #%d: %I64d\n",icase++,ans);
	}
	return 0;
}



