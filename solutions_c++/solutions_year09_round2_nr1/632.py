#include<cctype>
#include<cstdio>
#include<set>
#include<string>
using namespace std;
struct tree{
  double weight;
  string feature;
  tree(){
    feature="";
  }
}tr[7777];
char*p,cmd[77777],tcmd[77777];
set<string>sett;
void dfs(int i){
  tr[i]=tree();
  while(*p){
    while(*p==' ')++p;
    if(isdigit(*p)){
      sscanf(p,"%lf",&tr[i].weight);
      while(isdigit(*p)||*p=='.')++p;
    }
    while(*p==' ')++p;
    if(*p==')'){++p;return;}
    if(isalpha(*p)){
      sscanf(p,"%s",tcmd);
      tr[i].feature=tcmd;
      while(isalpha(*p))++p;
    }
    while(*p==' ')++p;
    if(*p=='('){
      ++p;
      dfs(2*i+1);
    }
    while(*p==' ')++p;
    if(*p=='('){
      ++p;
      dfs(2*i+2);
    }
  }
}
void print(int i){
  printf("%f %s\n",tr[i].weight,tr[i].feature.c_str());
  if(!tr[i].feature.size())return;
  print(2*i+1);
  print(2*i+2);
}
double ans;
void fun(int i){
  //printf("sett.size%d i%d %s",sett.size(),i,tr[i].feature.c_str());
  ans*=tr[i].weight;
  if(tr[i].feature=="")return;
  if(sett.find(tr[i].feature)==sett.end())
    fun(i*2+2);
  else fun(i*2+1);
}
int main(){
  int test;
  scanf("%d",&test);
  int testi;
  for(testi=1;testi<=test;++testi){
    int l;
    scanf("%d",&l);
    gets(cmd);
    p=cmd;
    while(l--){
      gets(p);
      while(*p)++p;
    }
    //puts(cmd);
    p=cmd;
    while(*p-'(')++p;
    ++p;
    dfs(1);
    //print(1);
    int a;
    scanf("%d",&a);
    printf("Case #%d:\n",testi);
    while(a--){
      scanf("%s",cmd);
      int n;
      scanf("%d",&n);
      sett.clear();
      while(n--){
        scanf("%s",cmd);
        sett.insert(cmd);
      }
      ans=1;
      fun(1);
      printf("%.7f\n",ans);
      //set<string>::iterator ite;for(ite=sett.begin();ite!=sett.end();++ite)puts(ite->c_str());
    }
  }
  return 0;
}