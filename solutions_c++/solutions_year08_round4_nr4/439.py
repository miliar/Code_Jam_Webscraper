#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <stack>
#include <queue>

#define f(x,y) for(int x=0; x<(y); ++x)
#define MAX 1005
using namespace std;
int N, K;
char S[MAX];
int perm(int n, vector<int> &p);
int main(){
  scanf("%d", &N);
  f(t, N){
    scanf("%d", &K);
    while(getchar()!='\n');
    cin.getline(S, MAX);
    vector<int> p;
    printf("Case #%d: %d\n", t+1, perm(0, p));
  }
  return 0;
}

int perm(int n, vector<int> &p){
  if(n<K){
    int val=INT_MAX;
    int *arr=new int[K+1];
    for(int i=1; i<=K; ++i) arr[i]=0;
    for(int i=0; i<p.size(); ++i)
      arr[p[i]]=1;
    for(int i=1; i<=K; ++i){
      if(arr[i]==0){
	p.push_back(i);
	int x=perm(n+1, p);
	if(x<val) val=x;
	p.pop_back();
      }
    }
    delete arr;
    return val;
  }
  else{
    char S1[MAX];
    int i;
    int val=1;
    for(i=0; S[i]!='\0';){
      int j;
      for(j=0; j<K; ++j){
	S1[i+j]=S[i+(p[j]-1)];
      }
      i+=j;
    }
    S1[i]='\0';
    //for(int i=0; i<p.size(); ++i) printf("%d ", p[i]);
    //printf("\n");
    //printf("%s\n", S1);
    for(int i=1; S1[i]!='\0'; ++i)
      if(S1[i]!=S1[i-1]) val++;
    return val;
  }
  return 0;
}

    
	
