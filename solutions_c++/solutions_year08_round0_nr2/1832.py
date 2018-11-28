#include<stdio.h>
#include<algorithm>
using namespace std;
struct t
{
	int dh,dm,rh,rm,sta;
}a[300];

bool dcmp(const t &a, const t & b) 
{
    if(a.dh < b.dh) return true;
	if(a.dh > b.dh) return false;
	if(a.dm < b.dm) return true;
	else return false;	
}

bool rcmp(const t &a, const t & b) 
{
    if(a.rh < b.rh) return true;
	if(a.rh > b.rh) return false;
	if(a.rm < b.rm) return true;
	else return false;	
}

bool rdcmp(const t &a, const t & b) 
{
    if(a.rh < b.dh) return true;
	if(a.rh > b.dh) return false;
	if(a.rm <= b.dm) return true;
	else return false;	
}

int main()
{
	//freopen("test.txt","r",stdin);
	//freopen("out.txt","w",stdout);	
	int n,t,na,nb,i,j,l,tot;	
	bool goon;
	scanf("%d",&n);
	for(l=1;l<=n;l++)
	{			
		scanf("%d",&t);
		scanf("%d %d",&na,&nb);			
		tot=na+nb;
		for(i=0;i<tot;i++)
		{
			scanf("%d:%d %d:%d",&a[i].dh,&a[i].dm,&a[i].rh,&a[i].rm);
			a[i].rm+=t;
			if(a[i].rm>60){a[i].rh++;a[i].rm-=60;}
			a[i].sta=0;
		}		
		goon=true;
		while(goon)
		{					
			goon=false;			
			sort(a,a+na,rcmp);			
			sort(a+na,a+tot,dcmp);
			for(i=0;i<na;i++)
			{
				if(a[i].sta==1 || a[i].sta ==2)continue;
				for(j=na;j<tot;j++)
				{
					if(a[j].sta==0 || a[j].sta==1)
						if( rdcmp(a[i], a[j]) )
						{
							if(a[i].sta==0)a[i].sta=1;
							else a[i].sta=2;
							if(a[j].sta==0)a[j].sta=3;
							else a[j].sta=2;
							goon=true;			
							break;
						}
				}
			}
			sort(a,a+na,dcmp);
			sort(a+na,a+tot,rcmp);
			for(i=na;i<tot;i++)
			{
				if(a[i].sta==1 || a[i].sta ==2)continue;
				for(j=0;j<na;j++)
				{
					if(a[j].sta==0 || a[j].sta==1)
						if( rdcmp(a[i], a[j]) )
						{
							if(a[i].sta==0)a[i].sta=1;
							else a[i].sta=2;
							if(a[j].sta==0)a[j].sta=3;
							else a[j].sta=2;
							goon=true;							
							break;
						}
				}
			}
		}
		//for(i=0;i<tot;i++)printf("no.%d %d:%d %d:%d %d\n",i,a[i].dh,a[i].dm,a[i].rh,a[i].rm,a[i].sta);
		j=0;t=0;
		for(i=0;i<na;i++)if(a[i].sta==0 || a[i].sta==1){j++;}//printf("%d ",i);}printf("\n");
		for(i=na;i<tot;i++)if(a[i].sta==0 || a[i].sta==1){t++;}//printf("%d ",i);}printf("\n");
		printf("Case #%d: %d %d\n",l,j,t);
	}
	return 1;
}