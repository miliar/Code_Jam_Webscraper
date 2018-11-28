
/************** Elvis Rusnel Capia Quispe ***************/
#include <bits/stdc++.h>
#define f(i,x,y) for (int i = (x); i < (y); i++)
#define fd(i,x,y) for(int i = x; i>= y; i--)
#define FOR(it,A) for(typeof A.begin() it = A.begin(); it!=A.end(); it++)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define vint vector<int>
#define pii pair<int,int>
#define vpii vector<pii>
#define ll long long
#define clr(A,x) memset(A, x, sizeof A)
#define pb push_back
#define fst first
#define snd second
#define ones(x) __builtin_popcount(x)
#define cua(x) (x)*(x)
#define MOD 1000000007
#define INF 1000000000
#define HASH unsigned long long
#define bug1(x) cout<<#x<<" = "<<x<<endl
#define bug2(x,y) cout<<#x<<" = "<<x<<" "<<#y<<" = "<<y<<endl
#define bug3(x,y,z) cout<<#x<<" = "<<x<<" "<<#y<<" = "<<y<<" "<<#z<<" = "<<z<<endl
#define bug4(x,y,z,m) cout<<#x<<" = "<<x<<" "<<#y<<" = "<<y<<" "<<#z<<" = "<<z<<" "<<#m<<" = "<<m<<endl
#define sc(x) scanf("%d",&x)
#define ana(x) cout<<"NO JUST FOR ME"<<endl

using namespace std;
char TICTAC[4][4];
int main(){
    freopen("in.c","r",stdin);
    freopen("on.c","w",stdout);

    int tc , nc = 1;
    sc(tc);

    while(tc--)
    {
        bool fill = true;
        f(i,0,4)
            f(j,0,4)
            {   cin>>TICTAC[i][j];
            if(TICTAC[i][j]=='.') fill = false;
            }
        //gana O
        string ans = "";
        int A , B , neutral;

        f(i,0,4)
        {   A = 0 , B = 0 , neutral = 0;
            f(j,0,4)
            if(TICTAC[i][j]=='O') A++;
            else if(TICTAC[i][j]=='X') B++;
                 else   if(TICTAC[i][j]=='T') neutral++;

            if(A==4 || (A==3 && neutral==1)) ans = "O";
            else    if(B==4 || (B==3 && neutral==1)) ans = "X";
        }

        f(j,0,4)
        {   A = 0 , B = 0 , neutral = 0;
            f(i,0,4)
            if(TICTAC[i][j]=='O') A++;
            else if(TICTAC[i][j]=='X') B++;
                 else   if(TICTAC[i][j]=='T') neutral++;

            if(A==4 || (A==3 && neutral==1)) ans = "O";
            else    if(B==4 || (B==3 && neutral==1)) ans = "X";
        }

        A = 0 , B = 0 , neutral = 0;
        f(i,0,4)
        {    if(TICTAC[i][i]=='O') A++;
            else if(TICTAC[i][i]=='X') B++;
                 else   if(TICTAC[i][i]=='T') neutral++;

        }
            if(A==4 || (A==3 && neutral==1)) ans = "O";
            else    if(B==4 || (B==3 && neutral==1)) ans = "X";

        A = 0 , B = 0 , neutral = 0;
        f(i,0,4)
        {    if(TICTAC[i][3 - i]=='O') A++;
            else if(TICTAC[i][3 - i]=='X') B++;
                 else   if(TICTAC[i][3 - i]=='T') neutral++;

        }
            if(A==4 || (A==3 && neutral==1)) ans = "O";
            else    if(B==4 || (B==3 && neutral==1)) ans = "X";

        printf("Case #%d: ",nc++);
        if(ans=="O") cout<<"O won"<<endl;
        else    if(ans=="X") cout<<"X won"<<endl;
                else    if(fill) cout<<"Draw"<<endl;
                        else cout<<"Game has not completed"<<endl;

    }


    return 0;
}

