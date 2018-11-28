#include <iostream>
#include <fstream>
#include <string>
#include <queue>
#include <deque>
#include <iomanip>
#include <math.h>
using namespace std;

class FF
{
public:
	int x, y, z;
	int vx, vy, vz;

	FF(){}

	void set(int x,int y,int z,int vx,int vy,int vz)
	{
		this->x = x;
		this->y = y;
		this->z = z;
		this->vx = vx;
		this->vy = vy;
		this->vz = vz;
	}
};

void analyze(FF* ff, int N, double &dmin, double &tmin)
{
	double ax = 0, bx = 0;
	double ay = 0, by = 0;
	double az = 0, bz = 0;
	double a = 0, b = 0, c = 0;
	for(int i = 0; i < N; i++)
	{
		ax += ff[i].x;
		bx += ff[i].vx;
		ay += ff[i].y;
		by += ff[i].vy;
		az += ff[i].z;
		bz += ff[i].vz;
	}

	a = bx * bx + by * by + bz * bz;
	b = 2 * ax * bx + 2 * ay * by + 2 * az * bz;
	c = ax * ax + ay * ay + az * az;

	if(abs(a) < 0.0000001)
	{
		if(a * b > 0)
		{
			tmin = 0;
		}else
		{
			if(abs(b) > 0.0000001)
			{
				tmin = -1 * c / b;
			}else
			{
				tmin = 0;
			}
		}
	}else
	{
		tmin =  -1 * b / 2 / a;
	}

	if(tmin < 0)
	{
		tmin = 0;
	}
	dmin = sqrt(a * tmin * tmin + b * tmin + c) / N;
}

char *infilepath = "C:\\Users\\cyzhao\\Desktop\\code jam\\Round1c_2\\B-large.in";
char *outfilepath = "C:\\Users\\cyzhao\\Desktop\\code jam\\Round1c_2\\out.txt";

void main()
{
	ifstream infile(infilepath);
	if(!infile)
	{
		cerr<<"File could not be open"<<endl;
		abort();
	}

	ofstream outfile;
	outfile.open(outfilepath, ios::out);
	if(!outfile)
	{
		cerr<<"File could not be open"<<'\n';
		abort();
	}

	int T, N, x, y, z, vx, vy, vz;
	double dmin, tmin;
	FF* ff;
	infile>>T;
	for(int i = 0; i < T; i++)
	{
		infile>>N;
		ff = new FF[N];
		for(int j = 0; j < N; j++)
		{
			infile>>x>>y>>z>>vx>>vy>>vz;
			ff[j].set(x,y,z,vx,vy,vz);
		}
		analyze(ff, N, dmin, tmin);
		outfile<<setiosflags(ios::fixed);
		outfile<<setprecision(8);
		outfile<<"Case #"<<i + 1<<": "<<dmin<<" "<<tmin<<endl;
		delete ff;
	}

	infile.close();
	outfile.close();
}
