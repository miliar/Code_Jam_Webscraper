#include <iostream>
#include <sstream>

using namespace std;

int N;

long count_subsets(string phrase, string str) {
  int l = str.size();
  long* prev_prefix = new long[l];
  long* next_prefix = new long[l];
  
  
  unsigned p = 0; // iterate over phrase
  long sum;

  // Initialize first char
  sum = 0;
  for (int i=0; i<l; i++) {
    if (str[i] == phrase[p]) sum++;
    next_prefix[i] = sum;
  }
 
  // Iterate remaining chars of phrase
  for (p++; p<phrase.size(); p++) {
    swap(prev_prefix, next_prefix);
    sum = 0;
    next_prefix[0] = 0;
    for (int i=1; i<l; i++) {
      if (str[i] == phrase[p]) sum+= prev_prefix[i-1];
      assert(sum < 1000000000);
      next_prefix[i] = sum;
    }
  }

  // Return result
  long result = next_prefix[l-1];
  delete next_prefix;
  delete prev_prefix;
  return result;
}

int main()
{
  string wtcj = "welcome to code jam";
  string str;
  getline(cin,str);
  stringstream ss(str);
  ss >> N;
  
  for (int i = 0; i < N; i ++) {
    getline(cin,str);
    long val = count_subsets(wtcj, str);
    string val4 = "";
    for (int j=0; j<4; j++) {
      char d = '0' + val % 10;
      val4 = d + val4;
      val = val / 10;
    }
    cout << "Case #" << i+1 << ": " << val4 << endl;
  }
}
