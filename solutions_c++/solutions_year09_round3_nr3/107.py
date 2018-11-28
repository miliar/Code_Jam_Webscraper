#include<iostream>
#include<vector>
#include<string>
using namespace std;
int rel[1000];
int Q;
int P;
int ind[20000];
int pmap[2000];
int len;
int soln[310][310];
int recur(int p1,int p2)
{ //cout<<p1<<" "<<p2<<" "<<pmap[p1]<<" "<<pmap[p2]<<"\n";
  if(p2-p1<1)
  return 0;
  if(soln[p1][p2]!=-1)
  return soln[p1][p2];
  int&res=soln[p1][p2];
  res=P*Q;
  int in=0;
  for(int i=0;i<Q;i++)
  if(rel[i]>=pmap[p1]&&rel[i]<=pmap[p2])
  { res=min(res,pmap[p2]-pmap[p1]+(rel[i]>0?recur(p1,ind[rel[i]-1]):0)+(rel[i]+1<P?recur(ind[rel[i]+1],p2):0));
    in=1;
  }
  if(in==0)
  res=0;
  //cout<<pmap[p1]<<" "<<pmap[p2]<<" "<<res<<"\n";
  return res;
}
int main()
{ int T;
  cin>>T;
  for(int t=0;t<T;t++)
  { 
    cin>>P>>Q;
    int len=0;
    for(int i=0;i<310;i++)
    for(int j=0;j<310;j++)
    soln[i][j]=-1;
    for(int i=0;i<20000;i++)
    ind[i]=-1;
    pmap[0]=0;
    ind[0]=0;
    len++;
    for(int i=0;i<Q;i++)
    { cin>>rel[i];
      rel[i]--;
    }
    sort(rel,rel+Q);
    for(int i=0;i<Q;i++)
    { if(rel[i]>0&&ind[rel[i]-1]==-1)
      { pmap[len]=rel[i]-1;
        ind[rel[i]-1]=len++;
      }  
      if(ind[rel[i]]==-1)
      { pmap[len]=rel[i];
        ind[rel[i]]=len++;
      }
      if(rel[i]<P-1&&ind[rel[i]+1]==-1)
      { pmap[len]=rel[i]+1;
        ind[rel[i]+1]=len++;  
      }
    }
    if(ind[P-1]==-1)
    { pmap[len]=P-1;
      ind[P-1]=len++;
    }  
    int res=recur(ind[0],ind[P-1]);
    cout<<"Case #"<<t+1<<": "<<res<<"\n";
  }
}
