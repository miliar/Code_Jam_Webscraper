#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
using namespace std;

int L, D, N;

char dic[5001][20];
bool flag[20][26];
char input[500];
int main()
{
    int i, j, len, cur, cnt, casenum = 0;
    bool wishright;
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d%d%d", &L, &D, &N);
    for(i=0; i<D; i++)
    scanf("%s", dic[i]);
    for(casenum = 1; casenum<=N; casenum++)
    {
         memset(flag, 0, sizeof(flag));
         scanf("%s", input);
         len = strlen(input);
         cur = 0; 
         wishright = false;
         for(i=0; i<len; i++)
         {
          if(wishright&&input[i]>='a'&&input[i]<='z')
          {
              flag[cur][input[i]-'a'] = true;
          }else if(!wishright&&input[i]>='a'&&input[i]<='z')
          {
              flag[cur][input[i]-'a'] = true;
              cur++;
          }else if(wishright&&input[i]==')')
          {
                wishright = false;
                cur++;
          }else if(!wishright&&input[i]=='(')
          {
                wishright = true;
          }
         }
         
         cnt = 0;
         for(i=0; i<D; i++)
         {
          for(j=0; j<L; j++)
           if(!flag[j][dic[i][j]-'a']) break;
           if(j>=L)
           cnt++;
         }
         printf("Case #%d: %d\n", casenum, cnt);
    }
    return 0;
}
