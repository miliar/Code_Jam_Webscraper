#include <iostream>
#include <algorithm>

#define forn(i,n) for(int i = 0; i < n; ++i)
#define forab(i,a,b) for(int i = a; i <= b; ++i)

#define N (8+2)

using namespace std;

typedef unsigned char uc;

uc msk[N+1][N+1][N+1][2];

int T, n, m;

int u[N], v[N];
uc ans[N];int kans;

int sum(uc m){
    return m ? (sum(m>>1) + (m&1)) : 0;
}

void f(uc m, int i){
    if(sum(m) <= 2) return ;
    if(i < 0){
        ans[kans++] = m;
    }else{
        f(m & msk[n][u[i]][v[i]][0], i - 1);
        f(m & msk[n][u[i]][v[i]][1], i - 1);
    }
}

int cl[N];
int mcl[N], Ans;

bool g(int i){
    if(i == n){
        int mx = *max_element(cl, cl + n) + 1;
        uc mmx = (1<<mx) - 1;
        if(mx == Ans){
            int i = 0;
            for(; i < kans; ++i){
                uc cur = 0;
                forn(z, n)
                    if( (ans[i] >> z) & 1)
                        cur |= (1 << (cl[z]));
                if(cur != mmx)
                    break;
            }
            if(i == kans){
                copy(cl, cl + n, mcl);
                return 1;
            }
        }
    }else{
        forn(t, Ans){
            cl[i] = t;
            if(g(i + 1))return 1;
        }
    }
    return 0;
}

int main()
{
    forab(n, 4, 8){
        for(int l = 0; l < n; ++l)
            for(int r = l + 2; r < n; ++r){
                msk[n][l][r][0] = (1 << r);
                msk[n][l][r][1] = (1 << l);
                int i = l;
                while(i != r){
                    msk[n][l][r][0] |= (1 << i);
                    if(++i == n)
                        i = 0;
                }
                i = r;
                while(i != l){
                    msk[n][l][r][1] |= (1 << i);
                    if(++i == n)
                        i = 0;
                }
            }
    }
    cin >> T;
    forn(t, T){
        cin >> n >> m;
        forn(i, m)
            cin >> u[i];
        forn(i, m)
            cin >> v[i];
        forn(i, m){
            u[i] -= 1;
            v[i] -= 1;
            if(u[i] > v[i])
                swap(u[i], v[i]);
        }
        kans = 0;
        f( (1 << n) - 1, m - 1 );
        Ans = 1;
        while(g(0))
            ++Ans;
        --Ans;
        cout << "Case #" << t + 1 << ": " << Ans << endl;
        forn(i, n)
            cout << mcl[i] + 1 << ' ';
        cout << endl;
    }
    return 0;
}
