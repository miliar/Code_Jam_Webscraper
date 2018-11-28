#include <iostream>
#include <vector>
#include <map>
#include <stack>
#include <cassert>

using namespace std;

#define Forf(i,f,n) for(int i=(f);i<(n);++i)
#define For(i,n) for(int i=0;i<(n);++i)
#define foreach(it,m) for(typeof((m).begin()) it = (m).begin();it!=(m).end();++it) 

typedef pair<int,int> PII;
typedef vector<int> VI;


#define NUM 3003

int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, 1, 0, -1};


void debug(vector<vector<char> > &vcc) {
  for(int f = 0; f<vcc.size(); ++f) {
    for(int c = 0; c<vcc[f].size();++c) {
      cerr << int(vcc[c][f]);
    }
    cerr << endl;
  }
}

void set(vector<vector<char> > &v, int x, int y, int f, int dir) {
  if (dir>0) {
    if (f==0) v[x][y] = 1;
    else if (f==1) v[x][y+1] = 1;
    else if (f==2) v[x-1][y+1] = 1;
    else if (f==3) v[x-1][y] = 1;
  }
  else if (dir<0) {
    if (f==0) v[x-1][y] = 1;
    else if (f==1) v[x][y] = 1;
    else if (f==2) v[x][y+1] = 1;
    else if (f==3) v[x-1][y+1] = 1;
  }
  else assert(0);
}



void solveit() {
  vector<vector<char> > v(NUM*2+1, vector<char>(NUM*2+1, 0));
  int L;
  cin >> L;
  int x = NUM+1, y = NUM+1;
  int f = 0;
  string walk;
  int dir = 0;
  For(i,L) {
    string s;
    int c;
    cin >> s >> c;
    For(j,c) walk+=s;
  }

  For(j,walk.size()) if (walk[j]=='L') dir--; else if (walk[j]=='R') dir++;

  assert(dir !=0 );

    For(k,walk.size()) {
      if (walk[k]=='F') {
	set(v, x, y, f, dir);
	x+=dx[f]; y+=dy[f];
      }
      else if (walk[k]=='L') {
	f--; f = (f+4)%4;
      }
      else if (walk[k]=='R') {
	f++; f = f%4;
      }
    }


    //    debug(v);

  stack<PII> s;
  s.push(PII(0,0));
  while(!s.empty()) {
    
    PII p = s.top(); s.pop();
    For(i,4) {
      PII q = p;
      q.first += dx[i];
      q.second += dy[i];
      if (q.first>=0 and q.first<NUM*2+1 and q.second>=0 and q.second<NUM*2+1
	  and v[q.first][q.second]==0) {
	    v[q.first][q.second] = 2;
	    s.push(q);
	  }
    }
  }

  vector<vector<char> > poc(NUM*2+1, vector<char>(NUM*2+1, 0));

  //    debug(v);

    For(i,NUM*2+1) {
      bool vist = false;
      For(j,NUM*2+1) {
	if (v[i][j]==1) vist = true;
	if (vist and v[i][j]==2) poc[i][j]++;
      }
      
      vist = false;
      for(int j = NUM*2; j>=0; --j) {
	if (v[i][j]==1) vist = true;
	if (vist and v[i][j]==2) poc[i][j]++;
      }

      For(j,NUM*2+1) {
	if (poc[i][j]==1) poc[i][j]=0;
      }
    }

    //  debug(poc);

    For(j,NUM*2+1) {
      bool vist = false;
      For(i,NUM*2+1) {
	if (v[i][j]==1) vist = true;
	if (vist and v[i][j]==2) poc[i][j]++;
      }
      
      vist = false;
      for(int i = NUM*2; i>=0; --i) {
	if (v[i][j]==1) vist = true;
	if (vist and v[i][j]==2) poc[i][j]++;
      }
      
      For(i,NUM*2+1) {
	if (poc[i][j]<=1) poc[i][j]=0;
	else poc[i][j] = 2;
      }

    }

    //    debug(poc);

    int area = 0;
    For(i, NUM*2+1) For(j,NUM*2+1) {
      if (poc[i][j]>1) area++;
    }

    cout << area << endl;
}


int main() {
  int N;
  cin >> N;
  For(c,N) {
    cout << "Case #" << (c+1) << ": ";
    solveit();
  }
}
