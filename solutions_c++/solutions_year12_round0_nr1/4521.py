#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <stack>
#include <set>
#include <list>
#include <iostream>
#include <sstream>
#include <algorithm>

using namespace std;

#define pb push_back
#define clean(a,b) memset(a,b,sizeof(a))
#define oo 1<<20
#define dd double
#define ll long long
#define ull unsigned long long
#define ff float
#define EPS 10E-5
#define fr first
#define sc second
#define MAXX 100000
#define PRIME_N 1000000
#define PI (2*acos(0))
#define INFI 1<<30
#define SZ(a) ((int)a.size())
#define all(a) a.begin(),a.end()

//int rx[] = {0,-1,0,1,1,-1,-1,0,1}; //four direction x
//int ry[] = {0,1,1,1,0,0,-1,-1,-1   //four direction y
//int rep[] = {1,1,4,4,2,1,1,4,4,2}; //repet cycle for mod
//void ullpr(){printf("range unsigned long long : %llu\n",-1U);} //for ull
//void ulpr(){printf("range unsigned long : %lu\n",-1U);} //for ull
//void upr(){printf("range unsigned : %u\n",-1U);} //for ull

string inp = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
string out = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
string giv;

map<char,char>mpcheck;

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int Tcase,cas =1;
    scanf("%d",&Tcase);
    mpcheck['z'] = 'q';
    mpcheck['q'] = 'z';

    for(int i=0 ; i<SZ(inp) ; i++)
    {
        if(mpcheck[inp[i]]=='\0')mpcheck[inp[i]] = out[i];
    }
    getchar();
    while(Tcase--)
    {
        getline(cin,giv);
        printf("Case #%d: ",cas++);
        for(int i=0 ; i<SZ(giv) ; i++)
        {
            printf("%c",mpcheck[giv[i]]);
        }
        printf("\n");
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
