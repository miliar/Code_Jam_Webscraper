#include <cmath>
#include <cstdio>
#include <string>
#include <vector>
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

int main() 
{
    ofstream fout ("test.out");
   // ifstream fin ("test.in");
    int t;
    cin >> t;
    for(int i=1;i<=t;i++)
    {
      int N,S,p;
      cin>>N>>S>>p;
      vector<int> v;
      int x=N;
      while(x--)
      {
	int a;
	cin>>a;
	v.push_back(a);
      }
      int dump=0;
      int count=0;
      for(int j=0;j<v.size();j++)
      {
	//double ans=v[j];
	if(v[j]>=p*3-2)count++;
	//int m=(int)ceil(ans/3);
	//if(m>=p)count++;
	else if(v[j]!=0&&v[j]>=p*3-4)dump++;
/*	if(v[j]%3!=1)
	{
	  if(m==p-1)dump++;
	}*/
      }
      count+=min(dump,S);
      if(count>N)cout<<"bazzinga"<<endl;
      fout<<"Case #"<<i<<": "<<count<<endl;
    }
  //  fout << a+b << endl;
    return 0;
}