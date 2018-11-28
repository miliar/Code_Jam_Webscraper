#include <cstdio>

inline int ABS(int x)
{
	return x<0?-x:x;
}

inline int MIN(int a,int b)
{
	return a<b?a:b;
}

inline int MAX(int a,int b)
{
	return a>b?a:b;
}

int pos[200];
char seq[200];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,n;
	int i;
	int ca=1;

	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			char op[4];
			scanf("%s%d",op,&pos[i]);
			seq[i]=op[0];
		}

		int total=0;
		int pos_o=1,pos_b=1;
		int use_o=0,use_b=0;
		for(i=0;i<n;i++)
		{
			if(seq[i]=='O')
			{
				int temp=MAX(ABS(pos_o-pos[i])-use_b,0) + 1;
				total+=temp;
				use_o+=temp;
				use_b=0;
				pos_o=pos[i];
			}
			else
			{
				int temp=MAX(ABS(pos_b-pos[i])-use_o,0) + 1;
				total+=temp;
				use_b+=temp;
				use_o=0;
				pos_b=pos[i];
			}
		}
		printf("Case #%d: %d\n",ca++,total);
	}

	return 0;
}