#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <vector>
#include <string>
using namespace std;

int main()
{
  int cases;
  scanf("%d\n", &cases);
  for(int t=0; t<cases; t++){
    printf("Case #%d: ", t+1);
    char str[100];
    scanf("%s\n", str);
    int n = strlen(str);
    if(next_permutation(str, str+n)){
      printf("%s\n", str);
    }
    else{
      sort(str, str+n);
      for(int i=0; i<n; i++)
	if(str[i]!='0'){ swap(str[i], str[0]); break; }
      printf("%c0%s\n", str[0], str+1);
    }
  }
  return 0;
}
