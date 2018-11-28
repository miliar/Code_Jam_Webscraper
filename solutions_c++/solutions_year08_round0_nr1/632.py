#include <iostream>
#include <vector>
#include <map>

#define FOR(i,a,b) for(int i=(a); i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define itype(c) __typeof((c).begin())
#define FORE(c,i) for(itype(c) i=(c).begin();i!=(c).end();++i)
#define PB push_back

using namespace std;

int main()
{
  string line;
  int T;
  cin>>T;
  REP(c,T)
  {
    int hit=0;
    int ans=0;
    int pass=1;
    map<string,int> ms;
    string t;
    int S,Q;
    cin>>S;
    getline(cin,t);
    REP(i,S) 
    {
      getline(cin,t);
      ms[t]=0;
    }

    cin>>Q;
    getline(cin,t);
    if(S==2)
    {
      string cur;
      REP(i,Q)
      {
	getline(cin,t);
	if(i==0)
	  cur=t;
	else
	{
	  if(t!=cur)
	  {
	    cur=t;
	    ans++;
	  }
	}
      }
    }
    else
    {
      REP(i,Q)
      {
	getline(cin,t);
	if(ms[t]!=pass) 
	{
	  ms[t]=pass;
	  hit++;
	}
	if(hit==S)
	{
	  ans++;
	  hit=1;
	  pass++;
	  ms[t]++;
	}
      }
    }

    printf("Case #%d: %d\n",c+1,ans);

    //    FORE(vs,i) cout<<*i<<endl;
    //    FORE(vq,i) cout<<*i<<endl;
  }
}
