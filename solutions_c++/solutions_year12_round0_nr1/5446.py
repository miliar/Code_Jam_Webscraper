#include <iostream>
#include <fstream>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;
#define MID ((l+r)>>1)
#define BUG1 puts("BUG11\n")
#define LgLg long long
#define MAX(a,b) (a>b?a:b)
#define MIN(a,b) (a>b?b:a)
#define two(x)            ((LL)1<<(x))
#define include(a,b)        (((a)&(b))==(b))
#define FOR(i,a,b) for(int (i)=(a);(i)<=(b);(i)++)
#define FF(i,a) for(int i=0;i<a;i++)
#define FD(i,a,b) for(int i=a;i>=b;i--)
#define STOP  int stop;scanf("%d", &stop)
#define PD(x) printf("%d",(x))
#define PP printf(" ")
#define SD(x) scanf("%d", &(x))
#define SF(x) scanf("%lf", &(x))
#define SET(x,y) memset(x,y,sizeof(x))
#define LN printf("\n");
#define SWAP(a,b) a=a xor b;b= a xor b;a=a xor b;
#define EPS 1e-8
#define PI acos(-1.0)
int dx[] = {-1,0,1,0};
int dy[] = {0,1,0,-1};
#define read            freopen("in.in","r",stdin)
#define write            freopen("out.out","w",stdout)

int map[26];

int main(){
    read;
    write;
map[0]=24;
map[1]=7;
map[2]=4;
map[3]=18;
map[4]=14;
map[5]=2;
map[6]=21;
map[7]=23;
map[8]=3;
map[9]=20;
map[10]=8;
map[11]=6;
map[12]=11;
map[13]=1;
map[14]=10;
map[15]=17;
map[16]=25;
map[17]=19;
map[18]=13;
map[19]=22;
map[20]=9;
map[21]=15;
map[22]=5;
map[23]=12;
map[24]=0;
map[25]=16;
    int n;
    char ch[10000];
    SD(n);
    gets(ch);
    FOR(i,1,n){
        gets(ch);
        printf("Case #%d: ",i);
        FF(i,strlen(ch)){
            if ( ch[i]<='z' && ch[i]>='a')
                printf("%c",(char)(map[ch[i]-'a']+'a'));
            else
                PP;
        }LN;

    }

}
