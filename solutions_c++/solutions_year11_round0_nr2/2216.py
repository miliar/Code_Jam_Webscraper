#include <cstdio>
#include <cstring>
#include <cctype>

int combine[26][26];
bool opposed[26][26];

int ls[200];
int ln;

int cnt[26];

int main ()
{
  int cases,index; scanf("%d",&cases);
  for(index=0;index<cases;index++)
  {
    int n;
    int cn;scanf("%d",&cn);
    memset(combine,0xff,sizeof(combine));
    for(int i = 0; i < cn; i ++ )
    {
      char s[10];
      scanf("%s",s);
      int a = s[0]-'A';
      int b = s[1]-'A';
      int c = s[2]-'A';
      combine[a][b]=combine[b][a]=c;
    }
    int on;scanf("%d",&on);
    memset(opposed,0,sizeof(opposed));
    for(int i = 0; i < on; i ++ )
    {
      char s[10];
      scanf("%s",s);
      int a = s[0]-'A';
      int b = s[1]-'A';
      opposed[a][b] = opposed[b][a] = 1;
    }
    scanf("%d",&n);
    char inv[200];
    scanf("%s",inv);
    ln = 0;
    for(int i = 0; i < n; i ++ )
    {
      ls[ln++]=inv[i]-'A';
      while( ln >= 2 && combine[ls[ln-1]][ls[ln-2]]!=-1 )
      {
	int t = combine[ls[ln-1]][ls[ln-2]];
	ln -- ;
	ln -- ;
	ls[ln++] = t;
      }
      memset(cnt,0,sizeof(cnt));
      for(int j = 0; j < ln; j ++ )
      {
	cnt[ls[j]] ++ ;
      }
      bool flag = false;
      for(int p = 0; p < 26 && !flag; p ++ ) if( cnt[p] )
					       for(int q = 0; q < 26 && !flag ; q ++ ) if( cnt[q] ) 
	  if( opposed[p][q] ) flag = true;
      if( flag ) ln = 0;
    }
    printf("Case #%d: [",index+1);
    for(int i = 0; i < ln; i ++ )
    {
      if(i) printf(", ");
      putchar(ls[i]+'A');
    }
    printf("]\n");
  }
  return 0;
}
