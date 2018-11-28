#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>

#define D(a) a

using namespace std;


int main ()
{
  string code = " acbedgfihkjmlonqpsrutwvyxz";
  string decode = " yehosvcdxiulgkbzrntjwfpamq";

  string work;
  string Tstring;
  int T;
  getline (cin,Tstring);
  T = atoi(Tstring.c_str());
  for(int i=1;i<=T;i++) {
    getline (cin,work);
    for (int j=0;j<=work.length();j++) {
      for (int k=0;k<27;k++) {
	if ( work[j] == code[k] ) {
	  work[j] = decode[k];
	  break;
	}
      }
      continue;
    }
    cout << "Case #" << i << ": " << work << endl;
  }

  return 0;
}

