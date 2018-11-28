#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>
#include <string>

using namespace std; 

const int MAXN = 2000001; 

int color[MAXN]; 
int head[MAXN]; 

int solve(int l, int r){
  int ret = 0; 
  memset(head, 0, sizeof(head)); 
  for (int i = l; i<=r; ++i) {
    ret += head[color[i]]; 
    ++head[color[i]]; 
  }
  return ret; 
}

void init(){
  memset(color, 0, sizeof(color)); 
  for (int i = 1; i<MAXN; ++i) {
    char st[10]; 
    sprintf(st, "%d", i); 
    string num(st); 
    color[i] = i; 
    for (int j = 1; j<num.size(); ++j) 
      if (st[j]!='0'){
	string new_num = num.substr(j, num.size()-j)+num.substr(0, j); 
	int k; 
	sscanf(new_num.c_str(), "%d", &k); 
	if (k<i) {
	  color[i] = color[k]; 
	  break; 
	}
      }
      
  }
}

int main(){
  int T; 
  scanf("%d", &T); 
  init(); 
  for (int i = 1; i<=T; ++i) {
    int A, B; 
    scanf("%d%d", &A, &B); 
    printf("Case #%d: %d\n", i, solve(A, B)); 
  }
  
  return 0; 
}
