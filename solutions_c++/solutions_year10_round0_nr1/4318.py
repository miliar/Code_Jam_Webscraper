#include<iostream>
using namespace std;
void complement(int t[30],int p[30],int n)
{
for(int i=0;i<n;i++)
if(p[i])
{
t[i]=(t[i]==0)?1:0;
}
}

void display(int p[30],int t[30])
{
for(int i=29;i>=0;i--)
cout<<t[i];
cout<<"\n";

for(int i=29;i>=0;i--)
cout<<p[i];
cout<<"\n";

}
void setzero(int p[30],int index)
{
for(int i=index;i>=0;i--)
{
p[i]=0;
}
}

int main()
{
int n,k,test,count=0;
int t[30];
int p[30];
cin>>test;
while(test--)
{
setzero(p,29);
setzero(t,29);
count++;
cin>>n>>k;
p[n-1]=1;
//display(p,t);

for(int i=0;i<k;i++)
{
complement(t,p,n);
for(int i=n-1;i>=0;i--)
{
if(t[i]==0)
{
p[i]=1;
setzero(p,i-1);
break;
}
else
p[i]=1;


}
//cout<<"\n";
//display(p,t);



}
cout<<"Case #"<<count<<": ";
if(p[0] && t[0])
cout<<"ON";
else
cout<<"OFF";
cout<<"\n";
//display(p,t);
}
//system("pause");
}
