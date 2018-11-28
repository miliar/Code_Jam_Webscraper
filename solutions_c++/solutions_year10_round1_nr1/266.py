#include <cstdio>

#define MAX_N 100

char org_board[MAX_N + 1][MAX_N + 10];
char board[MAX_N + 1][MAX_N + 1];
int n,k;

void read_input()
{
  scanf("%d %d",&n,&k);
  for(int i=0; i<n; i++)
    scanf("%s",org_board[i]);
}

void print_board()
{
  for(int i=0; i<n; i++)
    printf("%s\n", board[i]);
  printf("-----------\n");
}

char blocks[MAX_N+1];

void fall(int col)
{
  int c = 0;

  for(int i=n-1; i>=0; i--)
    if(board[i][col]!='.') {
      blocks[c] = board[i][col];
      c++;
    }
  
  for(int i=0; i<n; i++)
    board[i][col] = '.';

  for(int i=0; i<c; i++)
    board[n-i-1][col] = blocks[i];
}

void copy_to_org()
{
  for(int i=0; i<n; i++)
    for(int j=0; j<n; j++)
      org_board[i][j] = board[i][j];
}

void rotate_board()
{
  // rotate
  for(int i=0; i<n; i++) {
    for(int j=0; j<n; j++)
      board[j][n - i - 1] = org_board[i][j];
    board[i][n] = '\0';
  }
}

void compress_board()
{
  for(int i=0; i<n; i++)
    fall(i);
}

void check_and_count(int& max, int& count, char p, char ch)
{
  if(ch==p) {
    count++;
    if(count > max)
      max = count;
  } else {
    count = 0;
  }
}

bool check_row(int r, char p)
{
  int max, c;
  c = 0;
  max = 0;
  for(int i=0; i<n; i++)
    check_and_count(max,c,board[r][i],p);
  return max >= k;
}

bool check_diag(int i, int j, char p)
{
  int max, c;
  c = 0;
  max = 0;
  do {
    check_and_count(max,c,board[i][j],p);
    i++;
    j++;
  } while((i<n) && (j<n));
  return max >= k;
}

bool check1(char p)
{
  for(int i=0; i<n; i++) {
    if(check_row(i,p))
      return true;
  }
  // check diagonal 1
  for(int i=0; i<n; i++) {
    if(check_diag(0,i,p))
      return true;
    if(check_diag(i,0,p))
      return true;
  }
}

bool check(char p)
{
  if(check1(p))
    return true;

  copy_to_org();
  rotate_board();
  if(check1(p))
    return true;
}

main()
{
  int T;
  scanf("%d",&T);
  for(int t=0; t<T; t++) {
    read_input();
    rotate_board();
    compress_board();
    bool rwin = check('R');
    bool bwin = check('B');

    printf("Case #%d: ",t+1);

    if(rwin)
      if(bwin)
	printf("Both\n");
      else
	printf("Red\n");
    else
      if(bwin)
	printf("Blue\n");
      else
	printf("Neither\n");
  }
}
