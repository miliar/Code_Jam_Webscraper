#include<iostream>
#include<new>
#include<cstdio>
using namespace std;
class in
{
    public:
    char col;
    int step;
};
class rob
{
    public:
    int present,time_left;
};
int main()
{

    int t,but,tot_time=0,diff;
    in *inp;
    rob o,b;

    cin>>t;
    for(int k=1;k<=t;k++)
    {
     cin>>but;
     inp=new in[but];
     o.present=b.present=1;
    o.time_left=b.time_left=0;
    tot_time=0;
    for(int i=0;i<but;i++)//input
    {
        cin>>inp[i].col;
        cin>>inp[i].step;
    }
for(int j=0;j<but;j++)
{  if(inp[j].col=='O')
{
     diff=inp[j].step-o.present;
     if(diff<0)
     diff=0-diff;
     diff=diff-o.time_left;
     if(diff<0)
     diff=0;
     tot_time=tot_time+diff+1;
     o.present=inp[j].step;
     o.time_left=0;
     if(b.time_left>0)
     b.time_left=b.time_left+diff+1;
     else
     b.time_left=diff+1;
}
else
{
diff=inp[j].step-b.present;
     if(diff<0)
     diff=0-diff;
     diff=diff-b.time_left;
     if(diff<0)
     diff=0;
     tot_time=tot_time+diff+1;
     b.present=inp[j].step;
     b.time_left=0;
     if(o.time_left>0)
     o.time_left=o.time_left+diff+1;
     else
     o.time_left=diff+1;
}
}
delete inp;
cout<<"Case #"<<k<<": "<<tot_time<<"\n";
    }
return 0;
}
