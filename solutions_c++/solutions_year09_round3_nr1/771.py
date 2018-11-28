#include <vector>
#include <list>
#include <algorithm>
#include <queue>
#include <stack>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <map>

#define forn(i) for(int i = 0; i< (int) n; ++i)

using namespace std;


long long int min_sec(string &) ;
void leer(vector < string > & test_case);



int main () {
 
  
  ofstream salida("output.out");
  vector < string > test_case;
  leer(test_case);
  long long int i = 1;
  bool found = false;
  int n = test_case.size();
  
  forn(k) {
    i = min_sec(test_case[k]);
    cout << k << endl;
    salida << "Case #" << k + 1<<": " << i << endl;
  }
  return 0;
}


void leer(vector< string > & test_case) {
  ifstream input("input.in");
  int n;
  input >>n;
  string s;
  getline(input,s,'\n');
  forn(i) {
    getline(input,s,'\n');
    //stringstream ss (s,stringstream::in | stringstream::out);
    //int temp;
    //vector<int> temp_v;
    //while(ss >> temp) {
    //  temp_v.push_back(temp);
    //}
    test_case.push_back(s);
  }
  
}


long long int min_sec(string & input) {
  string digits;
  int n = input.size();
  size_t t;
  forn(i){
    t = digits.find(input[i]);
    if(t==string::npos) {
      digits.push_back(input[i]);
    }
  }
  int base = digits.size();
  map<char,int> x;
  x[digits[0]] = 1;
  if(base>1) {
    x[digits[1]] = 0;
  }
  
  
  n = base;
  int j = 2;
  while(j<n) {
    x[digits[j]] = j;
    ++j;
  }
  if(base==1) {
    base++;
  }
  n = input.size();
  long long int res = 0;
  long long int unit = 1;
  forn(i) {
    res += x[input[input.size()-i-1]] * unit;
    unit = unit * base;
  }
  return res;
}




