#include<iostream>
using namespace std;
const int N=110;

struct node
{
	int win,total;
	int opponent[N];
	double op_owp[N];
	double WP,OWP,OOWP;
};

struct node player[N];
char input[N][N];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w+",stdout);
	int tot_cas,cas;
	int i,j,k;
	int length;
	int p;
	double sum;
	scanf("%d",&tot_cas);
	cas=1;
	while(cas<=tot_cas)
	{
		memset(player,0,sizeof(player));
		memset(input,0,sizeof(input));
		scanf("%d",&length);
		for(i=0;i<length;i++)
			scanf(" %s",input+i);
		for(i=0;i<length;i++)
		{
			for(j=0;j<length;j++)
			{
				if(input[i][j]!='.')
				{
					player[i].opponent[player[i].total]=j;
					player[i].total++;
					if(input[i][j]=='1')
						player[i].win++;
				}
			}
		}
		for(i=0;i<length;i++)
		{
			player[i].WP=1.0*player[i].win/player[i].total;
		}
		int p;
		for(i=0;i<length;i++)
		{
			for(j=0;j<player[i].total;j++)
			{
				p=player[i].opponent[j];
				if(input[i][p]=='1')
				{
					player[i].op_owp[j]=1.0*player[p].win/(player[p].total-1);
				}
				else
				{
					player[i].op_owp[j]=1.0*(player[p].win-1)/(player[p].total-1);
				}
			}
		}		
		for(i=0;i<length;i++)
		{
			sum=0;
			for(j=0;j<player[i].total;j++)
			{
				sum+=player[i].op_owp[j];
			}
			player[i].OWP=sum/player[i].total;
		}
		for(i=0;i<length;i++)
		{
			sum=0;
			for(j=0;j<player[i].total;j++)
			{
				p=player[i].opponent[j];
				sum+=player[p].OWP;
			}
			player[i].OOWP=sum/player[i].total;
		}
		printf("Case #%d:\n",cas);
		for(i=0;i<length;i++)
		{
			sum=0.25*player[i].WP+0.5*player[i].OWP+0.25*player[i].OOWP;
			printf("%lf\n",sum);
		}
		cas++;
	}
	return 0;
}
