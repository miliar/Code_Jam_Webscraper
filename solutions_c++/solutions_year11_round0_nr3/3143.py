#include <vector>
#include <iostream>

#define MAX(a,b) ((a)>(b)?(a):(b))

int splitCandy(std::vector <int> &candy, std::vector <int> &cS, std::vector <int> &cP){


 long sumSP=0, sumPP=0, sumSS=0;
 if(candy.empty()){
	if (cS.empty() || cP.empty()) return -1;
	unsigned i;
	for(i=0;i<cS.size();i++){
		sumSP = sumSP ^ cS[i];
		sumSS = sumSS + cS[i];
		}
	for(i=0;i<cP.size();i++)
		sumPP = sumPP ^ cP[i];
	if (sumPP != sumSP) return -1;
		else return sumSS;
	}

 int aC = candy.back();
 candy.pop_back();
 int rS, rP;
 cS.push_back(aC);
 rS = splitCandy(candy, cS, cP);
 cS.pop_back();
 cP.push_back(aC);
 rP = splitCandy(candy, cS,cP);
 cP.pop_back();
 candy.push_back(aC);

return MAX(rP,rS);
}

int main(int argc, char ** argv){

std::vector <int> candy;
std::vector <int> candySean;
std::vector <int> candyPatrick;

unsigned i,j, T, N, C;
long res;
std::cin >> T;

for(i=0;i<T;i++){
	candy.clear();
	candySean.clear();
	candyPatrick.clear();
	std::cin >> N;
	for(j=0;j<N;j++){
		std::cin >> C;
		candy.push_back(C);
		}
	res = splitCandy(candy,candySean,candyPatrick);
	std::cout << "Case #"<< i+1 <<": ";
	if (res == -1) std::cout<< "NO\n";
		else std::cout <<res <<std::endl;

}

return 0;
}
