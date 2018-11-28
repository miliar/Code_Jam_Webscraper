int N;

#include <stdio.h>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <assert.h>

using namespace std;

int main()
{
  // Input
  scanf("%d\n",&N);
  fprintf(stderr,"N = %d: \n",N);

  // Output
  for (int x=1; x<=N; x++) {
    fprintf(stderr,"Case #%d: \n",x);

    string str;
    getline(cin,str);
    stringstream ss(str);
    int C;
    ss >> C;
    map<pair<char,char>, char > comb;
    for (int i=0; i<C; i++) {
        string abc;
        ss >> abc;
        assert(abc.size() == 3);
        fprintf(stderr,"%d=%s\n",i, abc.c_str());
        comb[make_pair(abc[0],abc[1])] = abc[2];
        comb[make_pair(abc[1],abc[0])] = abc[2];
    }
    int D;
    ss >> D;
    set<pair<char,char> > opp;
    for (int i=0; i<D; i++) {
        string xy;
        ss >> xy;
        assert(xy.size() == 2);
        fprintf(stderr,"%d=%s\n",i, xy.c_str());
        opp.insert(make_pair(xy[0],xy[1]));
        opp.insert(make_pair(xy[1],xy[0]));
    }
    int M;
    string seq;
    ss >> M >> seq;
    assert(seq.size() == M);
    string res;
    for (int i=0; i<M; i++) {
        res += seq[i];
        int n = res.size();
        typedef pair<char,char> PP;
        pair<char,char> top (res[n-1], res[n-2]);
        if (n < 2) {
            // nothing happens
        }
        else if (comb.find(top) != comb.end()) {
            res.erase(n-2, 2);
            res += comb[top];
            fprintf(stderr,"%c+%c = %c\n",top.first, top.second, comb[top]);
        }
        // Search for opposing elements
        n = res.size();
        for (int j=0; j<n-1; j++) {
          PP test(res[j], res[n-1]);
          if (opp.find(test) != opp.end()) {
            fprintf(stderr,"%c+%c = BANG!\n",res[j], res[n-1]);
            res.clear();
            break;
          }
        }
        fprintf(stderr,"step %d --> %s\n",i, res.c_str());
    }

    printf("Case #%d: [",x);
    for (int i=0; i<res.size(); i++) {
        if (i<res.size()-1) {
            printf("%c, ",res[i]);
        }
        else {
            printf("%c",res[i]);
        }
    }
    printf("]\n",x);
  }
  return 0;
}
