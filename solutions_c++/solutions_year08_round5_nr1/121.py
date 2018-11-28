#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;

typedef long long lli;
// -ve coords possible!
vector<int> x,y;
int n;
lli abs(lli x) { return x<0?-x:x; }
lli polyarea()
{ lli rv=0;
  for(int i=1;i<n;++i)
    rv+=1LL*x[i-1]*y[i]-1LL*x[i]*y[i-1];
  return ::abs(rv)/2;
}

lli outarea()
{
  int minx,maxx,miny,maxy,i,j;
  minx=*min_element(x.begin(),x.end());
  miny=*min_element(y.begin(),y.end());
  maxx=*max_element(x.begin(),x.end());
  maxy=*max_element(y.begin(),y.end());
  if(minx==maxx||miny==maxy) return 0;
  vector<int> sst(maxx-minx,5000),sen(maxx-minx,-5000);
  for(i=1;i<n;++i) if(x[i]!=x[i-1])
  { int tx=min(x[i],x[i-1])-minx;
    if(sst[tx]>y[i]) sst[tx]=y[i];
    if(sen[tx]<y[i]) sen[tx]=y[i];
  }
  for(i=0;i<sst.size();++i) 
  { if(sst[i]==miny) break;
    if(i>0&&sst[i]>sst[i-1]) sst[i]=sst[i-1];
  }
  for(j=sst.size()-1;j>=0;--j)
  { if(sst[j]==miny) break;
    if(j<sst.size()-1&&sst[j]>sst[j+1]) sst[j]=sst[j+1];
  }
//  for(i=0;i<sst.size();++i) cout<<sen[i]<<' '<<sst[i]<<endl;
  while(i<=j) sst[i++]=miny;
  for(i=0;i<sen.size();++i)
  { if(sen[i]==maxy) break;
    if(i>0&&sen[i]<sen[i-1]) sen[i]=sen[i-1];
  }
  for(j=sen.size()-1;j>=0;--j)
  { if(sen[j]==maxy) break;
    if(j<sen.size()-1&&sen[j]<sen[j+1]) sen[j]=sen[j+1];
  }
  while(i<=j) sen[i++]=maxy;
  lli rv=0;

  for(i=0;i<sst.size();++i) rv+=sen[i]-sst[i];
  return rv;
}

const int dx[]={0,-1,0,1};
const int dy[]={-1,0,1,0};
int main()
{
  int ci,cn;
  cin>>cn;
  for(ci=1;ci<=cn;++ci)
  { int l,i,t,j;
    string s;
    cin>>l;
    x.clear(); y.clear();
    x.push_back(0); y.push_back(0);
    int d=0;
    for(i=0;i<l;++i)
    { cin>>s>>t;
      for(j=0;j<t*s.size();++j)
      { char ch=s[j%s.size()];
        if(ch=='F')
        { x.push_back(x.back()+dx[d]);
          y.push_back(y.back()+dy[d]);
        }else if(ch=='L') d=(d+1)%4;
        else if(ch=='R') d=(d+3)%4;
      }
    }
    n=x.size();
//    cout<<"Case #"<<ci<<": "<<outarea()<<' '<<polyarea()<<endl;
    cout<<"Case #"<<ci<<": "<<outarea()-polyarea()<<endl;
  }
}

