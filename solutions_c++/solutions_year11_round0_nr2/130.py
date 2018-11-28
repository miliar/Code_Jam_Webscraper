#include<cstdio>
#include<algorithm>
#include<cstring>
#include<string>
#include<iostream>
#include<queue>
#include<stack>
using namespace std;

inline int Rint(){int x; scanf("%d", &x); return x;}
#define out(x) cout <<#x<< ": " << x << endl;

int n;
int hash[1 << 10];
char comb[10][10];bool oppo[10][10];
char s[100 + 10];
void work()
{
     
     int tail = 0;
     char ans[100 + 10];
     for( int i = 0; i < n; ++ i )
     {
          ans[tail ++] = s[i];
          while( tail >= 2 )
          {
                int s = hash[ans[tail - 2]];
                int t = hash[ans[tail - 1]];
                
                if( s != -1 && t != -1 && comb[s][t] != -1 )
                {
                    tail -= 2;
                    ans[tail ++] = comb[s][t];
                }
                else
                {
                    for( int i = 0; i < tail - 1; ++ i )
                    {
                         int s = hash[ans[i]];
                         int t = hash[ans[tail - 1]];             
                         if( s != -1 && t != -1 && oppo[s][t]) tail = 0;
                    }
                    break;
                }
          }
     }
     if( !tail )
     {
          puts("[]");return ;
     }
     printf("[%c", ans[0]);
     for( int i = 1; i < tail; ++i )
          printf(", %c", ans[i]);
     puts("]");
}
int main()
{
    memset(hash, 0xff, sizeof(hash));
    hash['Q'] = 0;
    hash['W'] = 1;
    hash['E'] = 2;
    hash['R'] = 3;
    //-----------
    hash['A'] = 4;
    hash['S'] = 5;
    hash['D'] = 6;
    hash['F'] = 7;
    int Tcase = Rint();
    while(  Tcase -- )
    {
          memset(comb, 0xff, sizeof(comb));
          int c = Rint();
          while( c -- )
          {
                char str[5];
                scanf("%s", str);
                int s = hash[str[0]];
                int t = hash[str[1]];
                comb[s][t] = comb[t][s] = str[2];
          }
          memset(oppo, false, sizeof(oppo));
          int d = Rint();
          while( d -- )
          {
                char str[5];
                scanf("%s", str);
                int s = hash[str[0]];
                int t = hash[str[1]];
                oppo[s][t] = oppo[t][s] = true;
          }
          n = Rint();
          scanf("%s", s);
          static int o = 1;
          printf("Case #%d: ", o ++);
          work();
    }
    return 0;
}

