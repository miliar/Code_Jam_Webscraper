#include <iostream>
#include <algorithm>
#include <string>
#include <cstdio>
#include <list>
#include <vector>
#include <set>
#include <map>

using namespace std;

int main()
{
	//freopen("test.txt","r",stdin);freopen("test.out","w",stdout);
	//freopen("B-small.in","r",stdin);freopen("B-small.out","w",stdout);
	freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
	int testcase;
	cin >> testcase;
  
  // build the map from base char to int
  map<char, int> b; // map of base characters
  b['Q'] = 0;
  b['W'] = 1;
  b['E'] = 2;
  b['R'] = 3;
  b['A'] = 4;
  b['S'] = 5;
  b['D'] = 6;
  b['F'] = 7;

	for (int caseId=1;caseId<=testcase;caseId++)
	{
    vector< map<char,char> > com(8); // combination rules
    vector< set<char> > opp(8); // opposition rules

		int C, D, N;
    string s;
    // read the combination rules
    cin >> C;
    if(C != 0) {
      for(int i=0; i<C; i++) {
        cin >> s; // s has 3 characters
        int j=b[s[0]];
        int k=b[s[1]];
        if(com[j].count(s[1]) == 0)
          com[j].insert(make_pair(s[1],s[2]));
        if(com[k].count(s[0]) == 0)
          com[k].insert(make_pair(s[0],s[2]));
      }
    }
    // read the opposition rules
    cin >> D;
    if(D !=0) {
      for(int i=0; i<D; i++) {
        cin >> s; // s has 2 characters
        int j=b[s[0]];
        int k=b[s[1]];
        if(opp[j].count(s[1]) == 0)
          opp[j].insert(s[1]);
        if(opp[k].count(s[0]) == 0)
          opp[k].insert(s[0]);
      }
    }
    // read the final string and process
    list<char> l; // current list
    map<char, int> lc; // count of characters in l
    cin >> N;
    cin >> s;
    for(int i=0; i<N; i++) {
      int k = b[s[i]];
      // check whether can combine
      char x = l.back();
      if(com[k].count(x) !=0) { // s[i] can combine with x
        l.pop_back();
        char y = (com[k])[x]; // the result of the combination
        l.push_back(y);
        // update lc
        lc[x]--;
        lc[y]++;
      }
      else { // cannot combine
        // add to the list and check whether can clear 
        l.push_back(s[i]);
        lc[s[i]]++;
        // loop on the opposition list of s[i], check its count in lc
        for(set<char>::iterator it=opp[k].begin(); it!=opp[k].end(); it++) {
          if(lc[*it] != 0) { // we should clear
            l.clear();
            lc.clear();
            break;
          }
        }
      }
    }

		printf("Case #%d: ",caseId);
    // print the list
    list<char>::size_type n = l.size();
    list<char>::size_type k = 0;
    printf("[");
    for(list<char>::iterator it=l.begin(); it!=l.end(); it++) {
      printf("%c", *it);
      k++;
      if(k != n)
        printf(", ");
    }
    printf("]");
		printf("\n");
	}

	return 0;
}
