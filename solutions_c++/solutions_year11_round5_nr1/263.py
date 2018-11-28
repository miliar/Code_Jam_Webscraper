#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

struct point{double x, y;};

const double tol=1e-8;

int n, m, r;
double w;
point a[128], b[128];

double get_y(point p1, point p2, double x)
{
	double x1, y1, x2, y2;
	x1=p1.x; y1=p1.y;
	x2=p2.x; y2=p2.y;
	return (x*y1-x2*y1-x*y2+x1*y2)/(x1-x2);
}

int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
	
	int i, j, k;
	int t, tc;
	double tot;
	double x, nx;
	double y1, y2;
	double sarea;
	double s, e, mid;
	fscanf(fp, "%d", &tc);
	for(t=1;t<=tc;t++)
	{
		fscanf(fp, "%lf%d%d%d", &w, &m, &n, &r);
		for(i=1;i<=m;i++) fscanf(fp, "%lf%lf", &b[i].x, &b[i].y);
		for(i=1;i<=n;i++) fscanf(fp, "%lf%lf", &a[i].x, &a[i].y);
		tot=0.0;
		x=0.0;
		for(i=j=1;i<n && j<m;)
		{
			if(a[i+1].x<b[j+1].x)
			{
				nx=a[i+1].x;
				y1=get_y(a[i], a[i+1], x)-get_y(b[j], b[j+1], x);
				y2=get_y(a[i], a[i+1], nx)-get_y(b[j], b[j+1], nx);
				tot+=(nx-x)*(y1+y2)/2.0;
				x=nx; i++;
			}
			else if(a[i+1].x>b[j+1].x)
			{
				nx=b[j+1].x;
				y1=get_y(a[i], a[i+1], x)-get_y(b[j], b[j+1], x);
				y2=get_y(a[i], a[i+1], nx)-get_y(b[j], b[j+1], nx);
				tot+=(nx-x)*(y1+y2)/2.0;
				x=nx; j++;
			}
			else
			{
				nx=a[i+1].x;
				y1=get_y(a[i], a[i+1], x)-get_y(b[j], b[j+1], x);
				y2=get_y(a[i], a[i+1], nx)-get_y(b[j], b[j+1], nx);
				tot+=(nx-x)*(y1+y2)/2.0;
				x=nx; i++; j++;
			}
		}
		sarea=tot/(double)(r);
		tot=sarea;
		x=0.0;
		fprintf(ofp, "Case #%d:\n", t);
		for(i=j=1, k=0;i<n && j<m && k<r-1;)
		{
			if(a[i+1].x<b[j+1].x)
			{
				nx=a[i+1].x;
				y1=get_y(a[i], a[i+1], x)-get_y(b[j], b[j+1], x);
				y2=get_y(a[i], a[i+1], nx)-get_y(b[j], b[j+1], nx);
				if(tot>(nx-x)*(y1+y2)/2.0)
				{
					tot-=(nx-x)*(y1+y2)/2.0;
					x=nx; i++;
					continue;
				}
				s=x; e=nx;
				while(e-s>tol)
				{
					mid=(s+e)/2.0;
					y2=get_y(a[i], a[i+1], mid)-get_y(b[j], b[j+1], mid);
					if(tot>(mid-x)*(y1+y2)/2.0) s=mid;
					else e=mid;
				}
				k++;
				fprintf(ofp, "%.8lf\n", (s+e)/2.0);
				x=(s+e)/2.0; tot=sarea;
			}
			else if(a[i+1].x>b[j+1].x)
			{
				nx=b[j+1].x;
				y1=get_y(a[i], a[i+1], x)-get_y(b[j], b[j+1], x);
				y2=get_y(a[i], a[i+1], nx)-get_y(b[j], b[j+1], nx);
				if(tot>(nx-x)*(y1+y2)/2.0)
				{
					tot-=(nx-x)*(y1+y2)/2.0;
					x=nx; j++;
					continue;
				}
				s=x; e=nx;
				while(e-s>tol)
				{
					mid=(s+e)/2.0;
					y2=get_y(a[i], a[i+1], mid)-get_y(b[j], b[j+1], mid);
					if(tot>(mid-x)*(y1+y2)/2.0) s=mid;
					else e=mid;
				}
				k++;
				fprintf(ofp, "%.8lf\n", (s+e)/2.0);
				x=(s+e)/2.0; tot=sarea;
			}
			else
			{
				nx=a[i+1].x;
				y1=get_y(a[i], a[i+1], x)-get_y(b[j], b[j+1], x);
				y2=get_y(a[i], a[i+1], nx)-get_y(b[j], b[j+1], nx);
				if(tot>(nx-x)*(y1+y2)/2.0)
				{
					tot-=(nx-x)*(y1+y2)/2.0;
					x=nx; i++; j++;
					continue;
				}
				s=x; e=nx;
				while(e-s>tol)
				{
					mid=(s+e)/2.0;
					y2=get_y(a[i], a[i+1], mid)-get_y(b[j], b[j+1], mid);
					if(tot>(mid-x)*(y1+y2)/2.0) s=mid;
					else e=mid;
				}
				k++;
				fprintf(ofp, "%.8lf\n", (s+e)/2.0);
				x=(s+e)/2.0; tot=sarea;
			}
		}
	}

	fclose(fp);
	fclose(ofp);
	char cmd[128];
	strcpy(cmd, "type ");
	strcat(cmd, outfile);
	system(cmd);
	return 0;
}
