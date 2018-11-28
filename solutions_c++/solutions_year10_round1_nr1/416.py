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

int n,K;
int board[100][100];

void gravity() {
  fr(i,0,n) {
    int x = n-1;
    while(x>0) {
      if (board[x][i]!=0) {
        x--; continue;
      }
      int k = -1;
      for(k=x-1;k>=0;k--) {
        if (board[k][i]!=0) break;
      }
      if (k>=0 && board[k][i]!=0) {
        board[x][i] = board[k][i];
        board[k][i] = 0;
      }
      x--;
    }
  }
}

bool check_row(int r,int c,int val) {
  bool ok = true;
  fr(i,0,K) {
    if (r+i>=n) {
      ok = false;
      break;
    }
    if (board[r+i][c]!=val) {
      ok = false; break;
    }
  }
  if (ok) return true;
  ok = true;
  fr(i,0,K) {
    if (c+i>=n) {
      ok = false;
      break;
    }
    if (board[r][c+i]!=val) {
      ok = false; break;
    }
  }
  if (ok) return true;
  ok = true;
  fr(i,0,K) {
    if (r+i>=n || c+i>=n) {
      ok = false;
      break;
    }
    if (board[r+i][c+i]!=val) {
      ok = false; break;
    }
  }
  if (ok) return true;
  ok = true;
  fr(i,0,K) {
    if (r+i>=n || c-i<0) {
      ok = false;
      break;
    }
    if (board[r+i][c-i]!=val) {
      ok = false; break;
    }
  }
  if (ok) return true;
  
  return false;
}

bool check_val(int val) {
  fr(i,0,n) {
    fr(k,0,n) {
      if (check_row(i,k,val))
        return true;
    }
  }
  return false;
}

string check() {
  bool red = check_val(1);
  bool blue = check_val(2);
  if (red && blue)
    return "Both";
  if (red)
    return "Red";
  if (blue)
    return "Blue";
  return "Neither";
}

int main() {
	int t;
	
	ifstream fin("a.in");
	ofstream fout("a.ans");
	
	fin >> t;
	
	fr(x,0,t) {
	  cl(board,0);
	  fin >> n >> K;
	  string s;
	  fr(i,0,n) {
	    fin >> s;
	    fr2(k,s) {
	      if (s[k]=='.') board[k][n-i-1]=0;
	      if (s[k]=='R') board[k][n-i-1]=1;
	      if (s[k]=='B') board[k][n-i-1]=2;
	    }
	  }
	  gravity();
	  string res = check();
	  /*
	  fr(i,0,n)  {
	    fr(k,0,n) {
	      if (board[i][k]==0) cout << '.';
	      if (board[i][k]==1) cout << 'R';
	      if (board[i][k]==2) cout << 'B';
	    }
	    cout << endl;
	  }*/
		cout << "Case #" << x+1 << ": " << res << endl;
		fout << "Case #" << x+1 << ": " << res << endl;
	}
	
	fin.close();
	fout.close();
	return 0;
}
