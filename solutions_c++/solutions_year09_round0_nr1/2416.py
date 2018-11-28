#include <cstdio>
#include <string>
#include <vector>
#include <cstring>
using namespace std;

char words[5000][20];
bool can[20][256];
int L, D, N;
char pat[100*1000];

int main()
{
  scanf("%d%d%d", &L, &D,&N);
  for(int i=0;i<D;i++) 
    scanf("%s", words[i]);
  
  for(int i=0;i<N;i++) {
    memset(can,0,sizeof(can));
    scanf("%s", pat);
    int pos=0;
    for(int j=0;j<L;j++)
      if(pat[pos]=='(') {
	pos++;
	while(pat[pos]!=')') {
	  can[j][pat[pos]]=1;
	  pos++;
	}
	pos++;
      } else {
	can[j][pat[pos]]=1;
	pos++;
      }
    
    int res=0;
    for(int j=0;j<D;j++) {
      bool tcan = 1;
      for(int k=0;k<L;k++)
	if(!can[k][words[j][k]]) { tcan=0; break; }
      if(tcan) res++;
    }

    printf("Case #%d: %d\n", i+1, res);
  }
  
  return 0;
}
