#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int m[120][120];
int l[120][120];
int mm[120*120];

int main(void)
{
 int T;
 cin >> T;
 for(int C=0;C<T;C++){
  int H,W;
  cin>>H>>W;
  memset(m,0x7f,sizeof(m));
  for(int y=0;y<H;y++)
  for(int x=0;x<W;x++)
    cin>>m[y+1][x+1];
  for(int y=0;y<H;y++)
  for(int x=0;x<W;x++){
   int xx=x+1,yy=y+1;
   while(1){
    int aN=m[yy-1][xx];
    int aW=m[yy][xx-1];
    int aE=m[yy][xx+1];
    int aS=m[yy+1][xx];
    int alt=min(min(aN,aW),min(aE,aS));
    if(alt>=m[yy][xx])break;
    if(alt==aN)--yy;
    else if(alt==aW)--xx;
    else if(alt==aE)++xx;
    else if(alt==aS)++yy;
   }
   l[y][x] = xx+yy*120;
  }
  memset(mm,0xff,sizeof(mm));
  int next='a';
  printf("Case #%d:\n",C+1);
  for(int y=0;y<H;y++){
   for(int x=0;x<W;x++){
    int ll=l[y][x];
    if(mm[ll]<0){mm[ll]=next++;}
    putchar(mm[ll]);
    if(x<W-1) putchar(' ');
   }
   putchar('\n');
  }
 }
 return 0;
}
