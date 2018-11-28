#include <iostream>
#include <string>
#include <map>
#include <list>
using namespace std;

string pull(string &path)
{
  //cout << "'" << path << "' --> ";
  int idx = path.find('/', 1);
  
  if(idx == string::npos)
  {
      //cout << "'" << path << "' + ''" << endl;
      string ret = path;
      path = "";
      return ret;
  }
  
  string ret = path.substr(0, idx);
  path = path.substr(idx);
  //cout << "'" << ret << "' + '" << path << "'" << endl;
  return ret;
}

class Directory
{
  map<string, Directory*> data;
public:
  void add(string path)
  {
    if(path == "")
      return;
    string part = pull(path);
    
    Directory *dir = data[part];
    if(dir == NULL)
    {
      dir = new Directory;
      data[part] = dir;
    }
    
    dir->add(path);
  }
  
  int count(string path)
  {
    if(path == "")
      return 0;
    
    string part = pull(path);
    
    if(data[part] == NULL)
    {
      int ret = 1;
      
      for(int i = 0; i < path.length(); i++)
        if(path[i] == '/')
          ret ++;
      
      return ret;
    }
    
    return data[part]->count(path);
  }
};

int solve()
{
  int N, M;
  cin >> N >> M;
  Directory root;
  list<string> toAdd;
  
  for(int i = 0; i < N; i++)
  {
    string str;
    cin >> str;
    root.add(str);
  }

  for(int i = 0; i < M; i++)
  {
    string str;
    cin >> str;
    toAdd.push_back(str);
  }
  
  int ret = 0;
  for(int i = 0; i < M; i++)
  {
    typedef list<string>::iterator it;
    
    int min = 99999999;
    string minstr = "";
    
    for(it j = toAdd.begin(); j != toAdd.end(); j++)
    {
      int c = root.count(*j);
      if(c < min)
      {
        min = c;
        minstr = *j;
      }
    }
    
    //cout << "Adding " << minstr << " with cost of " << min << endl;
    root.add(minstr);
    ret += min;
    toAdd.remove(minstr);
  }
  
  return ret;
}

int main()
{
  int T;
  cin >> T;
  
  for(int i = 0; i < T; i++)
  {
    cout << "Case #" << (i+1) << ": " << solve() << endl;
  }
  
  return 0;
}

