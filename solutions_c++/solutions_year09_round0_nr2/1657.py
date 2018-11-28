#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <boost/foreach.hpp>
#include <boost/lexical_cast.hpp>

using namespace std;

const int di[]={-1,0,0,1};
const int dj[]={0,-1,1,0};

void paint(vector<vector<char> >& div, const vector<vector<int> >& dir, int i, int j){
  const char c = div[i][j];
  const int H = dir.size();
  const int W = dir[0].size();

  for(int k=0;k!=4;++k){
    const int ii = i + di[k];
    const int jj = j + dj[k];
    if(0<=ii && ii<H && 0<=jj && jj<W){
      const int kk = dir[ii][jj];
      if(kk>=0){
	const int iii = ii + di[kk];
	const int jjj = jj + dj[kk];
	if(iii==i && jjj==j){
	  div[ii][jj] = c;
	  paint(div, dir, ii, jj);
	}
      }
    }
  }
}

string solve(const vector<vector<int> >& mp){
  const int H = mp.size();
  const int W = mp[0].size();

  char c(1);
  vector<vector<char> > div(H);
  vector<vector<int> > dir(H);
  for(int i=0;i!=H;++i){
    dir[i].resize(W,-1);
    div[i].resize(W,0);
    for(int j=0;j!=W;++j){
      int mink(-1);
      int minh(mp[i][j]);
      for(int k=0;k!=4;++k){
	const int ii = i+di[k];
	const int jj = j+dj[k];
	if(0<=ii && ii<H && 0<=jj && jj<W){
	  if(mp[ii][jj] < minh){
	    minh = mp[ii][jj];
	    mink = k;
	  }
	}
      }
      if(mink>=0){
	dir[i][j] = mink;
      }
      else{
	div[i][j]=c;
	++c;
      }
    }
  }
  for(int i=0;i!=H;++i){
    for(int j=0;j!=W;++j){
      if(dir[i][j] < 0){
	paint(div, dir, i, j);
      }
    }
  }
  vector<vector<char> > rmp(H);
  for(int i=0;i!=H;++i){
    rmp[i].resize(W,0);
  }
  c='a';
  for(int i=0;i!=H;++i){
    for(int j=0;j!=W;++j){
      if(!rmp[i][j]){
	const char cc = div[i][j];
	for(int ii=0;ii!=H;++ii){
	  for(int jj=0;jj!=W;++jj){
	    if(div[ii][jj] == cc){
	      rmp[ii][jj] = c;
	    }
	  }
	}
	++c;
      }
    }
  }

  string ret;
  for(int i=0;i!=H;++i){
    for(int j=0;j!=W;++j){
      ret += rmp[i][j];
      if(j<W-1)ret += " ";
      else ret += "\n";
    }
  }
  return ret;
}

int main(int argc, char* argv[]){
  const int buf_size = 1024;
  char buf[buf_size];

  int T;
  cin >> T;
  for(int i=0;i!=T;++i){
    int H, W;
    cin >> H >> W;
    vector<vector<int> > mp(H);
    for(int j=0;j!=H;++j){
      mp[j].resize(W);
      for(int k=0;k!=W;++k){
	cin >> mp[j][k];
      }
    }
    cout << "Case #" << (i+1) << ":" << endl;
    cout << solve(mp);
  }
  return 0;
}
