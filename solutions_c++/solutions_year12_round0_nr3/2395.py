#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <iostream>
#include <fstream>
#include <sstream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>

#define fo(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define _(a,b) memset( a, b, sizeof( a ) )
using namespace std;
int ni() { int a; scanf( "%d", &a ); return a; }
double nf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100005]; string ns() { scanf( "%s", sbuf ); return sbuf; }
long long nll() { long long a; scanf( "%lld", &a ); return a; }

template <class T> void out( T a, T b ) { bool first = true; for( T i = a; i != b; ++ i ) { if( !first ) printf( " " ); first = false; cout << * i; } printf( "\n" ); }
template <class T> void outl( T a, T b ) { for( T i = a; i != b; ++ i ) { cout << * i << "\n"; } }
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;

void readFile(const char* filename, vector<string>& outputVect)
{
  string STRING;
  ifstream infile;
  infile.open (filename);
  while(!infile.eof()) // To get you all the lines.
  {
    getline(infile,STRING); // Saves the line in STRING.
    outputVect.push_back(STRING);
  }
  infile.close();
  outputVect.pop_back();
}

int printOutputFile(vector<string>& inputVect)
{

  freopen( "output.txt", "w", stdout );

  int t=1;
  for(vector<string>::iterator itLine = inputVect.begin();
      itLine != inputVect.end(); ++itLine)
  {
    //if(itLine == inputVect.begin()) { continue; }
    stringstream ouputLineStream;
    ouputLineStream << "Case #" << t << ": " << *itLine << endl;
    printf(ouputLineStream.str().c_str(), t );
    //printf(" \n", t);
    ++t;
  }

  return 0;
}

void tokenize(string& iProblemString, std::vector<int>& oParams) {
  stringstream stream(iProblemString);
  string tempString;
  while(getline(stream, tempString, ' ') )
    oParams.push_back(atoi(tempString.c_str())); 
}

int max(int& a, int& b, int& c) {
  int max = a;
  if(b > max) { max = b; }
  if(c > max) { max = c; }
  return max;
}

int maxDiscr(int& a, int& b, int& c) {

  int length1 = abs(b-a);
  int length2 = abs(c-a);
  int length3 = abs(b-c);
  int result = max(length1, length2, length3);
  return result;

}

int solveB(int& A, int& B) {
  int result = 0;

  for (int n = A; n <= B; n++) {
      // todo : determine if n,m is a valid recycled pair
      stringstream stream;
      stream << n;
      string nString = stream.str();
      stream.str("");

      std::vector<char> nVect( nString.begin(), nString.end() );


      int nbDigits = nVect.size();
      std::set<int> nStringAlternates;

      for (int i = 0; i < nbDigits; i++) {
        std::vector<char> nVectAlternate;
        for (int j = 0; j < nbDigits; j++) {
          nVectAlternate.push_back(nVect[(j+i)%nbDigits]);
        }
        if(nVectAlternate[0]!='0') {
          std::string nStringAlternate( nVectAlternate.begin(), nVectAlternate.end() );
          int value = atoi(nStringAlternate.c_str());
          // cout << nStringAlternate << "  " <<  value << endl;
          nStringAlternates.insert(value);
        }
      }

      for(std::set<int>::iterator itAlternateMstring = nStringAlternates.begin(); 
          itAlternateMstring != nStringAlternates.end(); ++itAlternateMstring) { 
        if(n < *itAlternateMstring && *itAlternateMstring <= B) {
            ++result;
        }
      } 

  }


  return result;
}
int solve(int& A, int& B) {
  int result = 0;

  for (int n = A; n < B; n++) {
    for (int m = n+1; m <= B; m++) {
      // todo : determine if n,m is a valid recycled pair
      stringstream stream;
      stream << n;
      string nString = stream.str();
      stream.str("");

      stream << m;
      string mString = stream.str(); 

      std::vector<char> nVect( nString.begin(), nString.end() );
      std::vector<char> mVect( mString.begin(), mString.end() );

      std::set<int> sn;
      for(std::vector<char>::iterator itN = nVect.begin(); 
          itN != nVect.end(); ++itN) { 
        sn.insert(*itN);
      } 

      std::set<int> sm;
      for(std::vector<char>::iterator itM = mVect.begin(); 
          itM != mVect.end(); ++itM) { 
        sm.insert(*itM);
      } 

      std::set<int> difference;
      std::set_difference(sn.begin(), sn.end(),
          sm.begin(), sm.end(),
          std::inserter(difference, difference.begin()));
      if(difference.empty()) {

        int nbDigits = nVect.size();
        std::set<string> mStringAlternates;

        for (int i = 0; i < nbDigits; i++) {
          if(nVect[0] == mVect[i]) {
            std::vector<char> mVectAlternate;
            for (int j = 0; j < nbDigits; j++) {
              mVectAlternate.push_back(mVect[(j+i)%nbDigits]);
            }
            if(mVectAlternate[0]!=0) {
              std::string mStringAlternate( mVectAlternate.begin(), mVectAlternate.end() );
              mStringAlternates.insert(mStringAlternate);
            }
          }
        }

        for(std::set<string>::iterator itAlternateMstring = mStringAlternates.begin(); 
            itAlternateMstring != mStringAlternates.end(); ++itAlternateMstring) { 
          if(nString.compare(*itAlternateMstring) == 0) {
            //cout << A << " <= " << n << " < " << m << " <= " << B << endl;
            ++result;
          }
        } 

      }
    }
  }


  return result;
}

int main( )
{
  string filename = "input.txt";
  vector<string> fileStringVect;
  readFile(filename.c_str(), fileStringVect);

  std::vector<string> resultVector;

  for(std::vector<string>::iterator itLine = fileStringVect.begin();
      itLine != fileStringVect.end(); ++itLine) {
    //cout << *itLine << endl;
    if(itLine!=fileStringVect.begin()) {
      std::vector<int> params;
      tokenize(*itLine, params);
      /*for(std::vector<int>::iterator itParam = params.begin();
        itParam != params.end(); ++itParam) {
      //cout << *itParam << endl;
      }*/
      cout << params[0] << " " << params[1] << endl;
      int result = solveB(params[0], params[1]);
      stringstream stream;
      stream << result;
      resultVector.push_back(stream.str());
      stream.str("");
    }
  }


  printOutputFile(resultVector);

}

