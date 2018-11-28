#include <stdio.h>
#include <math.h>
#include <crtdbg.h>

//#define SIZE	500

//int x[SIZE], y[SZE], z[SIZE], vx[SIZE], vy[SIZE], vz[SIZE];

int main(int argc, char *argv[])
{
	char line[200];
	gets(line);
	int nTestCases;
	sscanf(line, "%d", &nTestCases);
	for (int i = 0; i < nTestCases; i++)
	{
		gets(line);
		int nFlys;
		double xi = 0;
		double yi = 0;
		double zi = 0;
		double dvx = 0, dvy = 0, dvz = 0;
		sscanf(line, "%d", &nFlys);
		for (int j = 0; j < nFlys; j++)
		{
			gets(line);
			//sscanf(line, "%d %d %d %d %d %d", x + j, y + j, z + j, vx + j, vy + j, vz + j);
			int x, y, z, vx, vy, vz;
			sscanf(line, "%d %d %d %d %d %d", &x, &y, &z, &vx, &vy, &vz);
			xi += x;
			yi += y;
			zi += z;
			dvx += vx;
			dvy += vy;
			dvz += vz;
		}
		xi /= nFlys;
		yi /= nFlys;
		zi /= nFlys;
		dvx /= nFlys;
		dvy /= nFlys;
		dvz /= nFlys;
		double t;
		double tmp = dvx * dvx + dvy * dvy + dvz * dvz;
		if (tmp == 0.0)
		{
			t = 0.0;
		}
		else
		{
			t = -(dvx * xi + dvy * yi + dvz * zi) / tmp;
			if (t <= 0.0)
			{
				t = 0.0;
			}
		}
		double xa = dvx * t + xi;
		double ya = dvy * t + yi;
		double za = dvz * t + zi;
		double distance = sqrt(xa * xa + ya * ya + za * za);
		printf("Case #%d: %.8f %.8f\n", i +1, distance, t);
	}
	return 0;
}
