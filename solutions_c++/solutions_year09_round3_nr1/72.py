#include <cstdio>
#include <string>
#include <map>
#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
  int cases;
  scanf("%d", &cases);
  for(int cas=0; cas<cases; cas++){
    printf("Case #%d: ", cas+1);
    string S;
    cin>>S;

    int base=0;
    map <char, int> M;
    for(int i=0; i<S.size(); i++){
      if(M.find(S[i]) == M.end()){
	int v;
	if(base==0) v=1;
	else if(base==1) v=0;
	else v=base;
	M[S[i]]=v;
	base++;
      }
    }

    if(base == 1) base=2;

    long long ans=0;

    for(int i=0; i<S.size(); i++){
      ans=ans*base+M[S[i]];
    }

    printf("%Ld\n", ans, base);
  }
}
