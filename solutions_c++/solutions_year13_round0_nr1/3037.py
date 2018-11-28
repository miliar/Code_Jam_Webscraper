#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <vector>
#include <string>
#include <numeric>
#include <sstream>
#include <fstream>
#include <complex>
#include <cassert>
#include <iostream>
#include <algorithm>
/*
//      Code By "SAEED EZZATI"
//      g++ A.cpp -o A.o && ./A.o in.in out.out 
*/
using namespace std;

#define pb push_back
#define mp make_pair
#define min(x,y) (x<y?x:y)
#define max(x,y) (x>y?x:y)

typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef vector<unsigned int> VUI;
typedef vector<VI> VVI;
typedef vector<string> VS;
LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }

#define pi acos(-1.)
#define eps 1e-7
#define inf 1000000000
#define smallLine 100
#define largeLine 1000

//////////////////// Public Variables
int N; /// Number of Inputs
char* input_file;
char* output_file;
clock_t t;
/////////////////////////////////////////////////// Function
string function(vector<vector<char> > table);
//string function(const vector<vector<char> > &table);
///////////////////////////////////////////////////
int main(int argc, char* argv[])
{
  if(argc<3){
    cout << "\n > ERROR: 'Usage: ./alienNumbers.o input_file output_file' " << endl;
    return -1;
  }
  
  input_file=argv[1];
  output_file=argv[2];
  cout.setf(ios::fixed);
  cout.precision(0);
  t = clock();
  /// Reading Input File
  ifstream in_file;
  in_file.open(input_file);
  /// Opening Output File
  ofstream out_file;
  out_file.setf(ios::fixed);
  out_file.precision(0);
  out_file.open(output_file, fstream::app);
  if(in_file.is_open()){
    cout << "\n\n > '" << input_file << "' opened correctly!" << endl;

    int lineN = 0; /// Line Number

    vector<vector<char> > table;
    vector<char> row;
    string word;
    string line;
    while(!in_file.eof()){
      /// Reading First Line 
      if(lineN==0){
        getline(in_file, line);
        stringstream ss (line, stringstream::in | stringstream::out);
        for(int i=0; i< 1; ++i){//<<<<
          ss >> N;
        }
        cout << " > Number of Tests: " << N << endl;
        cout << " > Reading Data from: '" << input_file << "'" << endl;

      /// Reading DATA 
      }else if(lineN>0 && lineN<=N){// <<<<
        
        //cout << "\n" << lineN <<"  > IN: "; //<<<<

        /// Reading Words From Lines
        for(int i=0; i<4; i++){
          getline(in_file, line);
          stringstream ss1 (line, stringstream::in | stringstream::out);
          ss1 >> word;
          //cout << word << endl;
          for(int j=0; j<4; ++j){
            row.pb(word[j]);
          }
          table.pb(row);
          row.clear();
        }
        getline(in_file, line);
        /*CODE HERE*/
//        function(table);
        
        //cout << "      \\->> OUT: " << "Fmax=" << Fmax << ", Dmin=" << Dmin << ", Bmin=" << Bmin << endl; //<<<<

        /// Write to Output Vector
        if(out_file.is_open()){
          out_file << "Case #" << lineN << ": " << function(table) << endl;  
        }else{
          cout << " > Unable to open output file: " << output_file << endl;
          return -1;
        }
      }
      table.clear();
      ++lineN;

      if(in_file.eof()){
        break;
      }

    }
    cout << "\n";     

  }else{
    cout << " > Unable to open input file: " << input_file << endl;
    return -1;
  }
  
  in_file.close(); 
  out_file.close();
  
  /// Timing Results
  t = clock() - t;
  cout << " > It took me " << t << " Clicks OR " << ((float)t)/(CLOCKS_PER_SEC) << " Seconds to Process Input File and Create the Output File!" << endl;
  cout << " > Bye" << endl; 
return 0;
}
//////////////////////////////////////////////////
string function(vector<vector<char> > table)
{
  string str;
  int xh,oh,xv,ov,xda,oda,xdb,odb;
  for(int i=0; i<4; ++i){  
    xh=0;
    oh=0;
    xv=0;
    ov=0;
    xda=0;
    oda=0;
    xdb=0;
    odb=0;
    for(int j=0; j<4; ++j){  
      //horizental
      if(table[i][j]=='X'){
        ++xh;
      }else if(table[i][j]=='O'){
        ++oh;
      }else if(table[i][j]=='T'){
        ++xh;
        ++oh;
      }
      //vertical
      if(table[j][i]=='X'){
        ++xv;
      }else if(table[j][i]=='O'){
        ++ov;
      }else if(table[j][i]=='T'){
        ++xv;
        ++ov;
      }
      //diagonal 
      if(table[j][j]=='X'){
        ++xda;
      }else if(table[j][j]=='O'){
        ++oda;
      }else if(table[j][j]=='T'){
        ++xda;
        ++oda;
      }
      //diagonal 
      if(table[j][3-j]=='X'){
        ++xdb;
      }else if(table[j][3-j]=='O'){
        ++odb;
      }else if(table[j][3-j]=='T'){
        ++xdb;
        ++odb;
      }
    }
    if(xh==4 || xv==4 || xda==4 || xdb==4){
      return "X won";
    }
    if(oh==4 || ov==4 || oda==4 || odb==4){
      return "O won";
    }    
  }
  for(int i=0; i<4; ++i){
    for(int j=0; j<4; ++j){
      if(table[i][j]=='.'){
        return "Game has not completed";
      }
    }
  }
return "Draw";
}
//////////////////////////////////////////////////
