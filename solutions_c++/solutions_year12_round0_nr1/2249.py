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

int n, m;


int count_char(string& s, char c) {
  int count = 0;

  for (int i = 0; i < s.size(); i++)
    if (s[i] == c) count++;

  return count;
}

void count_charFreq(string& s, map<char,int>& ioFreq) {
  ioFreq.insert(make_pair('a', count_char(s,'a')));
  ioFreq.insert(make_pair('b', count_char(s,'b')));
  ioFreq.insert(make_pair('c', count_char(s,'c')));
  ioFreq.insert(make_pair('d', count_char(s,'d')));
  ioFreq.insert(make_pair('e', count_char(s,'e')));
  ioFreq.insert(make_pair('f', count_char(s,'f')));
  ioFreq.insert(make_pair('g', count_char(s,'g')));
  ioFreq.insert(make_pair('h', count_char(s,'h')));
  ioFreq.insert(make_pair('i', count_char(s,'i')));
  ioFreq.insert(make_pair('j', count_char(s,'j')));
  ioFreq.insert(make_pair('k', count_char(s,'k')));
  ioFreq.insert(make_pair('l', count_char(s,'l')));
  ioFreq.insert(make_pair('m', count_char(s,'m')));
  ioFreq.insert(make_pair('n', count_char(s,'n')));
  ioFreq.insert(make_pair('o', count_char(s,'o')));
  ioFreq.insert(make_pair('p', count_char(s,'p')));
  ioFreq.insert(make_pair('q', count_char(s,'q')));
  ioFreq.insert(make_pair('r', count_char(s,'r')));
  ioFreq.insert(make_pair('s', count_char(s,'s')));
  ioFreq.insert(make_pair('t', count_char(s,'t')));
  ioFreq.insert(make_pair('u', count_char(s,'u')));
  ioFreq.insert(make_pair('v', count_char(s,'v')));
  ioFreq.insert(make_pair('w', count_char(s,'w')));
  ioFreq.insert(make_pair('x', count_char(s,'x')));
  ioFreq.insert(make_pair('y', count_char(s,'y')));
  ioFreq.insert(make_pair('z', count_char(s,'z')));
}
void count_charFreq(std::vector<string>& vString, map<char,int>& ioFreq) {

  string& s = *vString.begin();
  count_charFreq(s, ioFreq);

  for(std::vector<string>::iterator itString = vString.begin(); 
      itString != vString.end(); ++itString) { 
    
    ioFreq['a']+=count_char(*itString,'a');
    ioFreq['b']+=count_char(*itString,'b');
    ioFreq['c']+=count_char(*itString,'c');
    ioFreq['d']+=count_char(*itString,'d');
    ioFreq['e']+=count_char(*itString,'e');
    ioFreq['f']+=count_char(*itString,'f');
    ioFreq['g']+=count_char(*itString,'g');
    ioFreq['h']+=count_char(*itString,'h');
    ioFreq['i']+=count_char(*itString,'i');
    ioFreq['j']+=count_char(*itString,'j');
    ioFreq['k']+=count_char(*itString,'k');
    ioFreq['l']+=count_char(*itString,'l');
    ioFreq['m']+=count_char(*itString,'m');
    ioFreq['n']+=count_char(*itString,'n');
    ioFreq['o']+=count_char(*itString,'o');
    ioFreq['p']+=count_char(*itString,'p');
    ioFreq['q']+=count_char(*itString,'q');
    ioFreq['r']+=count_char(*itString,'r');
    ioFreq['s']+=count_char(*itString,'s');
    ioFreq['t']+=count_char(*itString,'t');
    ioFreq['u']+=count_char(*itString,'u');
    ioFreq['v']+=count_char(*itString,'v');
    ioFreq['w']+=count_char(*itString,'w');
    ioFreq['x']+=count_char(*itString,'x');
    ioFreq['y']+=count_char(*itString,'y');
    ioFreq['z']+=count_char(*itString,'z');
  }

} 
  

void getCharOrder(std::vector<string>& vString, std::vector<char>& ioOrder,
       std::map<char, int>& mapFreq) {

  count_charFreq(vString,mapFreq);

  std::map<char, int> mapCopy = mapFreq;

  while(!mapCopy.empty()) {
    char maxFreqChar;
    int maxFreq = 0;
    for(std::map<char,int>::iterator itChar = mapCopy.begin(); 
        itChar != mapCopy.end(); ++itChar) { 
      if(itChar->second >= maxFreq) {
        maxFreq = itChar->second;
        maxFreqChar = itChar->first;
      }    
    } 
    mapCopy.erase(maxFreqChar);
    ioOrder.push_back(maxFreqChar);
  }


}

void printOrderProrposition(std::vector<char>& inOrder, std::vector<char>& outOrder,
            std::map<char, int>& mapFreq) {


  std::vector<char>::iterator itOrder = inOrder.begin();
  std::vector<char>::iterator itOOrder = outOrder.begin();
  for(
    ; 
    itOrder != inOrder.end(), itOOrder != outOrder.end(); ++itOrder, ++itOOrder) { 
    cout << *itOrder << "-->" <<  *itOOrder << " (" << mapFreq[*itOOrder] << ")" << endl;
  } 
  


}

void printFreq(const map<char,int>& iFreq) {

  for(std::map<char,int>::const_iterator itFrequency = iFreq.begin(); 
      itFrequency != iFreq.end(); ++itFrequency) { 
    cout << itFrequency->first << "   " << itFrequency->second << endl;
  } 

}

int printOutputFile(vector<string>& inputVect)
{

  freopen( "output.txt", "w", stdout );

  int t=1;
  for(vector<string>::iterator itLine = inputVect.begin();
      itLine != inputVect.end(); ++itLine)
  {
    if(itLine == inputVect.begin()) { continue; }
    stringstream ouputLineStream;
    ouputLineStream << "Case #" << t << ": " << *itLine << endl;
    printf(ouputLineStream.str().c_str(), t );
    //printf(" \n", t);
    ++t;
  }

  return 0;
}

// todo provide hint
void doSubstitutionMap(std::map<char, char>& ioMapSubst,
               std::vector<char>& inOrder, std::vector<char>& outOrder,
                    std::map<char, char>& iHintMap) {

  std::map<char, char> otherMapSubst;

  std::vector<char>::iterator itInOrder = inOrder.begin();
  std::vector<char>::iterator itOutOrder = outOrder.begin();
  for(
    ; 
    itInOrder != inOrder.end(), itOutOrder != outOrder.end(); ++itInOrder, ++itOutOrder) { 
    std::map<char, char>::iterator itFind = ioMapSubst.find(*itOutOrder);
    ioMapSubst.insert(make_pair(*itOutOrder,*itInOrder));
    otherMapSubst.insert(make_pair(*itInOrder,*itOutOrder));
  } 
  
  // factor in hint map
  for(std::map<char,char>::iterator itHintMap = iHintMap.begin(); 
      itHintMap != iHintMap.end(); ++itHintMap) { 
    if (itHintMap->second != ioMapSubst[itHintMap->first]) {
      char oldValue = ioMapSubst[itHintMap->first];
      ioMapSubst[itHintMap->first] = itHintMap->second;
      ioMapSubst[otherMapSubst[itHintMap->second]] = oldValue;
      char otherOldValue =  otherMapSubst[itHintMap->second];
      otherMapSubst[itHintMap->second] = itHintMap->first;
      otherMapSubst[oldValue] = otherOldValue;
    }  
  } 


}

void doSubstitution(string& iString,
    std::map<char, char>& ioMapSubst) {

  // string to char vector
  std::vector<unsigned char> input( iString.begin(), iString.end() );

  std::vector<char> result;
  for(std::vector<unsigned char>::iterator itChar = input.begin(); 
      itChar != input.end(); ++itChar) { 
    if(*itChar == ' ') { result.push_back(' '); continue;  }
    if(*itChar == '\n') { result.push_back('\n'); continue;  }
    result.push_back(ioMapSubst[*itChar]); 
  } 

  // back to string
  iString = std::string( result.begin(), result.end() );


}

void doSubstitution(vector<string>& inputVect,
    std::map<char, char>& ioMapSubst) {


  int t=1;
  for(vector<string>::iterator itLine = inputVect.begin();
      itLine != inputVect.end(); ++itLine)
  {
    doSubstitution(*itLine,ioMapSubst);
    ++t;
  }

}

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


int main( )
{
  string filename = "input.txt";
  vector<string> fileStringVect;
  readFile(filename.c_str(), fileStringVect);
  //printOutputFile(fileStringVect);

  std::map<char, char> hintMap;

  hintMap.insert(make_pair('e', 'o'));
  hintMap.insert(make_pair('m', 'l'));
  hintMap.insert(make_pair('j', 'u'));

  hintMap.insert(make_pair('p', 'r'));
  hintMap.insert(make_pair('y', 'a'));
  hintMap.insert(make_pair('q', 'z'));
  hintMap.insert(make_pair('m', 'l'));
  hintMap.insert(make_pair('s', 'n'));
  hintMap.insert(make_pair('l', 'g'));
  hintMap.insert(make_pair('j', 'u'));
  hintMap.insert(make_pair('c', 'e'));
  hintMap.insert(make_pair('k', 'i'));
  hintMap.insert(make_pair('d', 's'));
  hintMap.insert(make_pair('x', 'm'));
  hintMap.insert(make_pair('y', 'b'));
  hintMap.insert(make_pair('w', 'd'));
  hintMap.insert(make_pair('q', 'h'));
  hintMap.insert(make_pair('h', 'p'));
  hintMap.insert(make_pair('w', 'f'));
  // string to char vector
  /*string englishOrderString1 = "etaoinsrhdlucmfywgpbvkxqjz";
  std::vector<char> englishCanonicalOrder( englishOrderString1.begin(),
      englishOrderString1.end() );

  //std::map<char, int> mapFreq;
  //count_charFreq(fileStringVect,mapFreq);
  //printFreq(mapFreq);

  std::vector<char> vOrder;
  std::map<char, int> mapFreq;
  getCharOrder(fileStringVect, vOrder, mapFreq);

  //printOrderProrposition(englishCanonicalOrder,vOrder, mapFreq);

*/

  std::map<char, char> mapSubst;
  mapSubst.insert(make_pair('a', 'y'));
  mapSubst.insert(make_pair('b', 'h'));
  mapSubst.insert(make_pair('c', 'e'));
  mapSubst.insert(make_pair('d', 's'));
  mapSubst.insert(make_pair('e', 'o'));
  mapSubst.insert(make_pair('f', 'c'));
  mapSubst.insert(make_pair('g', 'v'));
  mapSubst.insert(make_pair('h', 'x'));
  mapSubst.insert(make_pair('i', 'd'));
  mapSubst.insert(make_pair('j', 'u'));
  mapSubst.insert(make_pair('k', 'i'));
  mapSubst.insert(make_pair('l', 'g'));
  mapSubst.insert(make_pair('m', 'l'));
  mapSubst.insert(make_pair('n', 'b'));
  mapSubst.insert(make_pair('o', 'k'));
  mapSubst.insert(make_pair('p', 'r'));
  mapSubst.insert(make_pair('q', 'z'));
  mapSubst.insert(make_pair('r', 't'));
  mapSubst.insert(make_pair('s', 'n'));
  mapSubst.insert(make_pair('t', 'w'));
  mapSubst.insert(make_pair('u', 'j'));
  mapSubst.insert(make_pair('v', 'p'));
  mapSubst.insert(make_pair('w', 'f'));
  mapSubst.insert(make_pair('x', 'm'));
  mapSubst.insert(make_pair('y', 'a'));
  mapSubst.insert(make_pair('z', 'q'));
  // string to char vector

  //doSubstitutionMap(mapSubst, englishCanonicalOrder, vOrder, hintMap);

  /*for(std::map<char,char>::iterator itMapSubst = mapSubst.begin(); 
    itMapSubst != mapSubst.end(); ++itMapSubst) { 
    cout << itMapSubst->first << "--->" << itMapSubst->second << " (" 
          << mapFreq[itMapSubst->first] << ")" << endl;
  } */
  


  doSubstitution(fileStringVect, mapSubst);
  printOutputFile(fileStringVect);

}



