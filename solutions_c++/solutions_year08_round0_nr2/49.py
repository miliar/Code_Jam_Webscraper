#include<iostream>
#include<algorithm>
using namespace std;

int adept[100],barrv[100],bdept[100],aarrv[100];
int an,bn,turn;

int main()
{
  int ci,cn,i,j;
  cin>>cn;
  for(ci=1;ci<=cn;++ci)
  { cin>>turn>>an>>bn;
    int sh,sm,eh,em;
    char dum;
    for(i=0;i<an;++i)
    { cin>>sh>>dum>>sm>>eh>>dum>>em;
      adept[i]=sh*60+sm;
      barrv[i]=eh*60+em;
    }
    for(i=0;i<bn;++i)
    { cin>>sh>>dum>>sm>>eh>>dum>>em;
      bdept[i]=sh*60+sm;
      aarrv[i]=eh*60+em;
    }
    sort(adept,adept+an); sort(barrv,barrv+an);
    sort(bdept,bdept+bn); sort(aarrv,aarrv+bn);

    int aneed=an,bneed=bn;
    for(i=j=0;i<bn&&j<an;++i)
    { for(;j<an && adept[j]<aarrv[i]+turn;++j);
      if(j<an) --aneed,++j;
    }
    for(i=j=0;i<an&&j<bn;++i)
    { for(;j<bn && bdept[j]<barrv[i]+turn;++j);
      if(j<bn) --bneed,++j;
    }
    cout<<"Case #"<<ci<<": "<<aneed<<' '<<bneed<<endl;
  }
}
