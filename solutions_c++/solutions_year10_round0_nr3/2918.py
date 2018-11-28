#include <stdio.h>
#include <math.h>

int main()
{
	int dt,i,j,l;
	int r,k,n;
	int mmoney,ssite;
	int tot;
	//int gi[2010];

	//freopen("test.in","r",stdin);
	//freopen("test.out","w",stdout);
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.out","w",stdout);
	//freopen(".in","r",stdin);
	//freopen(".out","w",stdout);	
	
	scanf("%d",&dt);
	
	for(i=1;i<=dt;++i)
	{
		scanf("%d %d %d",&r,&k,&n);
		int gi[n];
		tot=0;
		for(l=0;l<n;++l)
		{
            scanf("%d",&gi[l]);
            tot=tot+gi[l];
        }
		if (k>=tot)
		{
            mmoney=tot * r;       
        }
        else
        {
		//printf("r=%d k=%d n=%d\n",r,k,n);
		//printf("gi[0]=%d gi[1]=%d gi[2]=%d\n",gi[0],gi[1],gi[2]);
		mmoney=0;
		ssite=0;
		j=0;
		for(l=1;l<=r;++l)
		{
            j=j-1;
            do
            {
                  j=(j+1) % n;
                  ssite=ssite+gi[j];
                  //printf("r=%d j=%d gi[j]=%d ssite=%d\n",l,j,gi[j],ssite);
            }while(k>=ssite);
            mmoney=mmoney+ssite-gi[j];
            ssite=0;
            //printf(" big ! ssite=%d gi[j]=%d mmoney=%d\n",ssite,gi[j],mmoney);
        }
        }
        printf("Case #%d: %d\n",i,mmoney);
	}
}
