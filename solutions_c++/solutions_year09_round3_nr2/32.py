#include <cstdio>
#include <string>
#include <vector>
#include <cstring>
#include <cmath>

using namespace std;

int main()
{
	FILE* input = fopen("input2.txt", "r");
	FILE* output = fopen("output2.txt", "w");
	int t;
	fscanf(input, "%d", &t);
	int i;
	for (i = 0; i < t; i++)
	{
		int n;
		int xsum = 0;
		int ysum = 0;
		int zsum = 0;
		int xmove = 0;
		int ymove = 0;
		int zmove = 0;
		fscanf(input, "%d", &n);
		int x, y, z, vx, vy, vz;
		int j;
		for (j = 0; j < n; j++)
		{
			fscanf(input, "%d %d %d %d %d %d", &x, &y, &z, &vx, &vy, &vz);
			xsum+=x;
			ysum+=y;
			zsum+=z;
			xmove+=vx;
			ymove+=vy;
			zmove+=vz;
		}
		double t;
		t = xmove*xsum + ymove*ysum + zmove*zsum;
		t/=(xmove*xmove + ymove*ymove + zmove*zmove);
		t = -t;
		t = max(0.0, t);
		double d;
		d = (xsum + t*xmove)*(xsum+t*xmove) + (ysum + t*ymove)*(ysum+t*ymove) + (zsum + t*zmove)*(zsum + t*zmove);
		d = sqrt(d);
		d/=n;
		fprintf(output, "Case #%d: %lf %lf\n", i+1, d, t);
	}
}