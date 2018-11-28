/**
 * Recycled Numbers
 * Author: Sohail Munir Khan (sohail.munir@gmail.com)
 **/
#include <iostream>
#include <string>
#include <sstream>
#include <map>
using namespace std;

bool isRecycled(string& sA, string& sB) {
  size_t sALength = sA.length();
  size_t sBLength = sB.length();
  if (sALength != sBLength) return false;
  map<char,int> sACount, sBCount;
  map<char,int>::iterator it, it2;
  char t;
  for(size_t i=0; i<sALength; i++) {
    t = sA[i];
    sACount[t] ? sACount[t]++: sACount[t]=1;
  }
  for(size_t i=0; i<sBLength; i++) {
    t = sB[i];
    sBCount[t] ? sBCount[t]++: sBCount[t]=1;
  }
  
  for ( it=sACount.begin() ; it != sACount.end(); it++ ) {
    char sAChar = it->first;
    if ((it2 = sBCount.find(sAChar)) == sBCount.end() || it->second != it2->second) return false;
  }
  //cout << sA << ":" << sB << endl;
  for (size_t i=1; i<sBLength; i++) {
    string sBModified = sB.substr(i) + sB.substr(0, i);
    //cout << "Comparing now: " << sA << ":" << sBModified << endl;
    if (sA.compare(sBModified) == 0) return true;
  }
  return false;
}

bool isRecycled(int iA, int iB) {
  ostringstream sinA;
  sinA << iA;
  string sA = sinA.str();
  ostringstream sinB;
  sinB << iB;
  string sB = sinB.str();
  return isRecycled(sA, sB);
}

int getY(int A, int B) {
  int howMany = 0;
  for (int iA = A; iA < B; ++iA) {
	  for (int iB = iA + 1; iB <= B; ++iB) {
      if (isRecycled(iA, iB)) {
        ++howMany;
      }
    }
  }
  return howMany;
}

int main() {
  int T;
  cin >> T;
  // Process A & B.
  int A;
  int B;
  for (int prob = 1; prob <= T; prob++) {	
	  cin >> A >> B;
	  cout << "Case #" << prob << ": " << getY(A, B) << endl;
  }

  return 0;
}
