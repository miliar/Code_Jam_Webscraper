#include <stdio.h>
#include <math.h>

const double delta = 1e-12;

double t, l, r, m1, m2;
int T, C, n, i, j, k, A, B, CC, D, E, F;
double x, y, z, vx, vy, vz, div;

double ti(double t)
{
    double X, Y, Z;
    
    X = vx; X *= t; X += x;
    Y = vy; Y *= t; Y += y;
    Z = vz; Z *= t; Z += z;
    return sqrt(X * X + Y * Y + Z * Z) / n;
}

int main()
{
    freopen("b_in.txt", "r", stdin);
    freopen("b_out.txt", "w", stdout);
    scanf("%d", &T);
    for (C=1; C<=T; C++)
    {
        scanf("%d", &n);
        x = y = z = vx = vy = vz = 0;
        for (i=0; i<n; i++)
        {
            scanf("%d %d %d %d %d %d", &A, &B, &CC, &D, &E, &F);
            x += A; y += B; z += CC; vx += D; vy += E; vz += F;
        }
        t = 1;
        while ((vx||vy||vz) && ti(0)>ti(t)-1) t += t;
        l = 0; r = t;
        while (l+1e-9<r)
        {
        	m1 = (r - l) / 3 + l; m2 = r - (r - l) / 3;
         	if (ti(m1)-delta>ti(m2)) l = m1; else r = m2;
        }
        printf("Case #%d: %.8lf %.8lf\n", C, ti(l), l);
    }
}

