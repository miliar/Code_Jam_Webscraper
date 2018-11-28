#include <iostream>
#include <cstdlib>
#include <string>
#include <stdio.h>
#include <cmath>

using namespace std;
#define COUT cout

#define PI 3.14159265

int main(int argc, char * argv[]) {

	if(argc != 2) {
		cout << "usage: program_name input_file" << endl;
		exit(1);
	}
	
	FILE * fp = fopen(argv[1],"r");
	if(!fp) {
		cout << "input file " << argv[1] << " not exists" << endl;
		exit(2);
	}
	
	int num_testcase;
	char buffer[256];
	fgets(buffer, 256, fp);
	sscanf(buffer,"%d",&num_testcase); // 1st line
	//COUT << "num_testcase: " << num_testcase << endl;
	for(int i = 0; i < num_testcase; i++) {
		double f, R, t, r, g, totalarea, area = 0.0;
		fgets(buffer, 256, fp);
		sscanf(buffer,"%lf %lf %lf %lf %lf",&f,&R,&t,&r,&g); // 2rd line
		
		// total area  (quarter of the circle)
		totalarea = PI * R * R / 4.0;
		
		// radius correction
		R = R - t - f;
		r = r + f;
		g = g - f - f;
		
		if(R <= 0 || g <= 0) {
			area = 0;
		} else {
		// get circle points		
		double linestartx[1000];
		double lineendx[1000];
		double linestarty[1000];
		double lineendy[1000];
		linestartx[0] = r;
		lineendx[0] = (r + g < R)?(r + g):(R);
		int num_linept = 1;
		while(lineendx[num_linept - 1] + r + r < R) {
			linestartx[num_linept] = lineendx[num_linept - 1] + r + r;
			lineendx[num_linept] = (linestartx[num_linept] + g < R)?(linestartx[num_linept] + g):(R);
			num_linept++;
		}
		for(int j = 0; j < num_linept; j++) {
			linestarty[j] = sqrt(R * R - linestartx[j] * linestartx[j]);
			lineendy[j] = sqrt(R * R - lineendx[j] * lineendx[j]);
		}
		
		// combine both directions
		double bothstartx[2000];
		double bothendx[2000];
		double bothstarty[2000];
		double bothendy[2000];
		int num_bothpt = 0;
		int currentx = 0, currenty = num_linept - 1;
		
		//for(int j = 0; j < num_linept; j++) {
			//cout << "line : " << linestartx[j] << "," << linestarty[j] << " - " << lineendx[j] << "," << lineendy[j] << endl;
		//}

		while(currentx < num_linept && currenty >= 0) {
			if(linestartx[currentx] <= lineendy[currenty] &&
			   lineendx[currentx] > lineendy[currenty] &&
			   lineendx[currentx] <= linestarty[currenty]) {
			    //cout << "case 1" << endl;
				bothstartx[num_bothpt] = lineendy[currenty];
				bothstarty[num_bothpt] = lineendx[currenty];
				bothendx[num_bothpt] = lineendx[currentx];
				bothendy[num_bothpt] = lineendy[currentx];
				num_bothpt++;
				currentx++;
			} else if(lineendy[currenty] <= linestartx[currentx] &&
			   linestarty[currenty] > linestartx[currentx] &&
			   linestarty[currenty] <= lineendx[currentx]) {
			    //cout << "case 2" << endl;
				bothstartx[num_bothpt] = linestartx[currentx];
				bothstarty[num_bothpt] = linestarty[currentx];
				bothendx[num_bothpt] = linestarty[currenty];
				bothendy[num_bothpt] = linestartx[currenty];
				num_bothpt++;
				currenty--;
			} else if(lineendx[currentx] <= linestarty[currenty] &&
					  linestartx[currentx] >= lineendy[currenty]) {
			    //cout << "case 3" << endl;
				bothstartx[num_bothpt] = linestartx[currentx];
				bothstarty[num_bothpt] = linestarty[currentx];
				bothendx[num_bothpt] = lineendx[currentx];
				bothendy[num_bothpt] = lineendy[currentx];
				num_bothpt++;
				currentx++;
			} else if(linestartx[currentx] <= lineendy[currenty] &&
			          linestarty[currenty] <= lineendx[currentx]){
			    //cout << "case 4" << endl;
				bothstartx[num_bothpt] = lineendy[currenty];
				bothstarty[num_bothpt] = lineendx[currenty];
				bothendx[num_bothpt] = linestarty[currenty];
				bothendy[num_bothpt] = linestartx[currenty];
				num_bothpt++;
				currenty--;
			} else if(lineendx[currentx] <= lineendy[currenty]) {
				currentx++;
			} else if(linestartx[currentx] >= linestarty[currenty]){
				currenty--;
			} else {
				cout << "error " << linestartx[currentx] << "," << lineendx[currentx]
				     << " & " << lineendy[currenty] << "," << linestarty[currenty] << endl;
			}
		}
		
		//while(currentx < num_linept) {
		//	bothstartx[num_bothpt] = linestartx[currentx];
		//	bothstarty[num_bothpt] = linestarty[currentx];
		//	bothendx[num_bothpt] = lineendx[currentx];
		//	bothendy[num_bothpt] = lineendy[currentx];
		//	num_bothpt++;
		//	currentx++;
		//}
		
		//while(currenty >= 0) {
		//	bothstartx[num_bothpt] = lineendy[currenty];
		//	bothstarty[num_bothpt] = lineendx[currenty];
		//	bothendx[num_bothpt] = linestarty[currenty];
		//	bothendy[num_bothpt] = linestartx[currenty];
		//	num_bothpt++;
		//	currenty--;
		//}
		
		for(int j = 0; j < num_bothpt; j++) {
			//cout << "both : " << bothstartx[j] << "," << bothstarty[j] << " - " << bothendx[j] << "," << bothendy[j] << endl;
		}
		
		// calculate area
		for(int j = 0; j < num_bothpt; j++) {
			double this_angle = asin(bothendx[j] / R) - asin(bothstartx[j] / R);
			//cout << "angle = " << this_angle << endl;
			double this_area = 0.5 * (R * R * this_angle - 
				(bothstartx[j] * bothstarty[j] + bothendx[j] * bothendy[j]
				 - 2 * bothstartx[j] * bothendy[j] /*- bothendx[j] * bothstarty[j]*/));
			//cout << "add(arc) " << this_area << " = " << (R * R * this_angle) << " - " << (bothstartx[j] * bothstarty[j] + bothendx[j] * bothendy[j] - 2 * bothstartx[j] * bothendy[j] /*- bothendx[j] * bothstarty[j]*/) << endl;
			area += this_area;
		}
		
		for(double x = r; x < R; x += r + r + g) {
			for(double y = r; y < R; y += r + r + g) {
				if((x * x + y * y) > (R * R)) {
					// no area
				} else if((x * x + (y + g) * (y + g)) > (R * R) &&
				          ((x + g) * (x + g) + y * y) > (R * R)){
					// arc only
				} else if((x * x + (y + g) * (y + g)) > (R * R) &&
				          ((x + g) * (x + g) + y * y) < (R * R)) {
					double dy = sqrt(R * R - (x + g) * (x + g));
					double this_area = g * (dy - y);
					//cout << "add(1) " << this_area << endl;
					area += this_area;
				} else if((x * x + (y + g) * (y + g)) < (R * R) &&
				          ((x + g) * (x + g) + y * y) > (R * R)) {
					double dx = sqrt(R * R - (y + g) * (y + g));
					double this_area = g * (dx - x);
					//cout << "add(2) " << this_area << endl;
					area += this_area;
				} else if((x + g) * (x + g) + (y + g) * (y + g) > (R * R)) {
					double dy = sqrt(R * R - (x + g) * (x + g));
					double dx = sqrt(R * R - (y + g) * (y + g));
					double this_area = g * g - (x + g - dx) * (y + g - dy);
					//cout << "add(3) " << this_area << endl;
					area += this_area;
				} else {
					double this_area = g * g;
					//cout << "add(4) " << this_area << endl;
					area += this_area;
				}
			}
		}
		
		}
		
		//cout << "area = 1 - "  << area << "/" << totalarea << endl;
		
		cout << "Case #" << (i+1) << ": " << (1 - (area / totalarea)) << endl;
	}
	
	return 0;
	
}
