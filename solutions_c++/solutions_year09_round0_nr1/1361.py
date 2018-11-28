#include<iostream>
#include<ext/hash_set>
#include<string>
#include<vector>
// #include "../lib/basic.cc"
// #include "../lib/strutil.cc"
// #include "../lib/flag_reader.h"

namespace __gnu_cxx
{
        template<> struct hash< std::string >
        {
                size_t operator()( const std::string& x ) const
                {
                        return hash< const char* >()( x.c_str() );
                }
        };
}

using __gnu_cxx::hash_set;
using namespace std;

hash_set<string> dict;

void appendChar(const vector<string>& cases,
		char app,
		vector<string>& bkup) {
  string temp("");
  if (cases.empty()) {
    temp.push_back(app);
    if (dict.count(temp) > 0) {
      bkup.push_back(temp);
    }
    return;
  }
  for (int i = 0; i < cases.size(); i++) {
    temp = cases[i];
    temp.push_back(app);
    if (dict.count(temp) > 0) {
      bkup.push_back(temp);
    }
  }
}

int main(int argc, char * argv[])
{
  int L=0, D=0 , N=0;
  cin >>  L >> D >> N;
  //    cout << L << ":" << D << ":" << N << endl;
  for (int i = 0; i < D; i++) {
    string temp;
    cin >> temp;
    //    dict.insert(temp);
    for (int m = 0; m < temp.length(); m++) {
      dict.insert(temp.substr(0,m+1));
      //      cout << "imsert " << temp.substr(0,m+1) << endl;
    }
    //        cout << temp << endl;
  }

  for (int j = 0; j < N; j++) {
    string temp;
    cin >> temp;
    //    cout << temp << endl;
    vector<string> cases;
    vector<string> bkup_cases;
    bool open_par = false;
    for (int k = 0; k < temp.length(); k++) {
      if (temp[k] == '(') {
	open_par = true;
      } else if (temp[k] == ')') {
	open_par = false;
	cases.swap(bkup_cases);
	bkup_cases.clear();
	if (cases.empty())
	  break;
      } else {
	appendChar(cases, temp[k], bkup_cases);
	if (!open_par) {
	  cases.swap(bkup_cases);
	  bkup_cases.clear();	  
	  if (cases.empty())
	    break;
	}
      }
    }
    long long int count = 0;
    for (int l = 0; l < cases.size(); l++) {
      //      cout << cases[l] << endl;
      if (dict.count(cases[l]) > 0) {
	count++;
      }
    }
    cout << "Case #" << j+1 << ": " << count << endl;
  }
}
