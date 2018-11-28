#include<iostream>
#include<conio.h>
#include<vector>
#include<string>
using namespace std;
vector<string>s;
vector<string>q;
int ns,nq;
int soln[101][1001];
int cur;
int recur(int spos,int qpos)
{ if(qpos==nq)
  return 0;
  if(soln[spos][qpos]!=-1)
  return soln[spos][qpos];
  int&res=soln[spos][qpos];
  res=100000000;
  if(s[spos]!=q[qpos])
  res=min(res,recur(spos,qpos+1));
  for(int i=0;i<ns;i++)
  if(i!=spos&&s[i]!=q[qpos])
  res=min(res,1+recur(i,qpos+1));
  //if(cur==1)
  //cerr<<spos<<" "<<qpos<<" "<<res<<"\n";
  return res;
}
  
int main()
{ int ncases;
  char arr[100]="";
  cin>>ncases;
  for(int k=0;k<ncases;k++)
  { ns=0,nq=0;
    cin>>ns;
    s.clear();
    q.clear();
    cur=k;
    //cerr<<cur<<"\n";
    for(int i=0;i<101;i++)
    for(int j=0;j<1001;j++)
    soln[i][j]=-1;
    for(int i=0;i<ns;i++)
    { gets(arr);
      string tmp=arr;
      while(tmp=="")
      { gets(arr);
        tmp=arr;
      }
      s.push_back(arr);
      //cerr<<"ns:"<<arr<<"\n";
    }
    cin>>nq;  
    //cerr<<ns<<" "<<nq<<"\n";
    for(int i=0;i<nq;i++)
    { gets(arr);
      string tmp=arr;
      while(tmp=="")
      { gets(arr);
        tmp=arr;
      }
      q.push_back(arr);
      //cerr<<"nq:"<<arr<<"\n";
    }
    int mx=100000000;
    for(int i=0;i<ns&&nq>0;i++)
    if(s[i]!=q[0])  
    mx=min(mx,recur(i,1));
    if(nq==0)
    mx=0;
    cout<<"Case #"<<k+1<<": "<<mx<<"\n";//,k+1,mx);
  }

}
