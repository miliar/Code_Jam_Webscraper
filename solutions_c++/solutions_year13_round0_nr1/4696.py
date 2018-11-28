#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>

#define CodeJam_main main

int CheckWhoWin(char a[4][4],char x)
{
  int b = 0;
  int m,n;

  for(m = 0;m<4;m++)
    {
      for(n = 0;n<4;n++)
        {
          if(a[m][n] == x || a[m][n] == 'T')
            b |= 1<<n;
        }
      if(b == 15) 
        return 1;
      b = 0;
    }

  b = 0;
  for(n = 0;n<4;n++)
    {
      for(m = 0;m<4;m++)
        {
          if(a[m][n] == x || a[m][n] == 'T')
            b |= 1<<m;
        }
      if(b == 15)
        return 1;
      b = 0;
    }
  
  for(m = 0;m<4;m++)
    {
      if(a[m][m] == x || a[m][m] == 'T')
        b |= 1<<m;
    }
  if(b == 15)
    return 1;
  b = 0;

  for(m = 0;m<4;m++)
    {
      if(a[3 - m][m] == x || a[3 - m][m] == 'T')
        b |= 1<<m;
    }
  if(b == 15)
    return 1;
  b = 0;

  return 0;
}


int CodeJam_main(int argc,char **argv) 
{ 
#ifdef FILEIO
	freopen("2013CodeJam_in.txt","r",stdin); 
	freopen("2013CodeJam_out.txt","w",stdout); 
#endif

	int T;
	int N;

        int i;
        int m,n;
        char tchar;
        char a[4][4];
        int b = 0;
        scanf("%d",&T);
        scanf("%c",&tchar);
        
        for(i = 1;i <= T;i++)
          {
            memset(a,0,16*sizeof(char));
            b = 0;
            for(m = 0;m<4;m++)
              {
                for(n = 0;n<4;n++)
                  {
                    scanf("%c",&a[m][n]);
                    switch(a[m][n])
                      {
                      case 'X':
                      case 'T':
                      case 'O':
                        b |= 1<<(4*m + n);
                        break;
                      }
                  }
                scanf("%c",&tchar);
              }
			scanf("%c",&tchar);

            if(CheckWhoWin(a,'X') == 1)
                printf("Case #%d: X won\n",i);
            else if(CheckWhoWin(a,'O') == 1) 
                printf("Case #%d: O won\n",i);
			else if (b == 65535)
				printf("Case #%d: Draw\n",i);
            else
                printf("Case #%d: Game has not completed\n",i);
          }


#ifdef FILEIO
	fclose(stdin);
	fclose(stdout);
#endif

	return 0; 
} 
