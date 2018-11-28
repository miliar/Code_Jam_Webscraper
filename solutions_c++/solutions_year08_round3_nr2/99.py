#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <stack>
#include <queue>
#include <string>

#define f(x,y) for(int x=0; x<(y); ++x)
using namespace std;
void eval(int n, vector<string>& w);
int N;
char w[100];
int main(){
  scanf("%d", &N);
  while(getchar()!='\n');
  f(t, N){
    cin.getline(w, 100);    
    //printf("%s!%d\n", w, strlen(w));
    vector<string> W;
    eval(strlen(w)-1, W);
    if(strlen(w)==1){
      if((w[0]-'0')%2==0 || (w[0]-'0')%3==0 || (w[0]-'0')%5==0 || (w[0]-'0')%7==0)
	    printf("Case %d: %d\n", t+1, 1);
      else  printf("Case %d: %d\n", t+1, 0);
      cerr<<t+1<<"..done"<<endl;
      continue;
    }
    long long int ans=0;
    for(int i=0; i<W.size(); ++i){
      long long int res=w[0]-'0';
      long long int old=0;
      //printf("%s\n", W[i].c_str());
      for(int j=0; j<W[i].size(); ++j){
	if(W[i][j]=='0') res=res*10+(w[j+1]-'0');
	if(W[i][j]=='+'){
	  old+=res;
	  res=w[j+1]-'0';
	} 
	if(W[i][j]=='-'){
	  old-=res;
	  res=w[j+1]-'0';
	}
      }
      old+=res;
      if(old%2==0 || old%3==0 || old%5==0 || old%7==0){
	ans++;
	//printf(" %d Corr", old);
      }
    }
    printf("Case %d: %lld\n", t+1, ans);
    cerr<<t+1<<"..done"<<endl;
  }
  return 0;
}

void eval(int n, vector<string>& w){
  w.push_back("-");
  w.push_back("+");
  w.push_back("0");
  for(int i=0; i<n-1; ++i){
    vector<string> q(w);
    w.clear();
    for(int i=0; i<q.size(); ++i)
      w.push_back(q[i]+"-");
    for(int i=0; i<q.size(); ++i)
      w.push_back(q[i]+"+");
    for(int i=0; i<q.size(); ++i)
      w.push_back(q[i]+"0");
  }
  
}
