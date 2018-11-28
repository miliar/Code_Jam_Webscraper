#include <cstdio>

#define MAX_R 100
#define MAX_C 100

int r,c;
char map[MAX_R][MAX_C];

void read_input()
{
  char b[MAX_C];

  scanf("%d %d",&r,&c);
  for(int i=0; i<r; i++) {
    scanf("%s",&map[i+1][1]);
    map[i+1][0] = '.';
    map[i+1][c+1] = '.';
    map[i+1][c+2] = '\0';
  }
  for(int i=0; i<c+2; i++) {
    map[0][i]= '.';
    map[r+1][i]='.';
  }
  r++; c++;
}

int deal()
{
  for(int i=0; i<r; i++)
    for(int j=0; j<c; j++)
      if(map[i][j]=='#') {
	if((map[i+1][j]!='#') ||
	   (map[i][j+1]!='#') ||
	   (map[i+1][j+1]!='#')) {
	  return -1;
	}
	map[i][j]='/';
	map[i+1][j]='\\';
	map[i][j+1]='\\';
	map[i+1][j+1]='/';
	return 1;
      }
  return 0;
}

void solve(int t)
{
  printf("Case #%d:\n",t);
  read_input();
  int res;
  while((res=deal())!=0) {
    if(res==-1) {
      printf("Impossible\n");
      return;
    }
  }
  for(int i=1; i<=r-1; i++) {
    map[i][c]='\0';
    printf("%s\n",map[i]+1);
  }
}

main()
{
  int t;
  scanf("%d",&t);
  for(int tt=0; tt<t; tt++)
    solve(tt+1);
}
