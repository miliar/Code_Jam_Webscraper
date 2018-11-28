#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <algorithm>
#include <set>
#include <math.h>

using namespace std;


int main()
{
	char filename[16];
	char infile[16], outfile[16];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");

	FILE *inf=fopen(infile, "r"), *outf=fopen(outfile, "w");


	int T;
	fscanf(inf, "%d\n", &T);
   
  
	for(int m=1; m<=T; m++)
	{
	    int N;
		fscanf(inf, "%d\n", &N);

		//vector<vector<int>> vec;

		double sumX, sumY, sumZ;
		double sumVx, sumVy, sumVz;
        sumX = sumY = sumZ = sumVx = sumVy = sumVz = 0;
		for (int i = 0; i < N; i++){
			long temp[6];
			fscanf(inf, "%d %d %d %d %d %d\n", &temp[0], &temp[1], &temp[2], &temp[3], &temp[4], &temp[5]);
			//vec.push_back(vector<int>(temp, temp + 6));
			sumX += temp[0];
			sumY += temp[1];
			sumZ += temp[2];
			sumVx += temp[3];
			sumVy += temp[4];
			sumVz += temp[5];
			//cout <<   sumX  << " " << sumY << " " << sumZ << " " << sumVx << " " << sumVy << " " << sumVz << endl;
		}

       /* sumX = sumX/N; 
		sumY = sumY/N; 
		sumZ = sumZ/N; 
		sumVx = sumVx/N; 
		sumVy = sumVy/N; 
		sumVz = sumVz/N;*/
        double dt;
		double temp = sumVx*sumVx + sumVy*sumVy + sumVz*sumVz;
		if (temp == 0) {
             dt = 0;
		} else{
		     dt = (-1)*(sumX*sumVx + sumY*sumVy + sumZ*sumVz)/(temp);
		}
		if (dt < 0) dt = 0;
 
		double X2 = ((sumX + dt*sumVx)/N); X2 = X2*X2;
		double Y2 = ((sumY + dt*sumVy)/N); Y2 = Y2*Y2;
		double Z2 = ((sumZ + dt*sumVz)/N); Z2 = Z2*Z2;

        double Mt = sqrt(X2 + Y2 + Z2);

		
        fprintf(outf, "Case #%d: %f %f\n", m, Mt, dt);

	}

	fclose(inf); fclose(outf);
	return 0;
}