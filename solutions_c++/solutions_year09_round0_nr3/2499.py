#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <string>
#include <cstdlib>


using namespace std;

string welcome = "welcome to code jam";

struct infoChar {
  int pos_in_welcome;
  int pos_in_string;
  bool found;
};

infoChar find_next(string &s, int from, infoChar c) {
int size = s.size();
infoChar result;
result.found = false;
int i = from; 
bool found =false;
while(i < size && !found){
  if(s[i]==welcome[c.pos_in_welcome+1]) {
    found = true;
    result.pos_in_string = i;
    result.pos_in_welcome = c.pos_in_welcome+1;
    result.found = true;
  }
  i++;
}
return result;

}

int count_welcomes (string &s){
vector<infoChar> pending;
  bool found = false;
  int size_welcome = welcome.size();
  int size_s = s.size();
  int i = 0;
  infoChar first;
  int welcomes_counted = 0;
  while(i<size_s ) {
    if (s[i]==welcome[0]) {
      first.pos_in_welcome = 0;
      first.pos_in_string = i;
      first.found = true;
      pending.push_back(first);
      found = true;
    }
    i++;
  }
  if(!found) return 0;
  while(pending.size()!=0) {
    
    infoChar temp = pending.back();
    
    pending.pop_back();
    infoChar res;
    res.found = true;
    if(temp.pos_in_welcome==welcome.size()-1) {
      res.found = false;
      ++welcomes_counted;
      if(welcomes_counted>=10000) welcomes_counted-=10000;
    }
    while(res.found==true ) {
      res = find_next(s,temp.pos_in_string,temp);
      temp.pos_in_string = res.pos_in_string+1;
	if(res.found) pending.push_back(res);
    }
   
  }
  return welcomes_counted;
}
int main() {
  ifstream input("input.txt");
  int test_cases_number;
  string s;
  getline(input,s,'\n');
  test_cases_number = atoi(s.c_str());
  ofstream output("output.txt");
  string result_string;
  string num_string;
  for(int i = 1; i <= test_cases_number; i++) {
    getline(input,s,'\n');
    cout << s << endl;
    cout << i << endl;
    int result =count_welcomes(s);
    cout << result << endl;
    stringstream num;
    num << result;
    result_string = "0000";
    num_string = num.str();
    for(int j = 1; j <=num_string.size();j++) {
      result_string[result_string.size()-j] = num_string[num_string.size()-j];
    }
    cout << result_string<< endl;
    
    output << "Case #" << i<<": "<< result_string << endl;
  }
  return 0;
}