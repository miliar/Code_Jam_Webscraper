#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <string>
#include <map>

#define Max(a,b) ((a)>(b)?(a):(b))
#define Min(a,b) ((a)<(b)?(a):(b))
#define Mem(a,b) memset(a,b,sizeof(a))
#define Fu(i,a,b) for (int i=a;i<=b;++i)
#define Fd(i,a,b) for (int i=a;i>=b;--i)

using namespace std;

map <int , int > hash;
int n,T;
int a[500];
int f[1048578];

void outprint(int x,int y)
{
	//printf("%d %d\n",x-(x&y),y-(x&y));
	//printf("%d %d\n",x,y);
	Fu(j,1,n) if (((1<<(j-1)) & x) && ((1<<(j-1)) & y)==0) printf("%d ",a[j]);
	printf("\n");
	Fu(j,1,n) if (((1<<(j-1)) & y) && ((1<<(j-1)) & x)==0) printf("%d ",a[j]);
	printf("\n");
}

int main()
{
    //freopen("C-small-attempt0.in","r",stdin);
    //freopen("C-small-attempt0.out","w",stdout);
	scanf("%d",&T);
	Fu(test,1,T)
	{
		printf("Case #%d:\n",test);
		scanf("%d",&n);
		Fu(i,1,n) scanf("%d",&a[i]);
		int maxz=(1<<n)-1;
		hash.clear();
		Mem(f,0);
		Fu(i,1,maxz)
		{
			Fu(j,1,n) if ((1<<(j-1)) & i) f[i]+=a[j];
			if (hash.count(f[i]))
			{
				outprint(i,hash[f[i]]);
				break;
			} else 	hash[f[i]]=i;
		}
	}
	return 0;
}

