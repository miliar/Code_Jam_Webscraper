#include <iostream>
#include <string.h>
#include <stdio.h>
using namespace std;


const int maxl = 15, maxd = 5000, maxn = 500;

char Dic[maxd][maxl + 5];
char pattern[maxn];
int patternMap[maxl][26];
int l,d, n;

void InitPatternMap()
{
     int patternLen = strlen(pattern);
     int cur = 0;
     for(int i = 0; i < l; ++i)
             for(int j = 0; j < 26; ++j)
                     patternMap[i][j] = 0; 
     for(int i = 0; i < patternLen; ++i)
     {
             if(pattern[i] == '(')
             {
                           ++i;
                           while(pattern[i] != ')')
                           {
                                patternMap[cur][pattern[i] - 'a'] = 1;    
                                ++i;                    
                           }
                           cur++;
                           continue;
             }
             if(pattern[i] == ')')
                           continue;
             

             patternMap[cur++][pattern[i] - 'a'] = 1;
             
     }
}

void InitDic()
{
     for(int i = 0; i < d; ++i)
             cin >> Dic[i];
}
bool IsMatched(char *str)
{
     for(int i = 0; i < l; ++i)
     {
             if(patternMap[i][str[i]-'a'] != 1)
                                       return false;
     }
     return true;
}
int main()
{
     freopen("a_out.txt","w",stdout);
     freopen("A-large.in","r", stdin);
     
    cin >> l >> d >> n;
    InitDic();
    for(int i = 1; i <= n; ++i)
    {
            cin >> pattern;
            InitPatternMap();
            int num = 0;
            for(int j = 0 ; j < d; ++j)
            {
                    if(IsMatched(Dic[j]))
                                         ++num;
            }
            printf("Case #%d: %d\n", i, num);
            
    }
    return 0;
}


