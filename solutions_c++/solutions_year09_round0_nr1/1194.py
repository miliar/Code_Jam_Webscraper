#include <cstdio>
#include <set>
#include <vector>
#include <string>
using namespace std;

int main() {
  int L,D,N;
  string strs[5010];
  char buff[1000];
  scanf("%d%d%d",&L,&D,&N);
  for(int d=0;d<D;++d) {
    scanf(" %s",buff);
    strs[d]=string(buff);
  }
  for(int n=0;n<N;++n) {
    scanf(" %s",buff);
    set<char> pattern[20];
    int i=0;
    for(int l=0;l<L;++l) {
      if(buff[i]=='(') {
	i++;
	while(buff[i]!=')')
	  pattern[l].insert(buff[i++]);
	i++;
      }
      else pattern[l].insert(buff[i++]);
    }
    int num=0;
    for(int d=0;d<D;++d) {
      bool ok=true;
      for(int l=0;l<L && ok;++l) {
	if(pattern[l].count(strs[d][l])==0)
	  ok=false;
      }
      if(ok) ++num;
    }
    printf("Case #%d: %d\n",n+1,num);
  }
}
