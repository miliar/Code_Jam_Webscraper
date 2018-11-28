#include <cstdio>
#include <cstring>

char a[60][60];

int T,R,C;

#define ISH(r,c) (a[(r)][(c)] == '#')

int main(){
  scanf("%d", &T);
  for (int ttt=1; ttt<=T; ttt++){
    memset(a, '.', sizeof(a));

    scanf("%d %d", &R, &C);
    for (int r=1; r<=R; r++)
      scanf("%s", a[r]+1);

    printf("Case #%d:\n", ttt);
    for (int r=1; r<=R; r++)
      for (int c=1; c<=C; c++)
	if (a[r][c] == '#'){
	  if (ISH(r+1,c) && ISH(r,c+1) && ISH(r+1,c+1)){
	    a[r][c] = '/';
	    a[r+1][c] = '\\';
	    a[r][c+1] = '\\';
	    a[r+1][c+1] = '/';
	  } else {
	    printf("Impossible\n");
	    goto restart;
	  }
	}
    
    for (int r=1; r<=R; r++){
      for (int c=1; c<=C; c++)
	printf("%c", a[r][c]);
      printf("\n");
    }
  restart:;
  }
}
