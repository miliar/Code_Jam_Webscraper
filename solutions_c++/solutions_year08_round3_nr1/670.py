#include <iostream>
#include <vector>
#include <sstream>
#include <set>

#define FORR(x,a,b) for(int x=a;x<b;++x)
#define FORE(x,a) for(typeof((a).begin()) x=(a).begin(); x!=(a).end(); ++x)
#define BE(a) (a).begin(),(a).end()

using namespace std;

typedef vector<string> VS;
typedef VS::iterator VSIt;
typedef long long LL;

typedef vector<int> VI;
typedef VI::iterator VII;
typedef set<int> SI;
typedef vector<SI> VSI;

void process(void)
{
  int p,k,l;

  cin>>p>>k>>l;
  cerr<<"key capacity="<<p<<" keys="<<k<<" letters="<<l<<endl;
  string sfqs;
  getline(cin,sfqs);
  getline(cin,sfqs);
  stringstream sour(sfqs);
  int fq;
  VI fqs;
  while(sour>>fq)
    fqs.push_back(fq);
  cerr<<"freqs= ";
  FORE(itx,fqs)  
    cerr<<(*itx)<<" ";
  cerr<<endl;

  sort(BE(fqs));
  reverse(BE(fqs));

  LL ret=0;
  int pos=0,stage=1;
  while(pos<fqs.size())
    {
      for(int t=0;t<k&&pos<fqs.size();++t)
	{
	  ret+=LL(stage)*LL(fqs[pos]);
	  ++pos;
	}
      ++stage;
    }
  cout<<ret;
}

int main()
{
  int n;
  cin>>n;
  FORR(t,0,n)
    {
      cerr<<"Begin to process "<<(t+1)<<" case"<<endl;
      cout<<"Case #"<<(t+1)<<": ";
      cerr<<"Case #"<<(t+1)<<": ";
      process();
      cout<<endl;      
    }
  
  return 0;
}
 
