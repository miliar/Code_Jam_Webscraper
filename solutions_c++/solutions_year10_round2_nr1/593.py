#include <map>
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>

using namespace std;

class CDir
{
public:
  map<string, CDir> dir;

  CDir(){
    dir.clear();
  }

  int add(string path)
  {
    int count=0;
    string dir_name;
    int index;

    index = path.find("/");

    if(index == string::npos){
      dir_name = path;
    }
    else{
      dir_name = path.substr(0, index);
    }

    map<string, CDir>::iterator it = dir.find(dir_name);

    if(it == dir.end()){
      count++;
      dir[dir_name] = CDir();
    }

    if(index == string::npos)return count;

#if 0
    printf("dirname %s %d(substr=%s)\n", dir_name.c_str(), count,
	   path.substr(index+1).c_str());
#endif

    return dir[dir_name].add(path.substr(index+1)) + count;
  }
};

int solve(void)
{
  int N, M;
  int count=0;
  CDir root=CDir();

  cin >> N >> M;

  for(int i=0; i<N; i++){
    string path;
    
    cin >> path;

    root.add(path.substr(1));
  }

  for(int i=0; i<M; i++){
    string path;
    
    cin >> path;

    int a =root.add(path.substr(1));
    // printf("%s %d\n", path.c_str(), a);

    count += a;
  }

  return count;
}

int main()
{
  int T;

  cin >> T;

  for(int i=0; i<T; i++){
    printf("Case #%d: %d\n", i+1, solve());
  }
}
