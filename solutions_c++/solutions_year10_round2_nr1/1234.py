#include <iostream>
#include <vector>
using namespace std;

struct Dir{
  string name;
  vector<Dir> dir;
};
vector<Dir> root;
int Ccount;

void myfind(string name, int hie, vector<Dir>& curent, vector<string> parents, int pnum, bool countMode){
  if(hie==0){
    bool f = false;
    for(int i=0; i<curent.size(); i++){
      if(curent[i].name == name){
	f = true;
      }
    }
    if(f==false){
      Dir tmp;
      tmp.name = name;
      //cout << name << endl;
      if(countMode) Ccount++;
      curent.push_back(tmp);
    }
  }else{
    for(int i=0; i<curent.size(); i++){
      if(curent[i].name==parents[pnum]){
	myfind(name, hie-1, curent[i].dir, parents, pnum+1, countMode);
      }
    }
  }
}
void createDir(string dirs, bool countMode){
  int s=1, c=-1;
  vector<string> tmp;
  for(int i=1; i<dirs.length(); i++){
    c++;
    if(dirs[i]=='/'){
      tmp.push_back(dirs.substr(s, c));
      s = i+1;
      c = -1;
    }
  }
  tmp.push_back(dirs.substr(s, c+1));

  for(int i=0; i<tmp.size(); i++){
    myfind(tmp[i], i, root, tmp, 0, countMode);
  }
}


int main(){
  int T;
  int N, M;
  
  cin >> T;
  for(int t=1; t<=T; t++){
    root.clear();
    cin >> N >> M;
    string path;
    for(int n=0; n<N; n++){
      cin >> path;
      createDir(path, false);
    }
    Ccount = 0;
    for(int m=0; m<M; m++){
      cin >> path;
      createDir(path, true);
    }
    cout << "Case #" << t << ": " << Ccount << endl;
    
  }
  return 0;
}
