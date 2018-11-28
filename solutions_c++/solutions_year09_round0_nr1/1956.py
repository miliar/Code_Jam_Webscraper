#include <string>
using namespace std;
bool poss[500][16][26]; 
char p[500];
char wds[5000][16];
int main()
{
  int L, D, N;
  scanf("%d%d%d", &L, &D, &N);
  for(int i=0;i<D;i++)
     scanf("%s", wds[i]);
  for(int i =0;i<N;i++)
  {
    scanf("%s", p);
    int x = 0;
    int j = 0;
    while(x<L)
    {
     if(p[j]!='(')
      {poss[i][x++][p[j++] - 'a'] = true; continue;}
     j++;
    while(p[j]!=')'){
      poss[i][x][p[j++] - 'a'] = true;
    }
    j++;
    x++;
    }
    int c = D;
    for(int k = 0;k<D;k++)
      for(int t = 0;t<L;t++)
         if(!poss[i][t][wds[k][t]-'a']){c--; break;}
    printf("Case #%d: %d\n", i+1, c);
  }

}
