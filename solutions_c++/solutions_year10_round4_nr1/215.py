#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int abs(int x) { return x<0?-x:x; }
int calcright(vector<vector<char> >& input,int n)
{
  int rv,i,j;
  for(rv=0;rv<n-1;++rv)
  {
    for(i=0;i<2*n-1;++i)
    { int mhp=input[i].size()-1+rv;
      for(j=mhp+2;j/2<input[i].size();j+=2)
      { int jj=mhp*2-j;
        if(input[i][(jj+1)/2]!=input[i][j/2]) break;
      }
      if(j/2<input[i].size()) break;
    }
    if(i==2*n-1) return rv;
  }
  return rv;
}

int calc(vector<vector<char> >& input,int n)
{
  int h1,h2,v1,v2,i,j;
  h1=calcright(input,n);
  for(i=0;i<2*n-1;++i) reverse(input[i].begin(),input[i].end());
  h2=calcright(input,n);
  vector<vector<char> > dflip=input;
  for(i=0;i<2*n-1;++i) for(j=0;j<input[i].size();++j) 
  { int r=i, c=abs(n-1-i)+j*2;
    int ni=c, nj=(r-abs(n-1-c))/2;
    dflip[ni][nj]=input[i][j];
  }
  v1=calcright(dflip,n);
  for(i=0;i<2*n-1;++i) reverse(dflip[i].begin(),dflip[i].end());
  v2=calcright(dflip,n);
  h1=min(h1,h2);
  v1=min(v1,v2);
  int nn=n+h1+v1;
  return nn*nn-n*n;
}

int main()
{
  int ci,cn;
  cin>>cn;
  for(ci=1;ci<=cn;++ci)
  { int i,j,n;
    cin>>n;
    vector<vector<char> > data(2*n-1);
    for(i=0;i<2*n-1;++i)
    { data[i].resize(n-abs(n-1-i));
      for(j=0;j<data[i].size();++j) cin>>data[i][j];
    }
    cout<<"Case #"<<ci<<": "<<calc(data,n)<<endl;
  }
}
