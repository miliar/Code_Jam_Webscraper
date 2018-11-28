#include<iostream>
#include<map>
#include<vector>

using namespace std;

typedef map<char,bool> PresenceMap;
typedef map< int, PresenceMap > MatcherMap;

bool matches(MatcherMap &mv, string &s) {
  for(int i=0; i<s.length(); i++) {
    if(! mv[i][s[i]] ) {
      return false;
    }
  }
  return true;
}

void initializeMatcher(MatcherMap &matchMap, string s) {
  // string s = "(abc)(bc)a(ca)";


  
  bool insideGroup = false;
  int groupId = -1;

  for(int pos = 0; pos < s.length(); pos++) {

    if(!insideGroup) {

//       if(map_ptr !=0) {
//         PresenceMap &p = *map_ptr;
//         for(PresenceMap::iterator it = p.begin();
//             it != p.end(); it++ ) {
//           cout << "first: " << it->first << " second: " << it->second << endl;
//         }
//       }

      groupId++;
//       map_ptr = new PresenceMap;
//       mVec.push_back(*map_ptr);
    }

    char c = s[pos];
    switch(c) {
    case '(':
      insideGroup = true;
      break;
    case ')':
      insideGroup = false;
      break;
    default:
//       cout << groupId << " : " << c 
//            << endl;
      matchMap[groupId][c] = true;
    }
    
  }

}


int main() {
  int L,D,N;
  cin >> L >> D >> N;

  // input all the D lines
  vector<string> dlines;
  for(int d = 0; d<D; d++) {
    string s;
    cin >> s;
    dlines.push_back(s);
  }
  
  // input all the N pattern lines 
//   vector<string> patternVec;

  for(int p = 0; p<N; p++) {
    string s;
    cin >> s;
//     patternVec.push_back(s);

    // create a matcher and count the matches
    MatcherMap matchMap;
    initializeMatcher(matchMap, s);

    int count = 0;
    for(vector<string>::iterator dit = dlines.begin();
      dit != dlines.end();
      dit++) {
      
      if(matches(matchMap, *dit)) {
        // cout << "its a match" << endl;
        count++;
      } else {
        // cout << "its not a match" << endl;
      }
    }

    cout << "Case #" << p+1 << ": " << count << endl;
  }
}



// void t()
// {
//   cout << matchMap.size() << endl;

//   for(MatcherMap::iterator mit = matchMap.begin();
//       mit != matchMap.end() ; mit++ ) {
//     for(PresenceMap::iterator it = (mit->second).begin();
//         it != (mit->second).end(); it++ ) {
//       cout << mit->first  << "::" << "first: " << it->first << " second: " << it->second << endl;
//     }
//   }

  
  
//   string test_string = "abac";

//   if(matches(matchMap, test_string)) {
//     cout << "its a match" << endl;
//   } else {
//     cout << "its not a match" << endl;
//   }

//   test_string = "aaaa";
//   if(matches(matchMap, test_string)) {
//     cout << "its a match" << endl;
//   } else {
//     cout << "its not a match" << endl;
//   }
// }

