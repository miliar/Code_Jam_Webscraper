#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <boost/foreach.hpp>
#include <boost/lexical_cast.hpp>

using namespace std;

const string tgt = "welcome to code jam";

int solve(const string& str){
  vector<vector<int> > poss(tgt.size());
  for(int i=0;i!=poss.size();++i){
    for(int j=0;j!=str.size();++j){
      if(str[j]==tgt[i]){
	poss[i].push_back(j);
      }
    }
  }
  vector<vector<int> > m(tgt.size());
  m[0].resize(poss[0].size());
  for(int j=0;j!=m[0].size();++j){
    m[0][j]=1;
  }
  for(int i=1;i!=m.size();++i){
    m[i].resize(poss[i].size(),0);
    for(int j=0;j!=m[i].size();++j){
      for(int k=0;k!=m[i-1].size();++k){
	if(poss[i-1][k] < poss[i][j]){
	  m[i][j] += m[i-1][k]%10000;
	}
	else{
	  break;
	}
      }
    }
  }
  int ret(0);
  for(int i=0;i!=m.back().size();++i){
    ret += m.back()[i];
    ret %= 10000;
  }
  return ret;
}

int main(int argc, char* argv[]){
  const int buf_size = 1024;
  char buf[buf_size];

  int N;
  cin >> N;
  cin.getline(buf, buf_size);
  vector<string> lines;
  for(int i=0;i!=N;++i){
    cin.getline(buf, buf_size);
    lines.push_back(buf);
  }
  for(int i=0;i!=N;++i){
    int res = solve(lines[i]);
    string str = "0000" + boost::lexical_cast<string>(res);
    cout << "Case #" << (i+1) << ": " << str.substr(str.size()-4,4) << endl;
  }
  return 0;
}
