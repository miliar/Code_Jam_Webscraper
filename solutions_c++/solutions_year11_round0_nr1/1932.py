# include <cstdio>
using namespace std;
# define N 105
# define abs(a) ((a)>0?(a):-(a))
int s[2][N],c1,c2;
bool jud[N];
int max(int a,int b)
{
	return a>b?a:b;
}

int main()
{
	int test,n;
	scanf("%d",&test);
	for(int testcase=1;testcase<=test;testcase++)
	{
		c1=c2=0;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			char type[5];
			int id;
			scanf("%s%d",type,&id);
			switch(type[0])
			{
			case 'O':
				s[0][c1++]=id;
				jud[i]=false;
				break;
			case 'B':
				s[1][c2++]=id;
				jud[i]=true;
				break;
			};
		}
		s[0][c1]=s[1][c2]=1;
		int p[]={0,0},w[]={s[0][0]-1,s[1][0]-1};
		int ans=0;
		for(int i=0;i<n;i++)
		{
			int add=(w[jud[i]]>=0?w[jud[i]]+1:1);
			ans+=add;
			p[jud[i]]++;
			w[jud[i]]=abs(s[jud[i]][p[jud[i]]]-s[jud[i]][p[jud[i]]-1]);
			w[jud[i]^1]-=add;
		}
		printf("Case #%d: %d\n",testcase,ans);
	}
	return 0;
}