#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <string>
#include <cstdlib>

using namespace std;
bool could_be(string s, string * possible) {
  int i = 0;
  int size = s.size();
  bool result = true;
  while(i<size&result) {
    int j = 0;
    int size_j = possible[i].size();
    result = false;
    while(j<size_j&!result) {
      result = s[i] == possible[i][j];
      j++;
    }
    i++;
  }
  return result;
}
int count_possible(string * words,string * possible,int n) {
  int result = 0;
  for (int i =0;i<n;i++) {
    result += could_be(words[i],possible);
  }
  return result;
}
int main() {
  ifstream input("input.txt");
  ofstream output("output.txt");
  int length;
  int number_of_test_words;
  int number_of_test_cases;
  string b;
  getline(input,b,' ');
  length = atoi(b.c_str());
  
  getline(input,b,' ');
  number_of_test_words = atoi(b.c_str());
  
  getline(input,b,'\n');
  number_of_test_cases = atoi(b.c_str());
  
  string  words[number_of_test_words];
  
  for(int i =0;i< number_of_test_words;i++){
    getline(input,words[i],'\n');
  }
  char c;
  string possible[length];
  for(int case_number = 1; case_number<=number_of_test_cases;case_number++){
    for(int i =0;i<length;i++) {
      c= input.get();
      if(c=='(') {
	getline(input,possible[i],')');
      }
      else {
	b = "a";
	b[0] = c;
	possible[i] = b;
      }
    }
    while(input.peek()=='\n' || input.peek()==' ') input.get();
    int result = count_possible(words,possible,number_of_test_words);
    /*
    cout << "n. words: " << number_of_test_words << endl;
    for (int j = 0;j<number_of_test_words;j++){
      cout << words[j] << ", ";
    }
    cout << "length: " << length << endl;
    for (int j = 0;j<length;j++){
      cout << possible[j] << ", ";
    }
    cout << endl;
    */
    output << "Case #" << case_number << ": " << result << endl;
  }
  
  return 0;
}