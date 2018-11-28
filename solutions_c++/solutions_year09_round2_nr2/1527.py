#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cstdlib>
#include <fstream>
#include <algorithm>

using namespace std;

#define forn(i) for(int i = 0; i< (int)n;++i)

bool count_digits(string s, vector< unsigned int> &times, vector< unsigned int> &times2,bool o) {
  int n = s.size();
  string  temp;
  int j = 0;
  bool flag = true;
  while(j<n&& flag) {
    temp = s[j];
    if(atoi(temp.c_str())>0) {
      ++times[atoi(temp.c_str())];
    }
    flag = times[atoi(temp.c_str())] <= times2[atoi(temp.c_str())]||o;
    ++j;
  }
  return flag;
}


void swap(char & a, char& b) {
  char temp = a;
  a=b;
  b=temp;
}
char& min_gt( int target, string &s, int i, int end,int j) {
  int min;
  int min_i;
  string temp;
  temp = s[i];
  bool found = atoi(temp.c_str())>target;
  
  while(!found) {
    ++i;
    temp = s[i];
    found = atoi(temp.c_str())>target;
  }
  temp = s[i];
  min = atoi(temp.c_str());
  min_i = i;
  while(i<s.size()) {
    ++i;
    temp = s[i];
    if(min>atoi(temp.c_str())&& atoi(temp.c_str()) > target) {
      min = atoi(temp.c_str());
      min_i = i;
    }
  }
  j = min_i;
  return s[min_i];
  
}

bool ordered(string &s, int start, int end) {
  bool res = true;
  string temp;
  string temp2;
  for(int i = start;i<end-1;++i) {
    temp = s[i];
    temp2 = s[i+1];
    res = res && atoi(temp.c_str()) >= atoi(temp2.c_str());
  }
  return res;
}
void sort_it(string &s,int i, int end) {
  int n = end-i;
  string temp;
  vector <int> x;
  forn(j) {
    temp = s[j+i];
    x.push_back(atoi(temp.c_str()));
  }
  sort(x.begin(),x.end());
  forn(j) {
    int input = x[j];
    std::stringstream out;
    out << input;
    temp = out.str();
    s[j+i] = temp[0];
  }
}
void generate_next(string &s) {
  string temp;
  temp = "0";
  s = temp + s;
  cout << s << endl;
  int i = s.size();
  bool flag = true;
  while(flag) {
    --i;
    flag = ordered(s,i,s.size());
    cout << flag << endl;
    cout << "i: "<< i << endl;
    if(!flag&& i>0) {
      temp = s[i];
      int j = 0;
      swap(s[i],min_gt(atoi(temp.c_str()),s,i,s.size(),j)); // atoi(temp.c_str())
      sort_it(s,i+1,s.size());
      cout << s << endl;
    }
    if(!flag&& i==0) {
      /*vector< int > x ;
      int n = s.size();
      forn(j) {
	temp = s[i];
	x.push_back(atoi(temp.c_str()));
      }
      sort(x.begin(),x.end());
      s= "";
      n = x.size();
      forn(j) {
	temp = s[i];
	s.push_back(atoi(temp.c_str()));
      }*/
      int j;
      temp = s[i];
      swap(s[i],min_gt(atoi(temp.c_str()),s,i,s.size(),j));
      
      sort_it(s,1,s.size());
      cout << "resultad: " << s << endl;
      flag = false;
    }
    
  }
  
}


int next_i(int input) {
  std::string s;
  std::stringstream out;
  out << input;
  s = out.str();
  bool found = false;
  int i = input;
  vector<unsigned int> times(10,0);
  vector<unsigned int> zero(10,0);
  count_digits(s,times,zero,true);
  vector<unsigned int> times_test = zero;
  generate_next(s);
  return atoi(s.c_str());
}


void read_input(vector<int> &v) {
  ifstream input("input.in");
  int n;
  input >> n;
  int temp;
  forn(i)  {
    input >> temp;
    v.push_back(temp);
    
  }
  
}


int main() {
  vector<int> test_case;
  read_input(test_case);
  int n = test_case.size();
  ofstream output("output.out");
  forn(i) {
    output << "Case #" << i+1 << ": " << next_i(test_case[i]) << endl;
    cout << i << endl;
  }
  return 0;
}