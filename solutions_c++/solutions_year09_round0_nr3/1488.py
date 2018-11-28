#include <iostream>
#include <sstream>

using namespace std;

int main(){
  string pattern = "welcome to code jam";
  int N, n = pattern.length(), m;
  cin >> N >> ws;
  for(int i=0;i<N;i++){
    string text;
    getline(cin, text);
    m = text.length();
    int** table = new int*[n];
    for(int r=0;r<n;r++) {
      table[r] = new int[m];
      for(int c=0;c<m;c++){
	table[r][c] = 0;
      }
    }
    for(int r=0;r<n;r++){
      for(int c=m-1;c>=0;c--){
	if(c==m-1) table[r][c] = 0;
	else table[r][c] = table[r][c+1];
	if(text.at(c) == pattern.at(n-r-1)){
	  if(r==0) table[r][c]++;
	  else{
	    table[r][c] = (table[r][c] + table[r-1][c])%10000;
	  }
	}
      }
    }
    // pad leading zeros
    stringstream sout;
    if(table[n-1][0] > 999)sout << table[n-1][0];
    else if(table[n-1][0] > 99)sout << "0" << table[n-1][0];
    else if(table[n-1][0] > 9)sout << "00" << table[n-1][0];
    else sout << "000" << table[n-1][0];
    cout << "Case #" << i+1 << ": " << sout.str() << endl;

    for(int r=0;r<n;r++) delete[] table[r];
    delete[] table;
  }
  return 0;
}
