#include <iostream>
#include <string>
#include <set>
using namespace std;

int solve()
{
  int N, M;
  cin >> N >> M;
  set<string> pre_dir;
  for( int i = 0 ; i < N ; ++i ) {
    string dir;
    cin >> dir;
    pre_dir.insert(dir);
  }
  int mkdir = -1;
  for( int i = 0 ; i < M ; ++i ) {
    string dir;
    cin >> dir;
    dir += "/";
    int id = dir.size();
    while( (id = dir.find_last_of('/')) != string::npos ) {
      dir[id] = '\0';
      string ndir(dir.c_str());
      if( pre_dir.find(ndir) == pre_dir.end() ) {
        ++mkdir;
        pre_dir.insert(ndir);
      }
    }
  }
  return mkdir;
}

int main(void)
{
  int T;
  cin >> T;
  for( int i = 1 ; i <= T ; ++i ) {
    cerr << "Case #" << i << "\n";
    cout << "Case #" << i << ": " << solve() << "\n";
  }
  return 0;
}
