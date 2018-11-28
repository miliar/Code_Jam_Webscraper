#include <cmath>
#include <cstdio>
#include <string>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
typedef long long ll; 
#define FOR(i,n) for (i = 0; i < n; i++)
#define SZ(x) ((int)x.size())
#define PB push_back
#include <fstream>

using namespace std;
int numdigits(int x)
{
  int ans=0;
  while(x!=0)
  {
    x=x/10;
    ans++;
  }
  return ans;
}
int main() 
{
    ofstream fout ("ans.out");
 //   ifstream fin ("test.in");
   // int a, b;
   // fin >> a >> b;
   // fout << a+b << endl;
    int t;
    cin>>t;
    for(int ca=1;ca<=t;ca++)
    {
      int count=0;
      int a,b;
      cin>>a>>b;
      for(int i=a;i<=b;i++)
      {
	int digits=numdigits(i);
	int mul=10;
	set<int> s;
	for(int j=1;j<digits;j++)
	{
	  int n=i/mul+(i%mul)*pow(10,digits-j);
	 // cout<<
	  if(n>i&&n<=b)
	  {
	    s.insert(n);
	   // fout<<i<<" "<<n<<endl;
	   // count++;
	  }
	  mul*=10;
	}
	count+=s.size();
      }
      fout<<"Case #"<<ca<<": "<<count<<endl;
    }
    return 0;
}