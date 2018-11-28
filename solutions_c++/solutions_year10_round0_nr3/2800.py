
#include <iostream>
#include <fstream>

using namespace std;

int main(){
	ifstream input("inputC.txt");
	ofstream output("outputC.txt");
	size_t T;
	input >> T;
	size_t R,k,N,next,freePlaces,startFrom;
	size_t *g;
	unsigned __int64 money = 0;
	g = new size_t[10000000];
	for(size_t i = 0; i < T;i++){
		input >> R >> k >> N;
		for(size_t j = 0; j < N;j++){
			input >> g[j];
		}
		money = 0;
		next = 0;
		for(size_t j = 0; j < R;j++){
			freePlaces = k;
			startFrom = next;
			do{
				freePlaces -= g[next];
				next = (next+1)%N;
			}while(g[next] <= freePlaces && next != startFrom);
			money += k - freePlaces;
		}
		output << "Case #"<<(i+1)<<": " << money << "\n";
	}
	return 0;
}