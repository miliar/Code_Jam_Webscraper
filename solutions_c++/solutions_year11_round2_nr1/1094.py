#include <iostream>
#include <fstream>
#include <string>
#include <vector>
struct team{
	char* results;
	int wins;
	int loses;
};
int main (int argc, char * const argv[]) {
	std::ifstream input("input.txt",std::ios::in);
	std::ofstream output("output.txt",std::ios::out);
	int T;
	input >> T;
	for(int i = 1; i <= T;i++){
		int N;
		input >> N;
		team* x = new team[N];
		for(int j = 0;j < N;j++){
			x[j].results = new char[N];
			for(int k = 0;k < N;k++){
				input >> x[j].results[k];
				if(x[j].results[k] == '0'){
					x[j].loses++;
				}
				if(x[j].results[k] == '1'){
					x[j].wins++;
				}
			}
		}
		double* OOWP = new double[N];
		for(int j = 0;j < N;j++){
			int things = 0;
			for(int k = 0;k < N;k++){
				if(x[j].results[k] == '1'){
					OOWP[j] += x[k].wins/double(x[k].wins+x[k].loses-1);
					things++;
				}
				if(x[j].results[k] == '0'){
					OOWP[j] += (x[k].wins-1)/double(x[k].wins+x[k].loses-1);
					things++;
				}
			}
			OOWP[j] /= things;
		}
		output << "Case #" << i << ":\n";
		for(int j = 0;j < N;j++){
			double v = x[j].wins/double(x[j].wins+x[j].loses)*0.25;
			v += OOWP[j]*0.5;
			int things = 0;
			double q = 0;
			for(int k = 0;k < N;k++){
				if(x[j].results[k] != '.'){
					q += OOWP[k];
					things++;
				}
			}
			v += q/things*0.25;
			output << v << "\n";
		}
	}
	output.flush();
	output.close();
    return 0;
}