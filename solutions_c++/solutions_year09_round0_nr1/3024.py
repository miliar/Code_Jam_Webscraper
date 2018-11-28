#include <cstdio>
#include <set>
using namespace std;

char words[5010][50];

int main()
{
  int n, d, l;
  scanf("%d%d%d\n", &l, &d, &n);
  
  for(int i=0; i<d; i++){
    scanf("%s\n", words[i]);
  }

  for(int i=0; i<n; i++){
    char ch;
    set <char> pat[100];
    int p=0;
    bool innermode=false;
    while(true){
      scanf("%c", &ch);
      if(ch=='\n') break;
      else if(ch=='(')
	innermode = true;
      else if(ch==')'){ 
	innermode = false;
	p++;
      }
      else{
	pat[p].insert(ch);
	//printf("p=%d ch=%c\n", p, ch);
	if(!innermode) p++;
      }
    }

    int matches = 0;
    for(int j=0; j<d; j++){
      bool ismatch = true;
      for(int k=0; k<l; k++){
	if(pat[k].find(words[j][k]) == pat[k].end()){
	  ismatch = false;
	  break;
	}
      }
      if(ismatch) matches++;
    }

    printf("Case #%d: %d\n", i+1, matches);
  }
  return 0;
}
