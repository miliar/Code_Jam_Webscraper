#include <iostream>
#include <cstdio>
#include <string>
#define MAXN 105
using namespace std;

int testcase,N;
string A;
char S[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main(){
  freopen("A-small-attempt0.in","r",stdin);
  freopen("ans.out","w",stdout);
  scanf("%d",&testcase);
  cin.ignore();
  for(int TC=1;TC<=testcase;++TC){
    getline(cin,A);
    N = A.length();
    printf("Case #%d: ",TC);
    for(int i=0;i<N;++i)
      if(A[i] == ' ') printf(" ");
      else printf("%c",S[A[i]-'a']);
    printf("\n");
  }
}
