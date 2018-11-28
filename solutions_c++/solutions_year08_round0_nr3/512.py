#include <stdio.h>
#include <iostream>
#include <math.h>

typedef struct _point
{
    double x;
    double y;
} point;

double readcase(FILE* fp);

using namespace std;

int main(int argc, char* argv[])
{
    FILE* fp;
    char buff[256];
    int ncases;

    if(argc < 2)
    {
        cout << "no input" << endl;
	return 0;
    }
    fp = fopen(argv[1], "r");
    fgets(buff, 255, fp);
    sscanf(buff, "%d", &ncases);
    for(int i=0; i<ncases; i++)
    {
        double result = readcase(fp);
	cout << "Case #" << (i+1) << ": ";
	printf("%.6f\n", result);
    }
    fclose(fp);

}

double readcase(FILE* fp)
{
    const double SQRT2 = 1.414213562;
    double result = 0;
    double f, R, t, r, g;
    double wCell, wSkip;
    double areaSum = 0, lastArea;
    int N, i, j;
    char buff[256];
    double t1, t2, t3, t4, t5, t6, t7, t8, t9, t10;
    fgets(buff, 255, fp);
    sscanf(buff, "%lf %lf %lf %lf %lf", &f, &R, &t, &r, &g);

    if(f + f > g)  return 1;
    if(R < (r + f) * SQRT2 + f + t)  return 1;

    wCell = g + r + r;
    wSkip = g - f - f;
    t1 = (R - t - f);
    N = (int)(ceil((R - t - f) / wCell));
    for(i=0; i<N; i++)
        for(j=0; j<N; j++)
	{
	    point alp, bet, gam, del;
	    int cellstat = 0;

	    alp.x = i * wCell + r + f;
	    alp.y = j * wCell + r + g - f;
	    bet.x = i * wCell + r + g - f;
	    bet.y = j * wCell + r + g - f;
	    gam.x = i * wCell + r + f;
	    gam.y = j * wCell + r + f;
	    del.x = i * wCell + r + g - f;
	    del.y = j * wCell + r + f;

	    bool alpInC1, betInC1, gamInC1, delInC1;
	    t2 = t1 * t1;
	    alpInC1 = (alp.x*alp.x + alp.y*alp.y < t2);
	    betInC1 = (bet.x*bet.x + bet.y*bet.y < t2);
	    gamInC1 = (gam.x*gam.x + gam.y*gam.y < t2);
	    delInC1 = (del.x*del.x + del.y*del.y < t2);

            lastArea = areaSum;
	    if(alpInC1 && betInC1 && gamInC1 && delInC1)
	    {
	        cellstat = 1;
	        areaSum += wSkip * wSkip;
	    }
	    else if(alpInC1 && gamInC1 && delInC1)
	    {
	        cellstat = 3;
	        t2 = sqrt(t1 * t1 - alp.y*alp.y);
	        t3 = sqrt(t1 * t1 - del.x*del.x);
		t5 = del.x - t2;
		t6 = alp.y - t3;
		t4 = sqrt(t5 * t5 + t6 * t6);
		t7 = t1 * t1 * asin(0.5 * t4 / t1);
		t8 = 0.5 * t2 * alp.y;
		t9 = 0.5 * t3 * del.x;
		t10 = alp.y * del.x - wSkip * wSkip;
		areaSum += (t7 + t8 + t9 - t10);
	    }
	    else if(alpInC1 && gamInC1)
	    {
	        cellstat = 4;
	        t2 = sqrt(t1 * t1 - alp.y*alp.y);
	        t3 = sqrt(t1 * t1 - gam.y*gam.y);
		t5 = t3 - t2;
		t6 = wSkip;
		t4 = sqrt(t5 * t5 + t6 * t6);
		t7 = t1 * t1 * asin(0.5 * t4 / t1);
		t8 = 0.5 * t2 * alp.y;
		t9 = 0.5 * t3 * gam.y;
		t10 = alp.y * t3 - (t3 - gam.x) * wSkip;
		areaSum += (t7 + t8 + t9 - t10);
	    }
	    else if(gamInC1 && delInC1)
	    {
	        cellstat = 6;
	        t2 = sqrt(t1 * t1 - gam.x*gam.x);
	        t3 = sqrt(t1 * t1 - del.x*del.x);
		t5 = t2 - t3;
		t6 = wSkip;
		t4 = sqrt(t5 * t5 + t6 * t6);
		t7 = t1 * t1 * asin(0.5 * t4 / t1);
		t8 = 0.5 * t2 * gam.x;
		t9 = 0.5 * t3 * del.x;
		t10 = del.x * t2 - (t2 - gam.y) * wSkip;
		areaSum += (t7 + t8 + t9 - t10);
	    }
	    else if(gamInC1)
	    {
	        cellstat = 5;
	        t2 = sqrt(t1 * t1 - gam.x*gam.x);
	        t3 = sqrt(t1 * t1 - gam.y*gam.y);
		t5 = t3 - gam.x;
		t6 = t2 - gam.y;
		t4 = sqrt(t5 * t5 + t6 * t6);
		t7 = t1 * t1 * asin(0.5 * t4 / t1);
		t8 = 0.5 * t2 * gam.x;
		t9 = 0.5 * t3 * gam.y;
		t10 = t2 * t3 - t5 * t6;
		areaSum += (t7 + t8 + t9 - t10);
	    }
	    else
	    {
	        cellstat = 2;
	    }
	    /*
	    cout << "Cell at (" << i*wCell << ", " << j*wCell << "):" << endl;
	    cout << "  cellstat = " << cellstat << endl;
	    t2 = areaSum - lastArea;
	    cout << "  area = " << t2 << endl;
	    cout << "  t1 = " << t1 << endl;
	    cout << "  t7 = " << t7 << endl;
	    cout << "  t8 = " << t8 << endl;
	    cout << "  t9 = " << t9 << endl;
	    cout << "  t10 = " << t10 << endl;
	    cout << "  alp.x = " << alp.x << endl;
	    cout << "  alp.y = " << alp.y << endl;
	    cout << "  del.x = " << del.x << endl;
	    cout << "  del.y = " << del.y << endl;
	    */
	}

    t2 = 0.25 * M_PI * R * R;
    result = 1.0 - areaSum / t2;

    return result;
}

