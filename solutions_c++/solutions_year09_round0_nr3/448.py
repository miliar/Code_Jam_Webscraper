#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

struct node{vector<int> pos;}m[26];
int f[24];
char text[504];
char mode[]="welcome to code jam";

void Init()
{
    int len=strlen(mode);
    for(int i=0; i<len; ++i)
    {
        if(mode[i]==' ') continue;
        int t=(int)(mode[i]-'a');
        m[t].pos.push_back(i);
    }
}

int main()
{
    /*
    freopen("G:\\Download\\C-large.in", "r", stdin);
    freopen("G:\\Download\\C-large.in.out", "w", stdout);
    */
    Init();
    int caseid,casenum,len,i,j,t;
    scanf("%d\n", &casenum);
    for(caseid=1; caseid<=casenum; ++caseid)
    {
        memset(f, 0, sizeof(f));
        gets(text);
        len=strlen(text);
        for(i=0; i<len; ++i)
        {
            if(text[i]==' ')
            {
                f[7]+=f[6],f[7]%=10000;
                f[10]+=f[9],f[10]%=10000;
                f[15]+=f[14],f[15]%=10000;
            }
            else if(text[i]=='w')
            {
                ++f[0];
            }
            else
            {
                t=text[i]-'a';
                for(j=m[t].pos.size()-1; j>=0; --j)
                    f[m[t].pos[j]]+=f[m[t].pos[j]-1],f[m[t].pos[j]]%=10000;
            }
        }
        printf("Case #%d: %04d\n", caseid, f[18]);
    }
    return 0;
}

/*
3
elcomew elcome to code jam
wweellccoommee to code qps jam
welcome to codejam

Case #1: 0001
Case #2: 0256
Case #3: 0000


 */