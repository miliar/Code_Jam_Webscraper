#include <cstdio>
#include <cmath>
#include <cctype>

#include <vector>

using namespace std;

typedef vector<double> TDoubleVector;
typedef vector<TDoubleVector> TDoubleVectorVector;

struct TCenter {
    double X;
    double Y;
    double Mass;
};

typedef vector<TCenter> TCenterVector;
typedef vector<TCenterVector> TCenterVectorVector;

TCenter GetCenter(double d, const TDoubleVectorVector& m, int x0, int y0, int x, int y) {
    double mass = 0;
    double cx = 0;
    double cy = 0;
    for (int k = x0; k < x0 + x; ++k) {
        for (int l = y0; l < y0 + y; ++l) {
            mass += d + m[k][l];
            cx += (double(k)+0.5)*double(d + m[k][l]);
            cy += (double(l)+0.5)*double(d + m[k][l]);
        }
    }
    TCenter result;
    result.Mass = mass;
    if (mass) {
        result.X = cx/mass;
        result.Y = cy/mass;
    } else {
        result.X = 0;
        result.Y = 0;
    }
    return result;
}

TCenter GetCenterC(const TCenterVectorVector& cn, int x0, int y0, int x, int y) {
    const TCenter& c0 = cn[x0 + x][y0 + y];
    const TCenter& c1 = cn[x0][y0 + y];
    const TCenter& c2 = cn[x0 + x][y0];
    const TCenter& c3 = cn[x0][y0];
    TCenter result;
    result.Mass = c0.Mass + c3.Mass - c1.Mass - c2.Mass;
    result.X = (c0.Mass*c0.X + c3.Mass*c3.X - c1.Mass*c1.X - c2.Mass*c2.X)/result.Mass;
    result.Y = (c0.Mass*c0.Y + c3.Mass*c3.Y - c1.Mass*c1.Y - c2.Mass*c2.Y)/result.Mass;
    return result;
}

bool Has(int r, int c, const TCenterVectorVector& cn, const TCenterVectorVector& mn, int k) {
    for (int i = 0; i <= r - k; ++i) {
        for (int j = 0; j <= c - k; ++j) {
            TCenter cc = GetCenterC(cn, i, j, k, k);
            TCenter c0 = mn[i][j];
            TCenter c1 = mn[i + k - 1][j + k - 1];
            TCenter c2 = mn[i + k - 1][j];
            TCenter c3 = mn[i][j + k - 1];
            TCenter c;
            c.Mass = cc.Mass - c0.Mass - c1.Mass - c2.Mass - c3.Mass;
            c.X = (cc.Mass*cc.X - c0.Mass*c0.X - c1.Mass*c1.X - c2.Mass*c2.X - c3.Mass*c3.X)/c.Mass;
            c.Y = (cc.Mass*cc.Y - c0.Mass*c0.Y - c1.Mass*c1.Y - c2.Mass*c2.Y - c3.Mass*c3.Y)/c.Mass;
            if ( fabs(2.0*c.X - k -2.0*i) < 1e-5 && fabs(2.0*c.Y - k -2.0*j) < 1e-5 )
                return true;
        }
    }
    return false;
}

int main() {
    // freopen("input.txt", "r", stdin);

    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-small-attempt1.out", "w", stdout);

    int t;
    scanf("%d", &t);

    for (int iTest = 0; iTest < t; ++iTest) {
        int r, c, d;
        scanf("%d%d%d", &r, &c, &d);

        TDoubleVector dummy(c);
        TDoubleVectorVector m(r, dummy);

        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                char ch;
                scanf("%c", &ch);
                while (!isdigit(ch))
                    scanf("%c", &ch);
                m[i][j] = ch - '0';
            }
        }
        
        TCenterVector dummyC(c + 1);
        TCenterVectorVector cn(r + 1, dummyC);
        TCenterVectorVector mn(r + 1, dummyC);

        for (int i = 0; i <= r; ++i) {
            for (int j = 0; j <= c; ++j) {
                cn[i][j] = GetCenter(d, m, 0, 0, i, j);
            }
        }
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                mn[i][j] = GetCenter(d, m, i, j, 1, 1);
            }
        }

        /*
        for (int i = 0; i < r; ++i)
            for (int j = 0; j < c; ++j)
                for (int x = 1; x <= r - i; ++x)
                    for (int y = 1; y <= c - j; ++y) {
                        TCenter c0 = GetCenter(d, m, i, j, x, y);
                        TCenter c1 = GetCenterC(cn, i, j, x, y);
                        printf("%lf %lf %lf\n", c1.X - c0.X, c1.Y - c0.Y, c1.Mass - c0.Mass);
                    }
        */

        int k = min(r, c);
        while ( (k >= 3) && !Has(r, c, cn, mn, k) )
            --k;

        printf("Case #%d: ", iTest + 1);
        if (k >= 3)
            printf("%d", k);
        else
            printf("IMPOSSIBLE");
        printf("\n");
    }

    return 0;
}
