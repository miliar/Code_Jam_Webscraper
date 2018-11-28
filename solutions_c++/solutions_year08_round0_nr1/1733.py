#include<iostream>
using namespace std;


int a[1024];
char c[1024][1024];
char ch[1024];
int mark[1024];

int  sn;
int  n;

int index()
{
	int i;
	for(i=1;i<=sn;i++)
		if(strcmp(ch,c[i])==0)
			return i;
	return 0;
}

int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int i,j,k,num,seq,result,cc;
	scanf("%d",&num);
	for(seq=1;seq<=num;seq++)
	{
		scanf("%d ",&sn);
		for(i=1;i<=sn;i++)
			gets(c[i]);
		scanf("%d ",&n);
		for(i=1;i<=n;i++)
		{
			gets(ch);
			a[i]=index();
		}

		memset(mark,0,sizeof(mark));
		cc=0;
		result=0;

		for(i=1;i<=n;i++)
		{
			k=a[i];
			if(mark[k]==0)
			{
				mark[k]=1;
				cc++;

				if(cc==sn)
				{
					result++;
					memset(mark,0,sizeof(mark));
					mark[k]=1;
					cc=1;
				}
			}
		}

		printf("Case #%d: %d\n",seq,result);
	}
	return 0;

}