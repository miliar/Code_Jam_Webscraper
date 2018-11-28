#include<cstdio>
#include<cstring>
#include<vector>
#include<set>
#include<algorithm>
using namespace std;
#define N 100005
int p[N];
bool f[N];

void init()//Ð¡Êý¾Ý
{
	int i,j,m=0;
	f[0]=f[1]=1;
	for(i=4;i<=N;i+=2)
		f[i]=1;
	for(i=3;i*i<=N;i+=2)
		if(!f[i])
			for(j=i*i;j<=N;j+=i*2)
				f[j]=1;
	for(i=2;i<=N;i++)
		if(!f[i])
			p[m++]=i;
}
int main()
{
	freopen("d:\\data\\C-small-attempt1.in","r",stdin);
	freopen("d:\\data\\C-small-attempt1.out","w",stdout);
	init();
	int t,n,a[105],l,h,m,i,j,c=0,ans;
	scanf("%d",&t);
	while(t--)
	{
		//printf("t=%d\n",t);
		//set<int> s;
		//set<int>::iterator it;
		//ans=1;
		scanf("%d%d%d",&n,&l,&h);//
		//printf("%d  %d  %d\n",n,l,h);
		for(j=0;j<n;j++)
		{
			scanf("%d",&a[j]);
			//printf("%d ",a);//
			/*for(i=0;p[i]*p[i]<=a;i++)
				if(a%p[i]==0)	
				{
					while(a%p[i]==0)
					{
						a/=p[i];						
					}
					s.insert(p[i]);
				}
			if(a)
				s.insert(a);*/
		}
		
		int ff=0;
		for(i=l;i<=h;i++)
		{
			int f=1;
			for(j=0;j<n;j++)
				if(!(a[j]%i==0||i%a[j]==0))
				{
					f=0;
					break;
				}
			if(f)
			{
				ff=1;
				break;
			}
		}
		//puts("");
		//for(i=0;i<s.size();i++)
		//	ans*=s[i];
		//for(it=s.begin();it!=s.end();++it)
		//	ans*=*it;
		printf("Case #%d: ",++c);
		
		if(ff)
			printf("%d\n",i);
		else 
			puts("NO");
	}
}
