#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
using namespace std;

string phrase = "welcome to code jam";
int letters = phrase.size();
int sum;
char* word;
int len, ind;

int main(int argc, char** argv) {
  int** count;
  ifstream input;
  ofstream output;
  input.open(argv[1]);
  output.open(argv[2]);
  int T;
  input >> T;
  string in;
  getline(input, in);
  string::size_type pos;
  for(int k = 1; k <= T; k++) {
    output << "Case #" << k << ": ";
    getline(input, in);
    //kick out characters that aren't relevant
    string::size_type w = in.find("w");
    if(w == string::npos) {
      output << "0000" << endl;
      continue;
    } else {
      in = in.substr(w, string::npos);
    }
    string::size_type m = in.find_last_of('m');
    if(m == string::npos) {
      output << "0000" << endl;
      continue;
    } else {
      in = in.substr(0, m + 1);
    }
    len = 0;
    for(int i = 0; i < in.size(); i++) {
      if(in[i] == 'w' || in[i] == 'e' || in[i] == 'l' || in[i] == 'c' || in[i] == 'o' || in[i] == 'm'
	 || in[i] == ' ' || in[i] == 't' || in[i] == 'd' || in[i] == 'j' || in[i] == 'a') {
	len ++;
      }
    }
    word = new char[len];
    ind = 0;
    for(int i = 0; i < in.size(); i++) {
      if(in[i] == 'w' || in[i] == 'e' || in[i] == 'l' || in[i] == 'c' || in[i] == 'o' || in[i] == 'm'
	 || in[i] == ' ' || in[i] == 't' || in[i] == 'd' || in[i] == 'j' || in[i] == 'a') {
	word[ind++] = in[i];
      }
    }
    count = new int*[len];
    for(int i = 0; i < len; i++) {
      count[i] = new int[letters];
      for(int j = 0; j < letters; j++) {
	count[i][j] = 0;
      }
    }
    for(int i = len - 1; i >= 0; i--) {
      cout << word[i] << " ";
      pos = -1;
      while((pos = phrase.find(word[i], pos + 1)) != string::npos) {
	cout << pos << " ";
	if(pos == phrase.size() - 1) {
	  cout << "base" << " ";
	  count[i][pos] = 1;
	  continue;
	}
	for(int j = i + 1; j < len; j++) {
	  count[i][pos] += count[j][pos + 1];
	}
	cout << "<" << count[i][pos] << ">";
	count[i][pos] %= 10000;
      }
      cout << endl;
    }
    sum = 0;
    for(int i = 0; i < len; i++) {
      sum += count[i][0];
      delete[] count[i];
    }
    delete[] count;
    delete[] word;
    output << setfill('0') << setw(4) << sum << endl;
  }
}
