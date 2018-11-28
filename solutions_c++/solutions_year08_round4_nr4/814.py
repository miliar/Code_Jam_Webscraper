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

int n,m,x;
char str[1024],ss[1024];
int a[8];
int ans,now;

int main()
{
	int ncase,icase=1;
	int i,j,k,t;
	freopen("1.in","r",stdin);
	freopen("wqb.out","w",stdout);
	for(scanf("%d",&ncase);ncase--;)
	{
		scanf("%d%s",&n,str);
		m=strlen(str);
		printf("Case #%d: ",icase++);
		for(i=0;i<n;i++)
			a[i]=i;
		ans=m;
		do
		{
			for(i=0;i<m;i+=n)
				for(j=0;j<n;j++)
					ss[i+j]=str[i+a[j]];
			for(now=1,i=1;i<m;i++)
				if(ss[i]!=ss[i-1])
					now++;
			if(now<ans)ans=now;
		}while(next_permutation(a,a+n));
		printf("%d\n",ans);
	}
	return 0;
}


