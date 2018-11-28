#include<iostream>
#include<conio.h>
using namespace std;
int main()
{
int t;
int r,k,n;
cin>>t;
int scores[51];
freopen("logfile.txt", "a+", stdout);
int ubs=0;
int pp=1;
int arr[1001];
int temp[1001];
while(pp<=t)
{
cin>>r;
cin>>k;
cin>>n;
int pt=1;
int cost=0;

for(int i=0;i<n;i++)
        cin>>arr[i];

while(pt<=r)
{
int ct=0;
int ctn=0;
int j;
for(j=0;j<n;j++)
{
ct=ct+arr[j];
ctn++;
if(ct>k)
{ ct=ct-arr[j];     
    break;
}
else
{
cost+=arr[j];
}
if(ctn==n)
          break;
}
j--;
ctn--;
for(int k=0;k<ctn;k++)
{
        temp[k]=arr[k];
}
int p;
for(p=j+1;p<n;p++)
{
 arr[p-ctn]=arr[p];
}
int jk=0;

for(int h=p-ctn;h<n;h++)
{
        
        arr[h]=temp[jk];
        jk++;
}
pt++;
//for(int p2=0;p2<n;p2++)
  //  cout<<arr[p2]<<"   ";
//cout<<endl;
}

scores[ubs]=cost;
ubs++;
pp++;
}
for(int l=0;l<ubs;l++)
       { cout<<"Case #"<<l+1<<": "<<scores[l];
        cout<<endl;}
//getch();
return 1;
}
