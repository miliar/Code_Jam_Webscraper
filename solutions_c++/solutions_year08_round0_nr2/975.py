#include <iostream>
#include <queue>
#include <memory>
using namespace std;

int a[500][500];//
int b[500][500];
int cost[500][500];

int ta[200][2];
int tb[200][2];
int na,nb;
int D;

int turn;

void out(int m[500][500])
{
	int i,j;
	for(i=0;i<=D;i++)
	{
		for(j=0;j<=D;j++)
		{
			cout<<m[i][j]<<' ';
		}
		cout<<endl;
	}
	cout<<"-----------------------------------"<<endl;
}

int ad[4000],aa[4000],bd[4000],ba[4000];

int main()
{
	int T;
	freopen("B-large.in", "r", stdin);
	freopen("outL.txt", "w", stdout);
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		memset(ad,0,sizeof(ad));
		memset(aa,0,sizeof(aa));
		memset(bd,0,sizeof(bd));
		memset(ba,0,sizeof(ba));

		int i,j;
		int hh,mm,ss;
		cin>>turn;
		cin>>na>>nb;
		for(i=0;i<na;i++)
		{
			scanf("%d:%d",&hh,&mm);
			ta[i][0] = mm+60*hh;
			ad[mm+60*hh]++;
			scanf("%d:%d",&hh,&mm);
			ta[i][1] = mm+60*hh+turn;
			aa[mm+60*hh+turn]++;
		}
		for(i=0;i<nb;i++)
		{
			scanf("%d:%d",&hh,&mm);
			tb[i][0] = mm+60*hh;
			bd[mm+60*hh]++;
			scanf("%d:%d",&hh,&mm);
			tb[i][1] = mm+60*hh+turn;
			ba[mm+60*hh+turn]++;
		}
		int ac=0,bc=0;
		int ra=0,rb=0;
		for(i=0;i<60*60;i++)
		{
			ac+=ba[i];
			bc+=aa[i];
			while(ad[i]--)
			{
				if(ac==0)
					ra++;
				else
					ac--;
			}
			while(bd[i]--)
			{
				if(bc==0)
					rb++;
				else
					bc--;
			}
		}
		/*for(i=0;i<500;i++)
		{
			for(j=0;j<500;j++)
			{
				cost[i][j]=1;
			}
		}
		int C = 2*(na-1) + 2;
		D = C + 2*nb + 2;
		for(i=0;i<na;i++)
		{
			a[1][2*i+2] = 1;
			a[2*i+2][2*i+3] = 1;
			a[2*i+3][D] = 1;
			cost[2*i+2][2*i+3] = 0;
		}
		for(i=0;i<nb;i++)
		{
			a[1][C+2*i+2] = 1;
			a[C+2*i+2][C+2*i+3] = 1;
			a[C+2*i+3][D] = 1;
			cost[C+2*i+2][C+2*i+3] = 0;
		}
		for(i=0;i<na;i++)
		{
			for(j=0;j<nb;j++)
			{
				if(ta[i][1]<=tb[j][0])
				{
					a[2*i+3][C+2*j+2] = 1;
					cost[2*i+3][C+2*j+2] = 0;
				}
				else if(tb[j][1]<=ta[i][0])
				{
					a[C+2*j+3][2*i+2] = 1;
					cost[C+2*j+3][2*i+2] = 0;
				}
			}
		}
		out(a);
		int ra=0,rb=0;
		for(i=0;i<C;i++)
		{
			if(b[1][i]==1)
			{
				ra++;
			}
		}
		for(;i<D;i++)
		{
			if(b[1][i]==1)
			{
				rb++;
			}
		}*/
		printf("Case #%d: %d %d\n",t,ra,rb);
	}
	return 0;
}