#include<cstdio>
#include<map>
#include<string>
#include<vector>
using namespace std;
char cmd[111111];
vector<map<string,int> >vm;
vector<string>vs;
void print(vector<string>&vs){
  int i;
  for(i=0;i<vs.size();++i)
    puts(vs[i].c_str());
}
void getvs(char*p){
  string tmp;
  vs.clear();
  for(p=cmd+1;*p;++p){
    if(*p-'/')tmp+=*p;
    else{
      vs.push_back(tmp);
      tmp="";
    }
  }
  if(*(p-1)-'/')
    vs.push_back(tmp);
}
void dfs(int i,int k,int&cnt){
  if(k==vs.size())return;
  int&ref=vm[i][vs[k]];
  if(!ref){
    ref=vm.size();
    vm.resize(vm.size()+1);
    ++cnt;
  }
  dfs(ref,k+1,cnt);
}
int main(){
  int test;
  scanf("%d",&test);
  int testi;
  for(testi=1;testi<=test;++testi){
    vm.clear();
    vm.resize(1);
    int n,m;
    scanf("%d%d",&n,&m);
    while(n--){
      scanf("%s",cmd);
      getvs(cmd);
      //print(vs);
      int cnt;
      dfs(0,0,cnt);
    }
    int cnt=0;
    while(m--){
      scanf("%s",cmd);
      getvs(cmd);
      //print(vs);
      dfs(0,0,cnt);
    }
    printf("Case #%d: %d\n",testi,cnt);
  }
  return 0;
}