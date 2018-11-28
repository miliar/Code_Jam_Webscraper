/*
  Input from stdin, output to stdout
 */

#include <cstdio>
#include <string>
#include <iostream>
#include <map>
#include <cassert>
using namespace std;

int main()
{
  int N;
  scanf("%d", &N);
  for(int t=1; t<=N; t++){
    int S, Q;
    map <string, int> M; 
    bool seen[101]={0};
    int num_seen=0, ans=0;
    string s;

    scanf("%d\n", &S);
    for(int i=0; i<S; i++){
      getline(cin, s);
      //printf("x=%s\n", s.c_str());
      M[s]=i;
    }
    scanf("%d\n", &Q);
    for(int i=0; i<Q; i++){
      getline(cin, s);
      int x=M[s];
      assert(x<S);
      if(!seen[x]){
	seen[x]=true;
	num_seen++;
      }
      if(num_seen==S){
	fill(seen, seen+S, false);
	num_seen=1; seen[x]=true;
	ans++;
      }
    }
    printf("Case #%d: %d\n", t, ans);
  }
  return 0;
}
