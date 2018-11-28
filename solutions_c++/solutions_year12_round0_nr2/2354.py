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

// for one googler
void computeAllPossibleScores(int& iScoreSum, int& iBestScore, bool& result,
                              bool& resultWithoutSurprsing,
                           std::vector<int> oScore1,
                           std::vector<int> oScore2,
                           std::vector<int> oScore3) {

  result = 0;
  for (int i = 0; i < 11; i++) {
    for (int j = 0; j < 11; j++) {
      for (int k = 0; k < 11; k++) {
        // surprising score ok
        if (i+j+k == iScoreSum &&
            maxDiscr(i,j,k)<3) {
          oScore1.push_back(i); 
          oScore2.push_back(j); 
          oScore3.push_back(k); 
          if(k >= iBestScore || i >= iBestScore || j >= iBestScore) {
            result = true;
          }
        }

        // no surprising score
        if (i+j+k == iScoreSum &&
            maxDiscr(i,j,k)<2) {
          oScore1.push_back(i);
          oScore2.push_back(j);
          oScore3.push_back(k);
          if(k >= iBestScore || i >= iBestScore || j >= iBestScore) {
            resultWithoutSurprsing = true;
          }
        }

      }
    }
  }

  for (int score = 0; score < oScore1.size(); score++) {
    cout << oScore1[score] << " " <<
         oScore2[score] << " " 
      << oScore3[score] << endl;
  }

}

int solve(int& nbGooglers, int& nbSurprisingScore, 
      int& p, std::vector<int>& scoreSums) {
  // display input
  cout << "nbGooglers " << nbGooglers << endl;
  cout << "nbSurprisingScore " << nbSurprisingScore << endl;
  cout << "p " << p << endl;
  int result = 0;
  int resultNoSurp = 0;
  int i = 1;
  for(std::vector<int>::iterator itScoreSum = scoreSums.begin(); 
    itScoreSum != scoreSums.end(); ++itScoreSum) { 
    cout << "Scoresum for googler " << i << " : " << *itScoreSum << endl;

    std::vector<int> score1;
    std::vector<int> score2;
    std::vector<int> score3;
    bool resultBool = false;
    bool resultBoolWithoutSurprising = false;
    computeAllPossibleScores(*itScoreSum, p,
                         resultBool, resultBoolWithoutSurprising,
                                     score1, score2, score3);
    if(resultBool) { ++result; }
    if(resultBoolWithoutSurprising) { ++resultNoSurp; }
    //cout << "result    suprise " << i << " " << resultBool << endl;
    //cout << "result no suprise " << i << " " << 
    //    resultBoolWithoutSurprising << endl;

    ++i;
  } 
  //cout << "result " << result << endl; 
  //cout << "result no surprise " << resultNoSurp << endl; 
  if (result - resultNoSurp > nbSurprisingScore) {
    // complex case : the number of surprising scores matter
    int returnb = resultNoSurp + nbSurprisingScore;
    return min(returnb, result);
  }else{
    return result; 
  }
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
      for(std::vector<int>::iterator itParam = params.begin(); 
          itParam != params.end(); ++itParam) { 
        //cout << *itParam << endl;
      } 
      std::vector<int> sumScores;
      int count=0;
      for(std::vector<int>::iterator itScore = params.begin(); 
        itScore != params.end(); ++itScore) { 
        if(count<3) { ++count; continue; }
        sumScores.push_back(*itScore);
        ++count;  
      } 
      
      int result = solve(params[0], params[1], params[2], sumScores);
      cout << "result " << result << endl; 
      ostringstream resultStream;
      resultStream << result;
      resultVector.push_back(resultStream.str());
      resultStream.str("");
    }
  } 

  printOutputFile(resultVector);
}



