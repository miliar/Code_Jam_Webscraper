#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <cstdio>
#include <map>
#include <queue>
#include <algorithm>
#include <fstream>
#include <cmath>

#define For(i,n) for(int i=0;i<(n);i++)
#define For1(i,n) for(int i=1;i<=(n);i++)
#define ll long long
#define clear(d) memset(d,0,sizeof(d))
#define INF 2000000000

using namespace std;

struct Bot{
  int l;
  int t;
};

int newtime(Bot &bot, int loc, int curr) {
  return max(curr + 1, bot.t + abs(bot.l - loc) + 1);
}

int main(int argc, char** argv){
  fstream fin(argv[1], ios::in);
  fstream fout("./result.out", ios::out);
  int CN;
  fin >> CN;
  For1(CI,CN){
    int n;
    int loc;
    int t=0;
    Bot orange = {1, 0};
    Bot blue = {1, 0};
    fin >> n;
    For(i,n){
      string bot_s;
      fin >> bot_s;
      if (bot_s == "O"){
        fin >> loc;
        t = newtime(orange, loc, t);
        orange.t = t;
        orange.l = loc;
      }
      else {
        fin >> loc;
        t = newtime(blue, loc, t);
        blue.t = t;
        blue.l = loc;
      }
    }

    cout << "Case #" << CI << ": " << t << endl;
    fout << "Case #" << CI << ": " << t << endl;
  }
  fin.close();
  fout.close();
}
