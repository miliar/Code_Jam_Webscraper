#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <cmath>
#include <iomanip>
using namespace std;

struct ffT {
	int x;
	int y;
	int z;
	int vx;
	int vy;
	int vz;
};

int main (int argc, char * const argv[]) {
    cout << "Input file name: ";
	string filename;
	getline(cin, filename);
	
	cout << "Output file name: ";
	string outFileName;
	getline(cin, outFileName);
	
	ofstream out;
	out.open(outFileName.c_str());
	
	ifstream in;
	in.open(filename.c_str());
	
	if(in.fail()) {
		cout << "File not found" << endl;
		exit(1);
	}
	
	string params;
	getline(in, params);
	stringstream paramsStream;
	paramsStream << params;
	
	int T;
	
	paramsStream >> T;
	
	out << fixed << setprecision(8);
	for(int i = 0; i < T; i++) {
		out << "Case #" << i + 1 << ": ";
		string number;
		getline(in, number);
		stringstream numberStream;
		numberStream << number;
		
		int N;
		numberStream >> N;
		
		ffT net = {0,0,0,0,0,0};
		
		for(int j = 0; j < N; j++) {
			string values;
			getline(in, values);
			stringstream valueStream;
			valueStream << values;
			
			ffT f;
			
			valueStream >> f.x >> f.y >> f.z >> f.vx >> f.vy >> f.vz;
			
			net.x += f.x;
			net.y += f.y;
			net.z += f.z;
			net.vx += f.vx;
			net.vy += f.vy;
			net.vz += f.vz;
		}
		
		/* The following formula was derived using Mathematica, with the input
		 * Solve[D[Sqrt[(vx*t + x)^2 + (vy*t + y)^2 + (vz*t + z)^2], t] == 0, t]
		 *
		 * This takes the derivative of the distance and solves for the time it is zero.
		 * I could have derived this by hand given a bit more time :)
		 */
		
		//double time = -(netvx * netx + netvy * nety + netz * netvz)/(netvx * netvx + netvy * netvy + netvz * netvz);
		
		double time = 0;
		
		int num = -(net.vx * net.x + net.vy * net.y + net.z * net.vz);
		int denom = (net.vx * net.vx + net.vy * net.vy + net.vz * net.vz);
		if(num > 0 && denom != 0)
			time = (double) num / denom;
		
		 double netx = (double) net.x / N;
		 double nety = (double) net.y / N;
		 double netz = (double) net.z / N;
		 double netvx = (double) net.vx / N;
		 double netvy = (double) net.vy / N;
		 double netvz = (double) net.vz / N;
		
		
		double posx = netvx * time + netx;
		double posy = netvy * time + nety;
		double posz = netvz * time + netz;
		
		double dist = sqrt(posx * posx + posy * posy + posz * posz);
		out << dist << " " << time << endl;
		
	}
	
	cout << "Done!";
	string dummy;
	getline(cin, dummy);
    return 0;
}




