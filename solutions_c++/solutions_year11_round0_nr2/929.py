#include<cstdio>
#include<vector>
#include<map>
#include<set>
#include<algorithm>

using namespace std;

char buff[10];

int main() {
  int T;
  scanf("%d", &T);
  for(int t = 1; t <= T; t++) {
    map<pair<char, char>, char> comb;
    set<pair<char, char> > opp;

    int C, D, N;
    scanf("%d", &C);
    for(int i = 0; i < C; i++)
    {
      scanf("%s", buff);
      comb[make_pair(buff[0], buff[1])] = buff[2];
      comb[make_pair(buff[1], buff[0])] = buff[2];
    }

    scanf("%d", &D);
    for(int i = 0; i < D; i++)
    {
      scanf("%s", buff);
      opp.insert(make_pair(buff[0], buff[1]));
      opp.insert(make_pair(buff[1], buff[0]));
    }

    scanf("%d", &N);
    vector<char> list;
    char buff[N+10];
    scanf("%s", buff);
    for(int i = 0; i < N; i++)
    {
      if(!list.empty() && comb.count(make_pair(list.back(), buff[i])))
        list.back() = comb[make_pair(list.back(), buff[i])];
      else {
        list.push_back(buff[i]);
        for(int j = 0; j < list.size(); j++)
          if(opp.count(make_pair(buff[i], list[j])))
          {
            list.clear();
            break;
          }
      }
    }
    
    printf("Case #%d: [", t);
    for(int j = 0; j < list.size(); j++)
      printf(j ? ", %c" : "%c", list[j]);
    printf("]\n");
  }
}
