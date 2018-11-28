#include <iostream>
#include <string.h>
#include <stdio.h>
using namespace std;

int n;
const int maxn = 500;
char str[maxn + 5];
int strLen = 0;
char *pattern = {"welcome to code jam"};
int patternLen = 0;

int f[50][maxn + 5];

void Init()
{
     for(int i = 0 ;i <= patternLen; ++i)
             for(int j = 0; j <= strLen; ++j)
                     f[i][j] = 0;
     
     for(int j = 0; j <= strLen; ++j)
             f[0][j] = 1;
     
}

void DP()
{
     for(int i =  1; i <= patternLen; ++i)
             for(int j  = 1; j <= strLen; ++j)
                     f[i][j] = (f[i-1][j-1]*((pattern[i-1] == str[j-1])?1:0) + f[i][j-1])%10000;
             
}

int  main()
{
     
     freopen("c_out.txt","w",stdout);
     freopen("C-large.in","r", stdin);
     
     cin >> n;
     gets(str);
     patternLen = strlen(pattern);
     
     
     
     for(int i = 1;i <= n; ++i)
     {
             gets(str);
             strLen = strlen(str);
             Init();
             DP();
             printf("Case #%d: %04d\n", i, f[patternLen][strLen]);
             
     } 
     return 0;
 } 
