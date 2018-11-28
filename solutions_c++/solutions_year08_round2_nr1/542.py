#include <iostream>
#include <vector>
#include <fstream>
#include <math.h>
#include <stdio.h>


using namespace std;

typedef vector<long long> VL;

int Solve(VL & first, VL & second){
		int result = 0;
		int size = first.size();
		
		for (int i = 0; i < size; i++){
			for (int j = i+1; j < size; j++){
				for (int k = j+1; k < size; k++){
					long double sum_1 = (first[i] + first[j] + first[k])/(3.0);
					long double sum_2 = (second[i] + second[j] + second[k])/(3.0);
					
					long double intpart;

					if (modf(sum_1, &intpart) == 0 && modf(sum_2, &intpart) == 0) result++;
				}
			}
		}

		return result;
}

int main(){
	int n = 1;
	int m;
	ifstream infile("a-small.in");
	ofstream outfile("a-small.out");

	infile >> m;

	if (n == 0) return 0;

	while (n <= m){
		int l;
		unsigned long long A, B, C, D, x_0, y_0, M; 
		infile >> l;
		infile >> A;
		infile >> B;
		infile >> C;
		infile >> D;
		infile >> x_0;
		infile >> y_0;
		infile >> M;

		VL first;
		VL second;

		for (int i = 0; i < l; i++){
			first.push_back(0);
			second.push_back(0);
		}

		first[0] = x_0;
		second[0] = y_0;

		for (int j = 1; j < l; j++){
			first[j] = (A*first[j-1] + B)%M;
			second[j] = (C*second[j-1] + D)%M;

			//outfile << j << " " << first[j] << " " << second[j] << endl;
		}


		outfile << "Case #" << n << ": " << Solve(first, second) << endl;
		n++;
	}

	infile.close();
	outfile.close();

	return 0;
}