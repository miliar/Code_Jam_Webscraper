/*G++ compiler is used*/
/* before giving input, ':' was replaced by ' '*/


#include<iostream>
#include<algorithm>
using namespace std;
struct train                           //assumed 0 by default
{
int ah,am,dh,dm;
int st;   //0 for a, 1 for b
int ready;      //0 for yes 1 for no
}a[200];
bool comp(const train &leftnode,const train &rightnode)
{
 if(leftnode.dh!=rightnode.dh) return leftnode.dh<rightnode.dh;
 if(leftnode.dm!=rightnode.dm) return leftnode.dm<rightnode.dm;
 if(leftnode.ah!=rightnode.ah) return leftnode.ah<rightnode.ah;
 if(leftnode.am!=rightnode.am) return leftnode.am<rightnode.am;
 return false;
}
main()
{
int n,t,na,nb,i,j,k,l,ctr[2]={0,0},flag;
cin>>n;
for(l=0;l<n;l++)
{
cin>>t>>na>>nb;
ctr[0]=0;
ctr[1]=0;
for(i=0;i<(na+nb);i++)
{cin>>a[i].dh>>a[i].dm>>a[i].ah>>a[i].am;
a[i].am+=t;
a[i].st=a[i].ready=0;
if(a[i].am>=60)
{
a[i].am-=60;
a[i].ah+=1;
}
}
for(i=na;i<(na+nb);i++)
a[i].st=1;
sort(a,a+(na+nb),comp);

for(i=0;i<(na+nb);i++)
{
k=a[i].st;
flag=0;
for(j=0;j<i;j++)
{
if(a[j].ready==0)
if(a[j].st!=k)
if((a[j].ah<a[i].dh)||((a[j].ah==a[i].dh)&&(a[j].am<=a[i].dm)))
{
flag=1;
a[j].ready=1;
j=i;
}
}
if(flag==0)
ctr[k]++;
}
cout<<"Case #"<<l+1<<": "<<ctr[0]<<" "<<ctr[1]<<endl;
}
}
