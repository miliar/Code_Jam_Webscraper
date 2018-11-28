/* -*- c++ -*-
   ID: dirtysalt
   PROG: 
   LANG: C++
   copy[write] by dirlt(dirtysalt1987@gmail.com) */
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstring>

#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <deque>
#include <map>
#include <numeric>
#include <algorithm>

using namespace std;
typedef long long LL;
typedef vector < int >VI;
typedef vector < string > VS;
typedef vector < double >VD;
typedef pair < int, int >PII;
#define SZ(v) ((int)((sizeof(v))/sizeof(*(v))))
#define PV(v) do {						\
    cout<<#v<<endl;						\
    for(int i=0;i<(int)(v).size();i++)cout<<(v)[i]<<" ";	\
    cout<<endl; \
  }while(0)
#define PA(v) do{							\
    cout<<#v<<endl;							\
    for(int i=0;i<(int)(sizeof(v)/sizeof(*(v)));i++)cout<<(v)[i]<<" ";	\
    cout<<endl;								\
  }while(0)
#define FUNC() do{					\
    cout<<"=========="<<__func__<<"=========="<<endl;	\
  }while(0)

#define TRIEN 750000
struct trie
{
  trie *next[26];
};
trie nodes[TRIEN+1];/* for root node */
trie *new_node()
{
  static int nodesn=0;
  trie *res=&(nodes[nodesn++]);
  for(int i=0;i<26;i++)res->next[i]=NULL;
  return res;
}
void insert_trie(trie *root,const char *str)
{
  trie *p=root;
  for(int i=0;str[i]!=0;i++){
    char ch=str[i];
    if(p->next[ch-'a']==NULL){
      trie *c=new_node();
      p->next[ch-'a']=c;
    }
    p=p->next[ch-'a'];
  }
  return ;
}

#define LN 20
int L,D,N;
vector<char>option[LN];
char dfs_s[LN];
int cnt;
void dfs(trie *p,int i)
{
  if(i==L){
    cnt++;
    return ;
  }else{
    for(int j=0;j<(int)option[i].size();j++){
      char ch=option[i][j];
      if(p->next[ch-'a']==NULL)continue;
      dfs(p->next[ch-'a'],i+1);
    }
  }
  return ;    
}

int main()
{
  string s;
  scanf("%d %d %d",&L,&D,&N);
  trie *root=new_node();
  for(int i=0;i<D;i++){
    cin>>s;
    insert_trie(root,s.c_str());
  }
  
  for(int i=0;i<N;i++){
    for(int j=0;j<LN;j++)option[j].clear();
    int status=0;
    int l=0;
    cin>>s;
    //cout<<s<<endl;
    for(int j=0;j<(int)s.length();j++){
      if(s[j]=='('){
	status=1;
      }else if(s[j]==')'){
	status=0;
	l++;
      }else{
	if(status==0)option[l++].push_back(s[j]);
	else option[l].push_back(s[j]);
      }
    }
    /*
    for(int j=0;j<L;j++){
      for(int k=0;k<(int)option[j].size();k++)
	putchar(option[j][k]);
      putchar('\n');
    }
    */
    cnt=0;
    dfs(root,0);
    printf("Case #%d: %d\n",i+1,cnt);
  }
  return 0;
}
