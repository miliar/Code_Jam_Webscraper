#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<algorithm>
#include<sstream>
#include<cmath>
using namespace std;

char q[200],b[200][200],a[200];
typedef struct node
{
	int st,ed,si;
}node;
node sa[105],sb[105];
int cmp(node a,node b)
{
	return a.st<b.st||a.st==b.st&&a.ed<b.ed;
}
int num;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t,n;
	int T,i,j,si[200];
	int na,nb,nab;
	scanf("%d",&n);
	for(t=1;t<=n;t++)
	{
		int len=0;
		scanf("%d%d%d",&T,&na,&nb);
        for(i=0;i<na;i++)
		{
			scanf("%s",a);

			sa[++len].st=((a[0]-'0')*10+(a[1]-'0'))*60+(a[3]-'0')*10+(a[4]-'0');
			scanf("%s",a);
			sa[len].ed=((a[0]-'0')*10+(a[1]-'0'))*60+(a[3]-'0')*10+(a[4]-'0');
			sa[len].si=0;
		}
		memset(si,0,sizeof(si));
        for(i=0;i<nb;i++)
		{
			scanf("%s",a);

			sa[++len].st=((a[0]-'0')*10+(a[1]-'0'))*60+(a[3]-'0')*10+(a[4]-'0');
			scanf("%s",a);
			sa[len].ed=((a[0]-'0')*10+(a[1]-'0'))*60+(a[3]-'0')*10+(a[4]-'0');
			sa[len].si=1;
		}
		nab=na+nb;
		sort(sa+1,sa+nab+1,cmp);
	//	for(i=1;i<=nab;i++)
	//		cout<<sa[i].st<<endl;
		num=0;
		int e=0,es=0;
		int sum[2],now,pos,sign;
		sum[0]=sum[1]=0;
		while(1)
		{
			es=0;
			for(i=1;i<=nab;i++)
				if(si[i]==0)
				{
					si[i]=1;
					
					sum[sa[i].si]++;
					num++;
					now=sa[i].ed;
					pos=i;
					es=1;
					sign=1-sa[i].si;
                   while(1)
				   {
						
						e=0;
						for(j=pos+1;j<=nab;j++)
							if(si[j]==0&&sa[j].si==sign&&now+T<=sa[j].st)
							{
								num++;
								sign=1-sign;
								now=sa[j].ed;
								si[j]=1;
								pos=j;
							    e=1;
								es=1;
								break;

							}
							if(e==0)break;

				   }

				}
			//	cout<<num<<endl;
				if(num==nab||es==0)break;
				
		}
		printf("Case #%d: %d %d\n",t,sum[0],sum[1]);
	}
	return 0;
}