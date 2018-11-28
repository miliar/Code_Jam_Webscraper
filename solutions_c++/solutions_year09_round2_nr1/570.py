#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <map>
#include <algorithm>

using namespace std;

#define MAX 100

typedef unsigned long long u64;

struct tree_node {
  double weight;
  int feature;
  tree_node *left,*right;
};

tree_node pool[100000];
int ptr;

u64 rand_table[1000][256];

inline u64 get_hash(char *str) {
  u64 res=0;
  int l=strlen(str);
  for(int i=0;i<l;++i)
    res^=rand_table[i][str[i]];
  return res;
}

map<u64,int> features;

int n;

inline void skip_blanks(char *&str) {
  while(*str==' ' || *str=='\n')
    ++str;
}

tree_node *parse(char *&str) {
  skip_blanks(str);
  tree_node *res=&pool[ptr++];
  if(*str=='(') {
    ++str;
    skip_blanks(str);
    double w;
    sscanf(str,"%lf",&w);
    while(*str=='.' || (*str>='0' && *str<='9'))
      ++str;
    skip_blanks(str);
    if(*str==')') {
      ++str;
      res->weight=w;
      res->feature=-1;
    }
    else {
      char feature[1000];
      sscanf(str,"%s",feature);
      u64 hash_code=get_hash(feature);
      if(features.find(hash_code)==features.end())
        features.insert(make_pair(hash_code,n++));
      res->weight=w;
      res->feature=features[hash_code];
      while(*str>='a' && *str<='z')
        ++str;
      res->left=parse(str);
      res->right=parse(str);
      skip_blanks(str);
      if(*str==')')
        ++str;
    }
  }
  return res;
}

int exist[100000];

double eval(tree_node *node) {
  double p=node->weight;
  if(node->feature>=0) {
    if(exist[node->feature]) {
      p*=eval(node->left);
    }
    else {
      p*=eval(node->right);
    }
  }
  return p;
}

char str[100000];

inline u64 rand64() {
  return ((u64)rand()) | (((u64)rand())<<15) | (((u64)rand())<<30) | (((u64)rand())<<45) | (((u64)rand())<<60);
}

int main() {
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  for(int i=0;i<1000;++i)
    for(int j=0;j<256;++j)
      rand_table[i][j]=rand64();
  int tests;
  gets(str);
  sscanf(str,"%d",&tests);
  for(int test=1;test<=tests;++test) {
    ptr=0, n=0;
    features.clear();
    int l;
    do {
      str[0]=0;
      gets(str);
    }
    while(!str[0]);
    sscanf(str,"%d",&l);
    char *s=str;
    for(int i=0;i<l;++i) {
      gets(s);
      s+=strlen(s);
    }
    s=str;
    tree_node *root=parse(s);
    printf("Case #%d:\n",test);
    scanf("%d",&l);
    for(int i=0;i<l;++i) {
      scanf("%s",&str);
      memset(exist,0,sizeof(exist));
      int k;
      scanf("%d",&k);
      for(int j=0;j<k;++j) {
        scanf("%s",&str);
        u64 hash_code=get_hash(str);
        if(features.find(hash_code)!=features.end()) {
          exist[features[hash_code]]=1;
        }
      }
      printf("%0.20lf\n",eval(root));
    }
  }
  return 0;
}
