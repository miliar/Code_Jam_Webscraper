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

bool ff[1024];
int w[1024];
int e[1024];
int x;

int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int i,j,k,t;
	int ncase;
	int icase=1;
	int a,b,p;
	int ans;
	memset(ff,true,sizeof(ff));
	for(i=2;i<1024;i++)
		if(ff[i])
			for(j=i*i;j<1024;j+=i)
				ff[j]=false;
	for(scanf("%d",&ncase);ncase--;)
	{
		scanf("%d%d%d",&a,&b,&p);
		for(i=a;i<=b;i++)
			w[i]=i;
		int now=1024;
		for(;p<=b;p++)
			if(ff[p])
			{
				x=0;
				i=((a-1)/p+1)*p;
				for(;i<=b;i+=p)
					e[x++]=w[i];
				for(i=a;i<=b;i++)
				{
					for(j=0;j<x;j++)
						if(w[i]==e[j])
							break;
					if(j<x)w[i]=now;
				}
				now++;
			}
		for(ans=0,i=a;i<=b;i++)
		{
			for(j=i+1;j<=b;j++)
				if(w[i]==w[j])
					break;
			if(j>b)ans++;
		}
		printf("Case #%d: %d\n",icase++,ans);
	}
	return 0;
}




