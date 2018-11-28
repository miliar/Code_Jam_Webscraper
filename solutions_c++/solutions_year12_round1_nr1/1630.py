#include <iostream>
#include <string>
#include <sstream>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;

template<class T> T** new2(int m, int n);
template<class T> void delete2(T** arr);

double solve(double* p, int a, int b)
{
	double ans = 0.0;
	double* option = new double[a];
	double pressEnter = 0.0;
	for(int i = 0; i < a; i++){
		option[i] = 0.0;
	}
	// solve case	
	for(int i = 0; i < a; i++){		
		double prob = 1.0;
		for(int j = 0; j < i; j++){			
			prob *= p[j];
		}
		prob *= 1.0-p[i];
		//std::cout << "prob=" << prob << std::endl;
		
		int* cost = new int[a];
		for(int j = 0; j < a; j++){
			cost[j] = j;
			cost[j] += b-(a-j)+1;
			int back = a-i;
			if(j != back){
				cost[j] += b+1;
			}
		}
		
		for(int j = 0; j < a; j++){
			//std::cout << "cost[" << j << "]=" << cost[j] << std::endl;
			option[j] += prob*cost[j];
		}		
		delete[] cost;
	}
	
	double allP = 1.0;
	for(int i = 0; i < a; i++){
		allP *= p[i];
	}
	for(int j = 0; j < a; j++){
		int stroke = j+(b-(a-j)+1);
		//std::cout << "if all correct, type back " << j << " needs " << stroke << std::endl;
		option[j] += allP*stroke;
	}
	
	ans = b+2;
	//std::cout << "pressEnter=" << ans << std::endl;
	for(int i = 0; i < a; i++){
		//std::cout << "option[" << i << "]=" << option[i] << std::endl;
		if(ans > option[i]){
			ans = option[i];
		}
	}
	delete[] option;
	return ans;
}

int main(int argc, char* argv[]){
	char* temp = 0;
	std::string line;
	std::getline(std::cin, line);
	int z = strtol(line.c_str(), &temp, 0);
	for(int c = 1; c <= z; c++){
		// read case
		std::getline(std::cin, line);
		std::istringstream src(line);
		
		int a, b;
		src >> a >> b;
		double* p = new double[a];
		std::getline(std::cin, line);
		std::istringstream src0(line);
		for(int i = 0; i < a; i++){
			src0 >> p[i];
		}
		
		double ans = solve(p, a, b);
		std::cout << "Case #" << c << ": " << ans << std::endl;
		delete[] p;
	}
	return 0;
}

template<class T>
T** new2(int m, int n)
{
	T* buf = new T[m*n];
	T** arr = new T*[m];
	for(int i = 0; i < m; i++){
		arr[i] = buf+(i*m);
	}
	return arr;
}

template<class T>
void delete2(T** arr)
{
	T* ptr = arr[0];
	delete[] arr;
	delete[] ptr;
	return;
}
