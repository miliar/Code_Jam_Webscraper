#include <iostream>
#include <sstream>
#include <unordered_map>
#include <algorithm>
#include <iterator>
#include <functional>
#include <vector>
#include <string>

using namespace std;


int main() {
 
  int nr = 0;
  int maxNr;
  cin >> maxNr;
  cin.ignore(10,'\n');
  cerr <<  "maxNr= " << maxNr << endl;

  string line;
  getline(cin,line);

  while(nr < maxNr && !cin.eof() && !line.empty()) { 
    stringstream sin(line,stringstream::in);
    // read meta infos
    int N,S,p;
    sin >> N >> S >> p;
    vector<int> scores;
    istream_iterator<int> eof,it(sin);
    copy(it,eof,back_inserter(scores));
    // process input

    int minRes = p + 2*(p-1); // min possible result
    if(minRes < 0) minRes = p;
    int minResS = p + 2*(p-2); // min possible surprising result;
    if(minResS < 0) minResS = p;

    cerr << "p: " << minRes << " pS: " << minResS << endl;

    // count googlers with a result > minRes and minResS
    copy(scores.begin(),scores.end(),ostream_iterator<int>(cerr,", "));
    cerr << endl;
    auto gtminRes = bind2nd(greater_equal<int>(),minRes);
    int cnt = count_if(scores.begin(),scores.end(),gtminRes);
    auto scoreEnd = remove_if(scores.begin(),scores.end(),gtminRes);
    
    copy(scores.begin(),scoreEnd,ostream_iterator<int>(cerr,", "));
    cerr << endl;
    int cntS = count_if(scores.begin(),scoreEnd,bind2nd(greater_equal<int>(),minResS));
    
    // for normal mode cnt googlers have at least p as max score
    // in special voting cntS have at least p as max score, but only 2 of them are possible
    // so if the difference between cnt and cnts is >2, only 2 googlers are added
    cerr << cnt << " " << cntS << endl;
    int googlers = cnt;
    if(cntS >= S) {
      googlers += S;
    } else if(cntS > 0){
      googlers += cntS;
    }

    cout << "Case #" << ++nr << ": " << googlers << endl;

    // read next line
    getline(cin,line);
  }
  

  if(nr != maxNr) {
    cerr << "unexpected end of stream..." << nr << " " << maxNr << endl;
  }

  return 0;
}

