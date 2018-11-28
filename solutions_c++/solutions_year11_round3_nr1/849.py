#include<cstdio>

using namespace std;

int main(){
  int T;
  scanf("%d\n",&T);
  for(int test=1;test<=T;test++){
    int R,C;
    scanf("%d%d\n",&R,&C);
    char table[60][60];
    for(int i=0;i<=R;i++)
      for(int j=0;j<=C;j++)
	table[i][j]='.';
    for(int i=0;i<R;i++)
      scanf("%s\n",table[i]);

    bool ans = true;
    for(int i=0;i<R&&ans;i++){
      for(int j=0;j<C&&ans;j++){
	if(table[i][j]=='#'){
	  if(table[i][j+1]=='#'&&table[i+1][j]=='#'&&table[i+1][j+1]=='#'){
	    table[i][j]=table[i+1][j+1]='/';
	    table[i+1][j]=table[i][j+1]='\\';
	  }else{
	    ans=false;
	  }
	}
      }
    }
    printf("Case #%d:\n",test);
    if(ans){
      for(int i=0;i<R;i++)
	puts(table[i]);
    }else{
      puts("Impossible");
    }
  }
}
