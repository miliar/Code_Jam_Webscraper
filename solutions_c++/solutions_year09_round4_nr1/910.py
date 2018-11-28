#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <sstream>
#include <algorithm>

using namespace std;

typedef pair <int, int> pii;
typedef long long ll;

int main()
{
  int numcases;
  scanf("%d", &numcases);
  for(int cno=0; cno<numcases; cno++){
    printf("Case #%d: ", cno+1);
    
    int A[41];
    int N;
    
    scanf("%d\n", &N);
    for(int i=0; i<N; i++){
      A[i]=0;
      for(int j=0; j<N; j++){
	char c;
	scanf("%c ", &c);
	if(c=='1') A[i]=j;
      }
    }
    
    int ret=0;
    for(int i=0; i<N; i++){
      int c=0;
      for(int j=0; j<N; j++){
	if(A[j]<=i){
	  ret+=c;
	  A[j]=50;
	  break;
	}
	if(A[j]<50) c++;
      }
    }

    printf("%d\n", ret);
  }
}
