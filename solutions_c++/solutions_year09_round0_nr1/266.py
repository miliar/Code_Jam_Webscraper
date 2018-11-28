#include<cstdio>
#include<cstring>
#include<vector>
using namespace std;
char dict[7777];
int l;
struct trie{
  bool b[5000*15];
  int trielen,next[5000*15][26];
  void init(){
    trielen=1;
    memset(b,0,sizeof(b));
    memset(next,0,sizeof(next));
  }
  void insert(char*a){
    int p=1;
    for(;*a;++a){
      if(!next[p][*a-97])
        next[p][*a-97]=++trielen;
      p=next[p][*a-97];
    }
    b[p]=1;
  }
}tr;
vector<vector<char> >vec;
int dfs(int p,int i){
  if(i==l)return 1;
  int j,sum=0;
  for(j=0;j<vec[i].size();++j){
    if(tr.next[p][vec[i][j]-97])
      sum+=dfs(tr.next[p][vec[i][j]-97],i+1);
  }
  return sum;
}
int main(){
  tr.init();
  int d,n;
  scanf("%d%d%d",&l,&d,&n);
  while(d--){
    scanf("%s",dict);
    tr.insert(dict);
  }
  int testi;
  for(testi=1;testi<=n;++testi){
    vec=vector<vector<char> >();
    scanf("%s",dict);
    char*p=dict;
    for(;*p;++p){
      vector<char>temp;
      if(*p-'('){
        temp.push_back(*p);
        vec.push_back(temp);
      }
      else{
        ++p;
        while(*p-')'){
          temp.push_back(*p);
          ++p;
        }
        vec.push_back(temp);
      }
    }
    int i,j;
    /*for(i=0;i<vec.size();++i){
      for(j=0;j<vec[i].size();++j)
        putchar(vec[i][j]);
      putchar('\n');
    }
    putchar('\n');*/
    printf("Case #%d: %d\n",testi,dfs(1,0));
  }
  return 0;
}