#include<iostream>
#include<cstring>
using namespace std;

int min(int a,int b)
{
    if(a<b)
    return a;
    else
    return b;
}
void swa(int &a,int &b)
{
     int t;
     t=a;
     a=b;
     b=t;
 }

void swapb(bool &a,bool &b)
{
     bool t;
     t=a;
     a=b;
     b=t;
 }
int check(int vel[],long long int cor[],long long int tar, float time, int n,int m)
{
   // cout<<"check";
    int swap=-1;
    int i,j,x,k,count=0;
    float y;
    bool b[50];
    int temp[51]={0};
//    long long int t[n];
  //  temp[n]=1000;
    for(i=n-1;i>=0;i--)
    {
//    temp[i]=min(temp[i+1],vel[i]);
    y=float(tar-cor[i])/vel[i];
    if(y<=time)
    b[i]=true;
    else
    b[i]=false;
    }
    for(i=n-1;b[i]&&i>=0;i--)
    {
     count++;
    }
    
     for(j=i;(j>=0)&&count<m;j--)
     {
	 
      k=j-1;
      if(b[j]==false)
      {
      while(k>=0&&b[k]==false)
      {
      k--;
      }
	  if(b[k]==true)
	  {
      for(x=k;x<j;x++)
      {
              swa(vel[x],vel[x+1]);
              swapb(b[x],b[x+1]);
              swap++;
                 
            //  cout<<"swap:"<<swap<<"\n";
      }
	  }
	  if(b[j]==true)
      count++;
     // cout<<"count"<<count<<"\n";
      }
     }
	//cout<<"\n"<<"count:"<<count<<"\n";
    if(count<m)
    return -1;
    else
    swap++;
    return swap;
}

int main()
{
    int c,n,k,t,i,j,ans;
    long long int x[50],b;
    int v[50];
    i=0;
    cin>>c;
    //cout<<"main";
    while(i<c)
    {
    cin>>n>>k>>b>>t;
    for(j=0;j<n;j++)
    cin>>x[j];
    for(j=0;j<n;j++)
    cin>>v[j];
    //cout<<"calling";
    ans=check(v,x,b,t,n,k);
    if(ans!=-1)
    cout<<"Case #"<<i+1<<": "<<ans<<"\n";
    else
    cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<"\n";
    i++;
    }
    return 0;
}
