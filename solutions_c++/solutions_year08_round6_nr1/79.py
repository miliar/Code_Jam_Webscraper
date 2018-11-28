#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;

const int imax=10000000;

typedef pair<int,int> pii;

bool inrange(int x,int mn,int mx) { return x>=mn&&x<=mx; }
int main()
{
  int ci,cn,r=1;
  cin>>cn;
  for(ci=1;ci<=cn;++ci)
  {
    string rsp;
    vector<pii> notbird;
    int shown,notsh,i,h,w;
    int hmin,hmax,wmin,wmax;
    hmin=wmin=imax;
    hmax=wmax=-1;

    cin>>shown;
    for(i=0;i<shown;++i)
    { cin>>h>>w>>rsp;
      bool b=true;
      if(rsp[0]=='N')
      { cin>>rsp;
        notbird.push_back(pii(h,w));
      }else
      { if(h<hmin) hmin=h;
        if(h>hmax) hmax=h;
        if(w<wmin) wmin=w;
        if(w>wmax) wmax=w;
      }
    }
    int top,left,right,bottom;
    top=right=imax;
    left=bottom=-1;
    for(i=0;i<notbird.size();++i)
    { if(inrange(notbird[i].first,hmin,hmax)) // with == as true
      { if(notbird[i].second>wmax&&notbird[i].second<top) top=notbird[i].second;
        if(notbird[i].second<wmin&&notbird[i].second>bottom) 
          bottom=notbird[i].second;
      }
      if(inrange(notbird[i].second,wmin,wmax))
      { if(notbird[i].first>hmax&& notbird[i].first<right) 
          right=notbird[i].first;
        if(notbird[i].first<hmin&&notbird[i].first>left) left=notbird[i].first;
      }
    }

//    cout<<hmin<<" to "<<hmax<<'\t'<<wmin<<" to "<<wmax<<endl;
//    cout<<left<<" to "<<right<<'\t'<<bottom<<" to "<<top<<endl;

    cout<<"Case #"<<ci<<":"<<endl;
    // Improvises
    cin>>notsh;
    for(i=0;i<notsh;++i)
    { cin>>h>>w;
      if(inrange(h,hmin,hmax)&&inrange(w,wmin,wmax))
        cout<<"BIRD"<<endl;
      else if(inrange(h,left+1,right-1)&&inrange(w,bottom+1,top-1))
        cout<<"UNKNOWN"<<endl;
      else cout<<"NOT BIRD"<<endl;
        
    }

  }
}
