#include<stdio.h>

char c[40][3];
char d[30][2];
char n[110];

char res[110];
int cnt['Z' - 'A'];

int main()
{
  int t;
  scanf("%d", &t);
  for(int i = 1; i <= t; i++)
  {
    int cc;
    scanf("%d", &cc);
    for(int j = 0; j < cc; j++)
      scanf("%s", c[j]);
      
    int dd;
    scanf("%d", &dd);
    for(int j = 0; j < dd; j++)
      scanf("%s", d[j]);
      
    int nn;
    scanf("%d", &nn);
    scanf("%s", n);
    
    for(int l = 0; l < 'Z' - 'A'; l++)
      cnt[l] = 0;    
    int respos = 0;
    
    for(int j = 0; j < nn; j++)
    {
      char inv = n[j];
      res[respos] = inv;
      cnt[inv - 'A']++;
      
      //combine
      for(int k = 0; k < cc; k++)
      {
        if( (c[k][0] == res[respos] && c[k][1] == res[respos-1]) || (c[k][0] == res[respos-1] && c[k][1] == res[respos]) )
        {
          cnt[res[respos] - 'A']--;
          cnt[res[respos-1] - 'A']--;
          respos--;
          res[respos] = c[k][2];
          cnt[c[k][2] - 'A']++;
          break;
        }
      }
      
      //opposed
      for(int k = 0; k < dd; k++)
      {
        if( (d[k][0] == res[respos] && cnt[d[k][1] - 'A'] > 0) || (d[k][1] == res[respos] && cnt[d[k][0] - 'A'] > 0) )
        {
          for(int l = 0; l < 'Z' - 'A'; l++)
            cnt[l] = 0;
          respos = -1;
          break;
        }
      }
      
      respos++;
    }

    printf("Case #%d: [", i);
    if(respos > 0)
      printf("%c", res[0]);
    for(int j = 1; j < respos; j++)
      printf(", %c", res[j]);
    printf("]\n");
  }
  return 0;
}
