// last update : 2013-04-13 13:26:47 nav

#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <algorithm>

using namespace std;
typedef long long ll;

#define ALL(a)  (a).begin(),(a).end()

const int INF = 1 << 29;
const double EPS = 1e-7;

int main(int argc, char **argv){
  int N;
  cin >> N;
  for(int k = 0; k < N; k++){  
    vector<string> table;
    for(int j = 0; j < 4; j++){
      string tmp;
      cin >> tmp;
      table.push_back(tmp);
    }

    // cout << "koko" << endl;
    // for(int j = 0; j < 4; j++){
    //   cout << table[j] << endl;
    // }
    // cout << "koko" << endl;

    bool decided = false;

    //O
    for(int i = 0; i < 4; i++){
      if(count(ALL(table[i]), 'O') 
	 + count(ALL(table[i]), 'T') == 4){
	cout << "Case #" << k + 1 << ": O won" << endl;
	decided = true;
      }
    }
    
    if(!decided)
    for(int i = 0; i < 4; i++){
      int cnt = 0;
      for(int j = 0; j < 4; j++){
	if(table[j][i] == 'O' || table[j][i] == 'T')
	  cnt++;
      }
      if(cnt == 4){
	cout << "Case #" << k + 1 << ": O won" << endl;
	decided = true;
      }
    }
    
    int cnt = 0;
    int rcnt = 0;
    if(!decided)
    for(int i = 0; i < 4; i++){
      if(table[i][i] == 'O' || table[i][i] == 'T')
	cnt++;
      if(table[i][3 - i] == 'O' || table[i][3 - i] == 'T')
	rcnt++;
      if(cnt == 4 || rcnt == 4){
	cout << "Case #" << k + 1 << ": O won" << endl;
	decided = true;
      }
    }

    //X
    if(!decided)
    for(int i = 0; i < 4; i++){
      if(count(ALL(table[i]), 'X') 
	 + count(ALL(table[i]), 'T') == 4){
	cout << "Case #" << k + 1 << ": X won" << endl;
	decided = true;
      }
    }
    
    if(!decided)
    for(int i = 0; i < 4; i++){
      int cnt = 0;
      for(int j = 0; j < 4; j++){
	if(table[j][i] == 'X' || table[j][i] == 'T')
	  cnt++;
      }
      if(cnt == 4){
	cout << "Case #" << k + 1 << ": X won" << endl;
	decided = true;
      }
    }

    cnt = 0;
    rcnt = 0;
    if(!decided)
    for(int i = 0; i < 4; i++){
      if(table[i][i] == 'X' || table[i][i] == 'T')
	cnt++;
      if(table[i][3 - i] == 'X' || table[i][3 - i] == 'T')
	rcnt++;
      if(cnt == 4 || rcnt == 4){
	cout << "Case #" << k + 1 << ": X won" << endl;
	decided = true;
      }
    }


    //draw or not complete
    if(!decided){
      bool draw = false;
      for(int i = 0; i < 4; i++)
	if(count(ALL(table[i]), '.') > 0)
	  draw = true;
    
      if(!draw)
	cout << "Case #" << k + 1 << ": Draw" << endl;
      else
	cout << "Case #" << k + 1 << ": Game has not completed" << endl;
    }
  }
}
