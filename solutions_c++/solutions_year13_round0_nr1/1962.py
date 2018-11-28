#include<iostream>
using namespace std;
#include<algorithm>
#include<set>
#include<string>
#include<cstring>
#include<vector>
#include<queue>
#include<stack>
#include<deque>
#include<cstdio>
#include<map>

typedef long long lli;

#define fi(i,a,b,d) for(i=a;i<=b;i+=d)
#define fir(i,a,b,d) for(i=a;i>=b;i-=d)

#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))

#define vi vector<int>
#define all(v) v.begin(), v.end()

#define mp make_pair
#define pb push_back
#define ppb pop_back
#define pf push_front
#define ppf pop_front


#define inpi(i) scanf("%d", &i)
#define inplli(i) scanf("%lld", &i)
#define inpc(ch) scanf("%c", &ch)
#define printi(i) printf("%d\n", i)
#define printlli(i) printf("%lld\n", i)
#define printc(ch) printf("%c\n", ch)
#define inpfl(fl) scanf("%f", &fl)
#define printfl(fl) printf("%f", fl)


class className
{
    char mat[5][5];
    int t, i, j, k, ans;
    bool full;

    public:

    int check_hori();
    int check_verti();
    int check_diag();

    void solve()
    {
        cin>>t;

        fi(k,1,t,1)
        {
            full = true;

            fi(i,0,3,1)
            fi(j,0,3,1)
            {
                cin>>mat[i][j];
                if(mat[i][j]=='.')
                full = false;
            }

            cout<<"Case #"<<k<<": ";

            ans = check_hori();
            if(ans)
            {
                if(ans==-1)
                cout<<"X won\n";

                else
                cout<<"O won\n";

                continue;
            }

            ans = check_verti();
            if(ans)
            {
                if(ans==-1)
                cout<<"X won\n";

                else
                cout<<"O won\n";

                continue;
            }

            ans = check_diag();
            if(ans)
            {
                if(ans==-1)
                cout<<"X won\n";

                else
                cout<<"O won\n";

                continue;
            }

            if(full)
            {
                cout<<"Draw\n";
            }
            else
            {
                cout<<"Game has not completed\n";
            }
        }
    }
};

    int className::check_hori()
    {
        int Xs, Os, Ts;
        int i, j;

        fi(i,0,3,1)
        {
            Xs = Os = Ts = 0;
            fi(j,0,3,1)
            {
                if(mat[i][j]=='X')
                ++Xs;
                else if(mat[i][j]=='O')
                ++Os;
                else if(mat[i][j]=='T')
                ++Ts;
            }

            if(Xs==4 || (Xs==3 && Ts==1))
            return -1;
            if(Os==4 || (Os==3 && Ts==1))
            return 1;
        }

        return 0;
    }


    int className::check_verti()
    {
        int Xs, Os, Ts;
        int i, j;

        fi(j,0,3,1)
        {
            Xs = Os = Ts = 0;
            fi(i,0,3,1)
            {
                if(mat[i][j]=='X')
                ++Xs;
                else if(mat[i][j]=='O')
                ++Os;
                else if(mat[i][j]=='T')
                ++Ts;
            }

            if(Xs==4 || (Xs==3 && Ts==1))
            return -1;
            if(Os==4 || (Os==3 && Ts==1))
            return 1;
        }

        return 0;
    }


    int className::check_diag()
    {
        int Xs, Os, Ts;
        int i, j;

        Xs = Os = Ts = 0;
        fi(i,0,3,1)
        {
            if(mat[i][i]=='X')
            ++Xs;
            else if(mat[i][i]=='O')
            ++Os;
            else if(mat[i][i]=='T')
            ++Ts;

            if(Xs==4 || (Xs==3 && Ts==1))
            return -1;
            if(Os==4 || (Os==3 && Ts==1))
            return 1;
        }
        if(Xs==4 || (Xs==3 && Ts==1))
        return -1;
        if(Os==4 || (Os==3 && Ts==1))
        return 1;


        Xs = Os = Ts = 0;
        fi(i,0,3,1)
        {
            j=3-i;

            if(mat[i][j]=='X')
            ++Xs;
            else if(mat[i][j]=='O')
            ++Os;
            else if(mat[i][j]=='T')
            ++Ts;
        }
        if(Xs==4 || (Xs==3 && Ts==1))
        return -1;
        if(Os==4 || (Os==3 && Ts==1))
        return 1;

        return 0;
    }


int main()
{
    className obj;

    obj.solve();
    return 0;
}
