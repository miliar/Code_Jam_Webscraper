#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;

long max(long, long);

ifstream infile;
ofstream outfile;
int main(){
	infile.open("A-large.in");
	outfile.open("result.txt");
	int t;
	int n;
	infile >> t;
	long time[2], pos[2];
	int new_pos, robot;
	char new_robot;
	for( int it=0; it <t; it++){
		infile>> n;
		time[0] = time[1] = 0;
		pos[0]  = pos[1]  = 1;
		for (int in = 0 ; in < n; in++){
			infile>> new_robot>> new_pos;
			if (new_robot == 'O') 
				robot = 0;
			else robot = 1;

			time[robot] = time[robot] + max(time[1-robot]- time[robot], abs(new_pos - pos[robot]))+1;
			pos[robot]  = new_pos;
		}
		outfile << "Case #" << it+1 <<": "<< max(time[0],time[1]) << endl;
	}

}

long max(long x, long y){
	return (x>y?x:y);
}