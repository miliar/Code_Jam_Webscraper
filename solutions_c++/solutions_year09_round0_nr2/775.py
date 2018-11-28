#include<cstdio>
#include<string>

#define INF 100000

using namespace std;

int tabla[128][128];
int sink[128][128];
char ime[30];
int brSink;
int dx[4]={-1, 0, 0, 1};
int dy[4]={0, -1, 1, 0};
int r,s;

int rek(int x,int y)
{
  int min=INF;
  int px,py;
  if( sink[x][y]!=0) return sink[x][y];
  
  for(int i=0;i<4;i++)
  {
    int nx=x+dx[i]; int ny=y+dy[i];
    if( nx>= 0 && nx<r && ny>=0 && ny<s )
      if(tabla[nx][ny] < min) 
        {
          min = tabla[nx][ny];
          px=nx; py=ny;
        }
  }
  
  if(tabla[x][y] <= min) 
  {
    sink[x][y]=brSink; 
    brSink++;
  }
  else sink[x][y] = rek(px, py);
  
  return sink[x][y];      
}

int main()
{
  int ntp;
  scanf("%d",&ntp);
  
  for(int tp=0;tp<ntp;tp++)
  {
    scanf("%d %d",&r,&s);
    for(int i=0;i<r;i++)
    {
      for(int j=0;j<s;j++) scanf("%d",&tabla[i][j]);
    }
    brSink=1;
    memset(sink, 0, sizeof(sink));
    for(int i=0;i<r;i++)
      for(int j=0;j<s;j++)
        if(sink[i][j]==0) rek(i,j);
    
    memset(ime, 0, sizeof(ime));
    char brIme='a';
    for(int i=0;i<r;i++)
      for(int j=0;j<s;j++)
        if( ime[sink[i][j]] == 0 ) 
        {
          ime[ sink[i][j] ] = brIme;
          brIme++;
        }
    printf("Case #%d:\n", tp+1);
    for(int i=0;i<r;i++)
    {
      for(int j=0;j<s;j++)
      {
        if(j) printf(" ");
        printf("%c", ime[ sink[i][j] ] );
      }
      printf("\n");
    }   
    
  }
  return 0;
}
