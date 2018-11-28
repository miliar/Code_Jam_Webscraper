#include <string>
#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;

int main() {
   int t,T,i;
   cin>>T;
   string s;
   for (t=1; t<=T;t++) {
      cin>>s;
      vector<int> v(256,-1);
      int b=0;
      for (i=0; i<s.length(); i++) {
	 if (v[s[i]]<0) {
	    b++;
	    if (b==1) v[s[i]]=1;
	    else if (b==2) v[s[i]]=0;
	    else v[s[i]]=b-1;
	 }
      }
      if (b<2) b=2;
      long long f=0;
      for (i=0; i<s.length(); i++) {
	 f=f*b+v[s[i]];
      }
      printf("Case #%d: %lld\n",t,f);
   }
   return 0;
}
