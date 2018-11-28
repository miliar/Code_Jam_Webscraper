#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <cstring>

using namespace std;

string itoa(int val) {stringstream ss;ss << val;return ss.str();}
typedef vector<int> vi;
vi parseInt(string s) {stringstream ss(s);vi ans;while (!ss.eof()) {int temp; ss >> temp; ans.push_back(temp); } return ans;}
#define COPY(x,y) y.resize(x.size());copy(x.begin(),x.end(),y.begin())
#define pb push_back
#define SWAP(t,x,y) t temp=x;x=y;y=temp;
#define fr(i,s,e) for (int i = int(s); i < int(e); i++)
#define fr2(i,c) for (unsigned int i = 0; i < (c).size(); i++)
#define cl(a,val) memset(a,val,sizeof(a)); 
#define ll long long
#define INF 1000000000

bool board[200][200];
int sr,sc,mr,mc,cnt;

int calc() {
  bool new_board[200][200];
  int sec = 0;
  int newcnt = 0;
  while(cnt>0) {
    sec++;
    newcnt = 0;
    for(int a=sr;a<mr;a++) {
      for(int b=sc;b<mc;b++) {
        if (board[a][b]) {
          if (board[a-1][b]==false && board[a][b-1]==false) {
            new_board[a][b] = false;
          } else {
            new_board[a][b] = true;
            newcnt++;
          }
        } else {
          if (board[a-1][b] && board[a][b-1]) {
            new_board[a][b] = true;
            newcnt++;
          } else {
            new_board[a][b] = false;
          }
        }
      }
    }
    cnt = newcnt;
    memcpy(board,new_board,sizeof(board));
  }
  return sec;
}

int main() {
	int t;
	
	ifstream fin("c.in");
	ofstream fout("c.ans");
	
	fin >> t;
	
	fr(x,0,t) {
	  int r;
    fin >> r;
    cl(board,0);
    mr = 0; mc = 0;
    sr = 200; sc = 200;
    cnt = 0;
    fr(i,0,r) {
      int x1,y1,x2,y2;
      fin >> x1 >> y1 >> x2 >> y2;
      sr = min(y1-1,sr); sc = min(x1-1,sc);
      mr = max(y2+1,mr); mc = max(x2+1,mc);
      for(int a=x1;a<=x2;a++)
        for(int b=y1;b<=y2;b++) {
          board[b][a] = true;
          cnt++;
        }
    }
    int res = calc();
		cout << "Case #" << x+1 << ": " << res << endl;
		fout << "Case #" << x+1 << ": " << res << endl;
	}
	
	fin.close();
	fout.close();
	return 0;
}
