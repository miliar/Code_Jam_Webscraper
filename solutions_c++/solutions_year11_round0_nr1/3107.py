#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int main()
{
  FILE *f;
  int ca,prei,prej,nowi,nowj,n,x,total=0,i;
  int sumo,sumb,ans;
  char s[3];
  scanf("%d",&ca);
  f=fopen("A_small.out","w");
  while(ca--)
  {
	prei=prej=nowi=nowj=1;
	sumo=sumb=0;
	ans=0;
	total++;
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
	  scanf("%s%d",s,&x);
	  if(s[0]=='O') 
	  {
	    nowi=x;
		if(abs(nowi-prei)+1<=sumo)
		{
		  ans+=1;
		  sumb+=1;
		  prei=nowi;
		}
		else 
		{
		  ans+=abs(nowi-prei)+1-sumo;
		  sumb+=abs(nowi-prei)+1-sumo;
		  prei=nowi;
		}
		sumo=0;
	  }
	  else
	  {
		nowj=x;
		if(abs(nowj-prej)+1<=sumb)
		{
		  ans+=1;
		  sumo+=1;
		  prej=nowj;
		  
		}
		else 
		{
		  ans+=abs(nowj-prej)+1-sumb;
		  sumo+=abs(nowj-prej)+1-sumb;
		  prej=nowj;
		  
		}
		sumb=0;
	  }
	  //printf("prei=%d   nowi=%d  prej=%d  nowj=%d  sumo=%d  sumb=%d  ans=%d\n",prei,nowi,prej,nowj,sumo,sumb,ans);
	}
	fprintf(f,"Case #%d: %d\n",total,ans);
  }
  system("pause");
  return 0;
}


	  