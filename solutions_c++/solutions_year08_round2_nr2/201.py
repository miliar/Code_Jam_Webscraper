#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <cstdlib>
using namespace std;

class union_find{
public:
  union_find(int n){
    for (int i=0;i<n;i++)
      dat.push_back(i);
  }

  int find(int a){
    if (dat[a]==a) return a;
    dat[a]=find(dat[a]);
  }

  void unite(int a,int b){
    dat[find(a)]=find(b);
  }

private:
  vector<int> dat;
};

long long gcd(long long a,long long b)
{
  if (b==0) return a;
  return gcd(b,a%b);
}

void process()
{
  long long a,b,p;
  cin>>a>>b>>p;

  vector<int> primes;
  vector<bool> flg(b+1,false);

  for (int i=2;i<=b;i++){
    if (flg[i]) continue;
    primes.push_back(i);
    for (int j=i+i;j<=b;j+=i)
      flg[j]=true;
  }

  union_find uf(b+1);
  for (int i=a;i<=b;i++){
    for (int j=i+1;j<=b;j++){
      long long g=gcd(i,j);
      for (int k=0;k<primes.size()&&primes[k]<=g;k++){
	if (primes[k]>=p&&(g%primes[k])==0){
	  uf.unite(i,j);
	  break;
	}
      }
    }
  }
  
  int ans=0;
  for (int i=a;i<=b;i++)
    ans+=uf.find(i)==i;

  cout<<ans<<endl;
}

int main()
{
  string line;
  getline(cin,line);
  int cases=atoi(line.c_str());
  for (int c=1;c<=cases;c++){
    cout<<"Case #"<<c<<": ";
    process();
  }
}
