#include<iostream>
using namespace std;
int main()
{
int tc;
cin>>tc;
for(int j=0;j<tc;j++)
{
int c,d,n;
cin>>c;
char com[3];
if(c==1)
{
for(int i=0;i<3;i++)
{
cin>>com[i];
}
}
cin>>d;
char opp[2];
if(d==1)
{
for(int i=0;i<2;i++)
{
cin>>opp[i];
}
}
cin>>n;
char inv[n];
for(int i=0;i<n;i++)
{
cin>>inv[i];
}
char ans[n+1];
int si=0;
int temp1=0;
int temp2;
int in=0;
int e=0;
for(int i=0;i<n;i++)
{
ans[in]=inv[i];
ans[in+1]='@';
if(c==1 && (in-si)!=0)
{
if((ans[in]==com[0] && ans[in-1]==com[1]) || (ans[in]==com[1] && ans[in-1]==com[0]))
{
ans[in-1]=com[2];
ans[in]='@';
in=in-1;
e=1;
}
}
if(e==1)
{
e=0;
in++;
continue;
}
if(d==1)
{
int x=si;
if(ans[in]==opp[0])
{
while(1)
{
if(ans[x]=='@')
break;
if(ans[x]==opp[1])
{
si=in+1;
break;
}
x++;
}
}
else if(ans[in]==opp[1])
{
while(1)
{
if(ans[x]=='@')
break;
if(ans[x]==opp[0])
{
si=in+1;
break;
}
x++;
}
}
/*if(ans[in]==opp[0] && temp1==0)
{
temp1=1;
}
else if(ans[in]==opp[1] && temp1==0)
{
temp1=2;
}
else if(ans[in]==opp[0] && temp1==2)
{
temp1=0;
si=in+1;
}
else if(ans[in]==opp[1] && temp1==1)
{
temp1=0;
si=in+1;
}*/
}
in++;
}

int w=si;
cout<<"Case #"<<j+1<<": [";
while(ans[w]!='@')
{
if(w!=si)
cout<<", ";
cout<<ans[w];
w++;
}
cout<<"]"<<endl;
}
return 0;
}
