#include<cstdio>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;

int getsegs(string x)
{
  int ret=1;
  for(int i=1; i<x.size(); i++){
    if(x[i]!=x[i-1]) ret++;
  }
  return ret;
}

int main()
{
  int T;
  scanf("%d", &T);
  for(int t=0; t<T; t++){
    char s1[1050];
    int K, best=2000;
    scanf("%d\n%s", &K, s1);
    vector <int> P(K);
    for(int i=0; i<K; i++) P[i]=i;
    string s=s1;
    
    do{
      int j=0; string S;
      while(j<s.size()){
	for(int i=0; i<K; i++) S+=s[j+P[i]];
	j+=K;
      }
      int segs=getsegs(S);
      if(segs < best) best=segs;
    }while(next_permutation(P.begin(), P.end()));
    
    printf("Case #%d: %d\n", t+1, best);
    
  }
  return 0;
}
