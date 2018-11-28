#include <stdio.h>
#include "stdafx.h"
#include <ctype.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#include <conio.h>
int main(int argc, char *argv[])
{
    freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t = 1,testcase,n,po,pb,i,pto,ptb,mt,mintime,pos;
	bool o = false,b = false;
	char r,ch;
	scanf("%d", &testcase);
	while(t<=testcase){
	    po = 1; pb = 1; ptb = 0; pto = 0;mintime = 0;
	    scanf("%d",&n);
		for(i = 1; i<=n; ++i){
		    scanf("%c%c%c%d",&ch,&r,&ch,&pos);
			//printf("%c%c%c%d\n",ch,r,ch,pos);
		    if(r == 'O'){
				if(o == false){
				    if(ptb<=abs(po - pos)){
						 mintime = mintime + abs(po - pos)-ptb+1;pto = pto + abs(po - pos)-ptb+1;
					}
					else {
					   mintime = mintime+1;pto = pto+1;
					}
				    ptb = 0;
					o = true; b = false;
				}
				else {
				  mintime = mintime + abs(po - pos) + 1; pto = pto + abs(po - pos) + 1;
				}
				po = pos;
			}
			else if(r == 'B'){
				if(b == false){
				   if(pto<=abs(pb - pos)){
				   mintime = mintime + abs(pb - pos)-pto+1;ptb = ptb + abs(pb - pos)-pto+1;
				   }
				   else{
					   mintime = mintime+1;ptb = ptb+1;
				   }
				   
				   pto = 0; b = true; o = false;
				}
				else {
				    mintime = mintime + abs(pb - pos) + 1; ptb = ptb + abs(pb - pos) + 1;
				}
				pb = pos;
			}
		}
		printf("Case #%d: %d\n",t,mintime);
	  ++t;	    
	}
	getch();
	return 0;
}