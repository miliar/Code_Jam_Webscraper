#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
using namespace std;

struct Blue
{
    int no ;
	int bt ;	   
}blu[105];

struct Orange
{
    int no ;
	int bt ;	   
}ora[105] ;

int mAbs(int a, int b)
{
    if(a > b) return a-b ;
	else return b-a ;  	
}

int main()
{
 	freopen("A-large.in", "r", stdin);
 	freopen("A-large.out", "w", stdout);
 	int T, N, i, j, o, b, t, sec, po, pb, no = 1 ;
 	char ob[3] ;
 	scanf("%d", &T);
 	while(T --)
 	{
	    scanf("%d", &N);
		for(i = o = b = sec = 0; i < N; i ++)
		{
		    scanf("%s%d", ob, &t);
			if(!strcmp("O", ob)) {ora[o].no = i; ora[o ++].bt = t;}
			else {blu[b].no = i; blu[b ++].bt = t;}
        } 	
        po = pb = 1 ;
		for(i = j = 0; i < o && j < b; )
		{
            if(ora[i].no > blu[j].no)
            {
	            t = mAbs(blu[j].bt, pb) + 1;
			    sec += t;
			    pb = blu[j].bt ;
				if(t >= mAbs(ora[i].bt, po)) po = ora[i].bt ;
				else  
				{
				    if(ora[i].bt > po) po += t ;
					else po -= t ; 	  
	            }		
				j ++ ;	 
            }
            else 
            {
	            t = mAbs(ora[i].bt, po) + 1;
			    sec += t;
			    po = ora[i].bt ;
				if(t >= mAbs(blu[j].bt, pb)) pb = blu[j].bt ;
				else  
				{
				    if(blu[j].bt > pb) pb += t ;
					else pb -= t ; 	  
	            }		
				i ++ ;	 
            }
        }	
        while(i < o)
        {
		    t = mAbs(ora[i].bt, po) + 1;
			sec += t ; 
			po = ora[i].bt ;
			i ++ ;	 
        }
        while(j < b)
        {
            t = mAbs(blu[j].bt, pb) + 1;
            sec += t ;
            pb = blu[j].bt ;
		    j ++ ; 	 
        }
        printf("Case #%d: %d\n", no ++, sec);
    }
    //system("pause");
    return 0 ;
}
