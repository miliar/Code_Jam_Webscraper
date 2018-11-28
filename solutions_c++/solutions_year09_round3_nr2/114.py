#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

typedef long double U;

U sq(U n)
{
    return n * n;
}
U dist(U x, U y, U z)
{
    return sqrt(sq(x) + sq(y) + sq(z)); 
}

U dot(U x1, U y1, U z1, U x2, U y2, U z2)
{
    return x1 * x2 + y1 * y2 + z1 * z2;
}

U cross(U x1, U y1, U z1, U x2, U y2, U z2)
{
    return sqrt(sq(y1 * z2 - y2 * z1) + sq(z1 * x2 - z2 * x1) + sq(x1 * y2 - x2 *  y1));
}

int main()
{
    int T;
    scanf("%d", &T);
    for(int tt = 1; tt <= T; tt++)
    {
        int N;
	scanf("%d", &N);
        
	U vx = 0, vy = 0, vz = 0;
	U mx = 0, my = 0, mz = 0;
	for(int i = 0; i < N; i++)
	{
            int x, y, z;
	    scanf("%d%d%d", &x, &y, &z);
	    mx += x;
	    my += y;
	    mz += z;
	    int x2, y2, z2;
scanf("%d%d%d", &x2, &y2, &z2);
	    vx += x2 ;
	    vy += y2;
	    vz += z2 ;

	}

	vx /= N;
	vy /= N;
	vz /= N;
	mx /= N;
	my /= N;
	mz /= N;

	U t = fabs(dot(vx, vy, vz, -mx, -my, -mz) / sq(dist(vx, vy, vz)));
	U d = fabs(cross(vx, vy, vz, -mx, -my, -mz) / dist(vx, vy, vz));

	printf("Case #%d: ", tt);

	cout.precision(8);
	if(dot(vx, vy, vz, -mx, -my, -mz) > 0)
	    cout << fixed << d << ' ' << t << '\n';
	    //printf("%.8lf %.8lf\n", d, t);
	else
	    cout << fixed << dist(mx, my, mz) << ' ' << 0.0  << '\n';

    }
    return 0;
}
