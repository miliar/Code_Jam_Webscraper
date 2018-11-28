#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<queue>
#include<map>
#include<set>
#define PB push_back
#define MP make_pair
#define X first
#define Y second
#define MS0(A) memset(A,0,sizeof(A));
#define rep(i,n) for(int i=0;i<n;i++)
#define repp(i,a,b) for(int i=a;i<=b;i++)
#define red(i,n) for(int i=n-1;i>=0;i--)
#define DA(A,n) {cout<<#A;rep(iii,n)cout<<' '<<A[iii];cout<<endl;}
#define D(x) {cout<<#x<<' '<<(x)<<endl;}
#define DD(x,y) {cout<<#x<<' '<<x<<' ';cout<<#y<<' '<<y<<endl;}
#define DDD(x,y,z) {cout<<#x<<' '<<x<<' ';cout<<#y<<' '<<y<<' ';cout<<#z<<' '<<z<<endl;}
#include<ext/rope>
#define __rope __gnu_cxx::
using namespace std;
typedef long long LL;
const int MAXN=111111;
const int oo=0X1FFFFFFF;
int PP=1000000007;
const long double PI=3.141592653589793;
template<typename TT>
void read(TT &x)
{
    char ch;
	for (ch=getchar(); ch>'9'||ch<'0'; ch=getchar()) ;
	for (x=0; ch>='0'&&ch<='9'; ch=getchar()) x=x*10+ch-48;
}
template<typename TT> void read2(TT &x,TT &y){read(x);read(y);}
template<typename TT> void read3(TT &x,TT &y,TT &z){read(x);read(y);read(z);}

int n;
char s[4][4],non[1];
bool work(char a,char b,char c,char d){
    int X=(a=='X')+(b=='X')+(c=='X')+(d=='X');
    int O=(a=='O')+(b=='O')+(c=='O')+(d=='O');
    int T=(a=='T')+(b=='T')+(c=='T')+(d=='T');
    if(X+T==4){puts("X won");return 1;}
    if(O+T==4){puts("O won");return 1;}
    return 0;
}
void Init(){
    rep(i,4) gets(s[i]);gets(non);
    rep(i,4) if(work(s[i][0],s[i][1],s[i][2],s[i][3]))return;
    rep(i,4) if(work(s[0][i],s[1][i],s[2][i],s[3][i]))return;
    if(work(s[0][0],s[1][1],s[2][2],s[3][3])) return;
    if(work(s[0][3],s[1][2],s[2][1],s[3][0])) return;
    bool draw=1;
    rep(i,4)rep(j,4)if(s[i][j]=='.')draw=0;
    puts(draw? "Draw":"Game has not completed");
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;read(T);
    rep(i,T){
        cout<<"Case #"<<(i+1)<<": ";
        Init();
    }

}
