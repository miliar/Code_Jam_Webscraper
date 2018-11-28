#include<stdio.h>
#include<stdlib.h>
int main()
{
	
	freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

	int t,n,i,j;

    int x[1000][2];
	int jj;
	int y=0;
scanf("%d",&t);

for(i=0;i<t;i++){

    scanf("%d",&n);
    for(j=0;j<n;j++)
	{
     scanf("%d%d",&x[j][0],&x[j][1]);
	 for(jj=0;jj<j;jj++)
	 {
		 if(((x[j][0]>x[jj][0])&&(x[j][1]<x[jj][1]))||((x[j][0]<x[jj][0])&&(x[j][1]>x[jj][1])))
			 y++;	 
	 }
	 

	}
    printf("Case #%d: %d\n",i+1,y);
	y=0;
}

return 0;
}
