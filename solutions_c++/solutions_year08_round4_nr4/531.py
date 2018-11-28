#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
using namespace std;

void process()
{
  int k;cin>>k;
  string s;cin>>s;

  vector<int> p(k);
  for (int i=0;i<k;i++) p[i]=i;

  int ans=s.length()+1;

  do{
    string t=s;
    for (int i=0;i<s.length();i+=k)
      for (int j=0;j<k;j++)
	t[i+j]=s[i+p[j]];

    int g=1;
    for (int i=1;i<t.length();i++)
      if (t[i-1]!=t[i])
	g++;

    ans<?=g;
  }while(next_permutation(p.begin(),p.end()));

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
