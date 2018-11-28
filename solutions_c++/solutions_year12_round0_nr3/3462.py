#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <sstream>
#include <stdlib.h>
#include <list>

using namespace std;


void readTestCase(ifstream& f, int& A, int& B){  f >> A;  f >> B;}


int countPairs(int a, int b, string sa)
{
 list<string> theList;
 int S = sa.size();
 if(S==1) return 0;
 string sb=string(sa);
 string sx;
 

 for(int x=a; x<=b; x++){
	stringstream out;
	out << x;
   sx = out.str();
	for(int idx = 1; idx < S; idx++){
	 
	  strncpy(&(sb[0]), &(sx[idx]), S-idx );
	  strncpy(&(sb[S-idx]), &(sx[0]), idx);
	  
	  if(sb[0]=='0') continue;
	  
	  int ib = atoi(&(sb[0]));
	  if(x < ib && ib <= b && ib  > a) {
// 		cout <<"               " << x << " : " << ib << endl;
		theList.push_back(sx+sb);
	  }
	}
 }
 theList.unique();
 //cout << "Listsize: " <<  theList.size() << endl;
 return theList.size(); 
}


int main(int argc, char** argv)
{
 int N;
 
 int A;
 int B;
 
 
 ifstream file;
 file.open(argv[1]);
 if(!file) return 0;
 
 file >> N;
 
 for(int n=1; n<=N; n++){
  readTestCase(file, A, B);
  string sa;
  stringstream out;
  out << A;
  sa = out.str();
  int pairs =  countPairs(A, B, sa);
  cout << "Case #" << n << ": " << pairs << endl;
 
 }


 return 0;
}
 
