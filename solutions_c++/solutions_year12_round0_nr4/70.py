#include <cstdio>
#include <cmath>
#include <cstring>

#define MAXN 100
#define EPS  1e-8
#define MICRO_STEP 1e-8
#define INF  1e9
#define SHIFT 100

typedef long double single;

bool dir[200][200];
char s[MAXN][MAXN];
int  hx, hy, d;
int  xx, yy;

char h(int y, int x)
{
    if (y < 0 || y >= hy || x < 0 || x >= hx) return '.';
    return s[y][x];
}

/*
single abs(single x)
{
    return x > 0 ? x : -x;
}*/

int up(single x)
{
    return (int) ( ceil(x) );
}

int dn(single x)
{
    return (int) ( floor(x) );
}

single min(single x, single y)
{
    return x < y ? x : y;
}

bool eq(single x, single y)
{
    return abs(x-y) < EPS;
}

int gcd(int x, int y)
{
    return x==0 ? y : gcd(y % x, x);
}

int neib(single y, single x)
{
    y -= 0.1;
    x -= 0.1;
    int Y = dn(y);
    int X = dn(x);
    int n = 0;
    if (h(y, x) == '#') n++;
    if (h(y+1, x) == '#') n++;
    if (h(y, x+1) == '#') n++;
    if (h(y+1, x+1) == '#') n++;
    return n;
}

bool xneib(single y, single x)
{
    y -= 0.1;
    x -= 0.1;
    int Y = dn(y);
    int X = dn(x);
    if (h(y, x) == '#' && h(y+1, x) == '#') return true;
    if (h(y, x+1) == '#' && h(y+1, x+1) == '#') return true;

    return false;
}

bool pass(int dy, int dx)
{
    single step;
    int    X1, Y1;
    single tx, ty;
    single x, y;
    char   c;
    int    cnt;

    single T = sqrt(dx*dx + dy*dy + 0.0);
    single vx = dx/T;
    single vy = dy/T;


    x = xx + 0.5;
    y = yy + 0.5;

    while (true)
    {
        X1 = dn(x);
        Y1 = dn(y);

                    if (abs(vx) > EPS)
                    {
                        if (vx > EPS) 
                            tx = (up(x) - x) / vx;
                        else
                            tx = (dn(x) - x) / vx;
                    } else tx = INF;

                    if (abs(vy) > EPS)
                    {
                        if (vy > EPS) 
                            ty = (up(y) - y) / vy;
                        else
                            ty = (dn(y) - y) / vy;
                    } else ty = INF;


                    if (min(tx, ty) > T + EPS)
                    {
                        // end of journey
                        x = x + vx*T;
                        y = y + vy*T;
                        
                        return (eq(xx + 0.5, x) && eq(yy + 0.5, y));
                    }



        if (eq(tx, ty))
        {
            x = x + vx*tx;
            y = y + vy*tx;
            T -= tx;

            cnt = neib(y, x);

            if (h(dn(y + vy*tx), dn(x + vx*tx)) != '#') //touching
            {
                // nothing to do
            }
            else if (cnt==1)
            {
                // lonely corner
                return false;
            } 
            else if (cnt==3)
            {
                vx = -vx;
                vy = -vy;
            }
            else 
            {
                if (xneib(y, x)) 
                    vx = -vx;
                else
                    vy = -vy;
            }
            T -= MICRO_STEP;
            x += vx*MICRO_STEP;
            y += vy*MICRO_STEP;

        }
        else 
        {
            if (tx < ty)
            {
                step = tx;
                c = vx > 0 ? h(Y1, X1 + 1) : h(Y1, X1 - 1);
            }
            else
            {
                step = ty;
                c = vy > 0 ? h(Y1 + 1, X1) : h(Y1 - 1, X1);
            }
            x = x + vx*step;
            y = y + vy*step;
            T -= step;            

            if (tx < ty && c=='#') vx = -vx;
            if (ty < tx && c=='#') vy = -vy;

            T -= MICRO_STEP;
            x = x + vx*MICRO_STEP;
            y = y + vy*MICRO_STEP;

        }
    }
}


int main()
{    
    int tc;
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);

    scanf("%i", &tc);
    for(int tt=1; tt<=tc; ++tt)
    {
        fprintf(stderr, "%i\n", tt);
        memset(dir, 0, sizeof(dir));
        scanf("%i %i %i", &hy, &hx, &d);
        for(int i=0; i<hy; ++i) 
        {
            scanf("%s", s[i]);
            for(int j=0; j<hx; ++j) if (s[i][j] == 'X') xx = j, yy = i;
        }
        
        int ans = 0;

        
        for(int dy=-d; dy<=d; ++dy)
            for(int dx=-d; dx<=d; ++dx) if (dx*dx + dy*dy <= d*d)
            {
                if (!dx && !dy) continue;
                int g = gcd( abs(dx), abs(dy) );
                int px = dx / g;
                int py = dy / g;
                if (dir[py + SHIFT][px + SHIFT]) continue;

                if (pass(dy, dx)) 
                {
                    dir[py + SHIFT][px + SHIFT] = true;
                    ans++;
                }
            } 
        
        //if (pass(-3, 3)) ans++;
        printf("Case #%i: %i\n", tt, ans);
    }
}
