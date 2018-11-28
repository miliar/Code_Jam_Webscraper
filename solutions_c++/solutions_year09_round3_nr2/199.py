#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>

using namespace std;

double dis(double x, double y, double z)
{
	return sqrt(x*x+y*y+z*z);
}

int main()
{
	char filename[500] = "K:\\Settings And Documents\\Document\\Visual Studio 2008\\Projects\\Round1A\\Debug\\B";
	char outfile[500];

	//scanf("%s", filename);
	strcpy(outfile, filename);
	strcat(outfile, ".out");
	FILE *ofp=fopen(outfile, "w+");

	int n;
	scanf("%d", &n);
	for(int i=0; i < n; i++)
	{
		int fly;
		int x=0,y=0,z=0,vx=0,vy=0,vz=0;
		
		scanf("%d", &fly);
		for(int j =0; j<fly;j++)
		{
			int tmpx,tmpy,tmpz,tmpvx,tmpvy,tmpvz;
			scanf("%d %d %d %d %d %d", &tmpx,&tmpy,&tmpz,&tmpvx,&tmpvy,&tmpvz);
			x+=tmpx;
			y+=tmpy;
			z+=tmpz;
			vx+=tmpvx;
			vy+=tmpvy;
			vz+=tmpvz;
		}
		double cmx,cmy,cmz,cmvx,cmvy,cmvz;
		cmx = (double)x/(double)fly;
		cmy = (double)y/(double)fly;
		cmz = (double)z/(double)fly;
		cmvx = (double)vx/(double)fly;
		cmvy = (double)vy/(double)fly;
		cmvz = (double)vz/(double)fly;

		double t = (-cmx*cmvx-cmy*cmvy-cmz*cmvz)/(cmvx*cmvx+cmvy*cmvy+cmvz*cmvz);
		if(vx==0&&vy==0&&vz==0) t = 0;
		if(x==0&&y==0&&z==0) t=0;

		if(t < 0)
		{
			fprintf(ofp, "Case #%d: %.8f %.8f\n", i+1, dis(cmx,cmy,cmz), (double) 0);
		}
		else
		{
			fprintf(ofp, "Case #%d: %.8f %.8f\n", i+1, dis(cmx+cmvx*t,cmy+cmvy*t,cmz+cmvz*t), t);
		}
	}
	return 0;
}