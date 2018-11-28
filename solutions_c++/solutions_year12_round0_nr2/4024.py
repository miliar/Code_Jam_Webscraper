#include<iostream>

using namespace std;
int main()
{
int T;
cin>>T;
int n,s,p,a[100];
for(int tt=0;tt<T;tt++)
{
int tempcount=0,t1,t2;
cin>>n>>s>>p;
for(int i=0;i<n;i++)
cin>>a[i];

for(int i=0;i<n;i++)
{
if(a[i]%3==0)
{
t1=a[i]/3;
if(t1>=p)
{
tempcount++;
}
else
{
if(t1!=0)
t1++;

if(t1==p && s>0)
{
tempcount++;
s--;
}
}

}
else if(a[i]%3==1)
{
	
t1=a[i]/3;
t2=t1;
t1++;
if(t2>=p)
{
tempcount++;
}
else if(t1>=p)
{
tempcount++;
}
}
else if(a[i]%3==2)
{
t1=a[i]/3;
t1++;
if(t1>=p)
tempcount++;
else if(((t1+1)>=p)&&(s>0))
{
tempcount++;
s--;
}

}

}





cout<<"Case #";
	cout<<tt+1<<": ";
	cout<<tempcount;
	cout<<endl;
	
}
return 0;
}