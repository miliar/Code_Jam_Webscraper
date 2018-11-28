#include "precompiled.h"


int main() {
  string buf;
  getline(cin, buf);
  stringstream ss(buf);
  int T;
  ss >> T;

  for (int i = 0; i < T; ++i) {
    int N, M;
    getline(cin, buf);
    stringstream ss(buf);
    ss >> N >> M;

    set<string> dirs;
    for (int j = 0; j < N; ++j) {
      getline(cin, buf);
      if (buf.at(buf.size()-1) == '\r') {
	buf.resize(buf.size()-1);
      }
      dirs.insert(buf);
    }

    int res = 0;
    for (int j = 0; j < M; ++j) {
      getline(cin, buf);
      if (buf.at(buf.size()-1) == '\r') {
	buf.resize(buf.size()-1);
      }
      vector<string> paths;
      paths.push_back(buf);
      auto it = buf.rbegin();
      it = find(it, buf.rend(), '/');
      while (it != buf.rend()-1 && it != buf.rend()) {
	string path(++it, buf.rend());
	reverse(path.begin(), path.end());
	paths.push_back(path);
	it = find(it, buf.rend(), '/');
      }
      reverse(paths.begin(), paths.end());
      
      

      for (int i = 0; i < paths.size(); ++i) {
	auto it = dirs.find(paths[i]);
	if (it == dirs.end()) {
	  ++res;
	  dirs.insert(paths[i]);
	
	}
      }

    }

    cout << "Case #" << i+1 << ": " << res << endl;

  }


}
