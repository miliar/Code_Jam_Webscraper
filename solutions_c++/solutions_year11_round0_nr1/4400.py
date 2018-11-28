#include<stdio.h>
using namespace std;
int diff(int x,int y)
{
if(x>y)
return(x-y);
else
return(y-x);
}
int main()
{
int test,tc;
int b_but,b_time,o_but,o_time,time,seq,seq_c;
char c;
int but;


scanf("%d",&test);
for(tc=1;tc<=test;tc++){
time=0;
b_but=1,b_time=0,o_but=1,o_time=0;


scanf("%d",&seq_c);
for(seq=1;seq<=seq_c;seq++)
{
scanf("%c",&c);
scanf("%c",&c);

scanf("%d",&but);
if(c=='O')
{
int time_req=diff(but,o_but);
int time_has=time-o_time;
if(time_req>=time_has)
time=time+(time_req-time_has)+1;
else
time=time+1;
o_but=but;
o_time=time;
}
else if(c=='B')
{
int time_req=diff(but,b_but);
int time_has=time-b_time;
if(time_req>=time_has)
time=time+(time_req-time_has)+1;
else
time=time+1;
b_but=but;
b_time=time;
}
}
printf("Case #%d: %d\n",tc,time);
}
}

