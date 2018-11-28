#include <algorithm>
#include <stdio.h>
#include <stack>
#include <queue>
#include <vector>
#include <string>
#include <map>
#include <set>
using namespace std;
int a;
int h=0;
char st[10000000];
int flag[30];
int fr[30][30];
int bad[30][30];
char pal[1000000];


void mete(char c)
{
    if(h==0)
    {
     //   printf("FR\n");
       st[h++]   =c;
       flag[c]++;
       return;
    }
    if(  fr[c][st[h-1]]!=-1 )
    {
   //     printf("FR\n");
      flag[ st[h-1] ]--;
      h--;
      mete(fr[c][st[h]]);
      return;
    }
    for(int r=0;r<30;r++)
     if( bad[r][c] && flag[ r ] )
      {
        h=0;
        memset(flag,0,sizeof(flag)) ;
        return ;
      }
    //  printf("NOR\n");
      st[h++]   =c;
       flag[c]++;
}

int main()
{
  int N;
  freopen("in.txt","r",stdin);
  freopen("out.txt","w",stdout);
  scanf("%d",&N);
  for(int _r=0;_r<N;_r++)
   {
     int n;
     for(int r=0;r<30;r++) for(int c=0;c<30;c++) fr[r][c]=-1;
     h=0;
     memset(flag,0,sizeof(flag)) ;
     memset(bad,0,sizeof(bad)) ;
     scanf("%d",&n);
     for(int r=0;r<n;r++)
      {
        scanf("%s",pal);
        fr[pal[0]-'A'][pal[1]-'A']=pal[2]-'A';
        fr[pal[1]-'A'][pal[0]-'A']=pal[2]-'A';
      }
     scanf("%d",&n);
     for(int r=0;r<n;r++)
      {
        scanf("%s",pal);
        bad[pal[0]-'A'][pal[1]-'A']=1;
        bad[pal[1]-'A'][pal[0]-'A']=1;
      }
     scanf("%d",&n);
       scanf("%s",pal);
     for(int rr=0;rr<n;rr++)
       mete(pal[rr]-'A');
       printf("Case #%d: [",_r+1);
     for(int r=0;r<h-1;r++)
      printf("%c, ",(st[r]+'A'));
     if(h)printf("%c",(st[h-1]+'A'));
      printf("]\n");
   }
}
