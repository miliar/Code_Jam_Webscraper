// Made by KIA :) 
#include <fstream>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <deque>
#include <math.h>
#include <bitset>
#include <stdio.h>

using namespace std;

FILE* in = fopen("D.in","r");
FILE* out = fopen("D.out","w");

struct plant{
	int X,Y,R;
};

int main(){
	int testnum = 0;
	
	fscanf(in,"%d", &testnum);
	int NPlant = 0;
	vector<plant> pl;
	for(int test = 0; test < testnum; ++test){
		pl.clear();
		fscanf(in, "%d", &NPlant);
		for(int i=0; i< NPlant; ++i){
			plant P;
			fscanf(in,"%d %d %d", &P.X, &P.Y, &P.R);
			pl.push_back(P);
		}
		double Rad;
		switch(NPlant){
			case 1: Rad = pl[0].R;
				break;
			case 2: Rad = pl[0].R > pl[1].R?pl[0].R:pl[1].R;
				break;
			case 3: 
				Rad = 1e100;
				for(int i=0; i<3; ++i){
					double CurRad, dist;
					int i1=0,i2=0;
					while(i1 == i){i1++;}
					while(i2 == i || i2 == i1){i2++;}
					plant P1 = pl[i1], P2 = pl[i2];
					dist = P1.R+P2.R+sqrt((double)(P1.X-P2.X)*(P1.X-P2.X)+(P1.Y-P2.Y)*(P1.Y-P2.Y));
					CurRad = pl[i].R>dist?pl[i].R:dist;
					Rad = Rad<CurRad? Rad:CurRad;
				}
				Rad/=2;
				break;
		}
		fprintf(out,"Case #%d: %f\n", test+1, Rad);
	}
	fprintf(out, "\n");
	return 0;
}