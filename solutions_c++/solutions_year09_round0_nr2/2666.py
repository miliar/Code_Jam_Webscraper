#include <Windows.h>
#include <iostream>
#include <fstream>
using namespace std;

char basin[26] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
                  'p','q','r','s','t','u','v','w','x','y','z'};

#define IN_FILE "B-large.in"
#define OUT_FILE "B-large.out"
class WaterShed
{
public:
	int height,width;
	int* maps;
	int sinknum;
	char* sinkmaps;
	char sinknull;
public:
	WaterShed();
	WaterShed(int H,int W);
	~WaterShed();
	void ComputeSink();
	void flow(const int i,const int j);
	void setcurrent(int& n,int& ni,int& nj,const int i,const int j);
	void findsides(int& n,int& ni,int& nj,const int i,const int j);
	void setsink(const int ni,const int nj,const int i,const int j);

};
WaterShed::WaterShed(int H, int W)
{
	height = H;
	width = W;
	sinknum =0;
	maps = new int [height*width];
	sinkmaps = new char [height*width];
	sinknull = sinkmaps[1];
}
WaterShed::~WaterShed()
{
	height = width = sinknum = 0;
	delete maps;
	delete sinkmaps;
}
void WaterShed::ComputeSink()
{
	sinkmaps[0] = basin[0];
	for (int i=0;i<height;i++)
	{
		for(int j=0;j<width;j++)
		{
			flow(i,j);
		}
	}
}
void WaterShed::flow(const int i,const int j)
{    
	if (sinkmaps[i*width+j]!=sinknull)
	{
		int n,ni,nj;
		setcurrent(n,ni,nj,i,j);
		findsides(n,ni,nj,i,j);
		sinkmaps[ni*width+nj] = sinkmaps[i*width+j];
		if (ni!=i||nj!=j)
		{
		   flow(ni,nj);
		}
	}
	else
	{
		int n,ni,nj;
		setcurrent(n,ni,nj,i,j);
		findsides(n,ni,nj,i,j);
        if (sinkmaps[ni*width+nj]!=sinknull)
        {
			sinkmaps[i*width+j] = sinkmaps[ni*width+nj];
		}else
		{
		if (ni==i&&nj==j)
		{
			sinknum = sinknum+1;
			sinkmaps[i*width+j] = basin[sinknum];
		}else{
			flow(ni,nj);
            sinkmaps[i*width+j] = sinkmaps[ni*width+nj];
		}
		}
	}
}

void WaterShed::findsides(int& n,int& ni,int& nj,const int i,const int j)
{
	if (i-1>=0&&maps[(i-1)*width+j]<n)
	{
		setcurrent(n,ni,nj,i-1,j);
	}
	if (j-1>=0&&maps[i*width+j-1]<n)
	{
		setcurrent(n,ni,nj,i,j-1);
	}
	if (j+1<width&&maps[i*width+j+1]<n)
	{
		setcurrent(n,ni,nj,i,j+1);
	}
	if (i+1<height&&maps[(i+1)*width+j]<n)
	{
		setcurrent(n,ni,nj,i+1,j);
	}
	
}
void WaterShed::setcurrent(int &n, int &ni, int &nj, const int i, const int j)
{
	n = maps[i*width+j];
	ni = i;
	nj = j;
}
int main(int argc, char **argv)
{
	int caseNum;
	int H,W;
    ifstream in(IN_FILE);
	ofstream out(OUT_FILE);
    in >> caseNum;
	for (int n=0;n<caseNum;n++)
	{
		in >>H;
		in >>W;
		WaterShed water(H,W);
		for (int i=0;i<H;i++)
		{
			for (int j=0;j<W;j++)
			{
				in >> water.maps[i*W+j];
			}
		}

        water.ComputeSink();
		out << "Case #" << n+1 << ":"<< "\n";
		for (int i=0;i<H;i++)
		{
			for (int j=0;j<W;j++)
			{
				out << water.sinkmaps[i*W+j] << ' ';
			}
			out << "\n";
		}
	}
	return 0;
}
