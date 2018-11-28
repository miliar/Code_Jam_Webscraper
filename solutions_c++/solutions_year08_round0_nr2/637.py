#include <stdio.h>
#include <algorithm>

using namespace std;

typedef struct{
  int time;	
  int type;//0==arrive A 1==arrive B 2==leave A 3==leave B
}Event;


bool cmp(Event e1,Event e2)
{
   
   return (e1.time<e2.time||(e1.time==e2.time&&e1.type<e2.type));
}


Event e[500];

int main()
{
   //freopen("B-small-attempt0.in.txt","r",stdin);
   //freopen("B-small-attempt0.out.txt","w",stdout);
     freopen("B-large.in.txt","r",stdin);
     freopen("B-large.out.txt","w",stdout);

    int n,p,na,nb,t,i,j,ra,rb,esize,ta,tb;
    int th,tm;
	scanf("%d",&n);

    for(p=0;p<n;p++)
	{
		esize=0;
        scanf("%d%d%d",&t,&na,&nb);
		for(i=0;i<na;i++)
		{
             scanf("%d:%d",&th,&tm);
			// printf("%d %d\n",th,tm);
             e[esize].time=th*60+tm;
			 e[esize].type=2;
			 esize++;

			 scanf("%d:%d",&th,&tm);
			// printf("%d %d\n",th,tm);
             e[esize].time=th*60+tm+t;
			 e[esize].type=1;
		     esize++; 
		}

	    for(i=0;i<nb;i++)
		{
             scanf("%d:%d",&th,&tm);
			// printf("%d %d\n",th,tm);
             e[esize].time=th*60+tm;
			 e[esize].type=3;
			 esize++;

			 scanf("%d:%d",&th,&tm);
			// printf("%d %d\n",th,tm);
             e[esize].time=th*60+tm+t;
			 e[esize].type=0;
		     esize++; 
		}
        sort(e,e+esize,cmp);

	//	for(i=0;i<esize;i++)
	//		printf("%d:%d %d\n",e[i].time/60,e[i].time%60,e[i].type);
        
		ra=0; rb=0;
		ta=0; tb=0;

		for(i=0;i<esize;i++)
		{
            if(e[i].type==0)
		        ta++;
			else if(e[i].type==1)
		        tb++;
		    else if(e[i].type==2)
	            ta--;    
			else if(e[i].type==3)
			    tb--;
			if(ta<ra)
				ra=ta;
			if(tb<rb)
				rb=tb;
		}
        ra=-ra;
		rb=-rb;

        printf("Case #%d: %d %d\n",p+1,ra,rb);
	}
}