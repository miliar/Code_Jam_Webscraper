#include <iostream>
#include <fstream>
using namespace std;

int main(int argc,char **argv)
{
	if(argc != 3){
		cout<<"usage : snapper input output"<<endl;
	}
	const char *input = argv[1];
	const char *output = argv[2];
	ifstream in(input);
	ofstream out(output);
	
	size_t times = 0;
	in>>times;
	
	int R[times];
	int N[times];
	int K[times];
	int money[times];
	int *g;
	for(int i = 0;i < times;++i){
		in>>R[i]>>K[i]>>N[i];
		g = new int[N[i]];
		for(int j = 0;j < N[i];++j){
			in>>g[j];
		}
		money[i] = 0;
		//compute the money
		int current = 0;
		for(int t = 0;t < R[i];++t){
			int people = 0;
			int counter = 0;
			while(people <= K[i]){
				people += g[ current % N[i] ];
				++counter;
				++current;
				if(counter > N[i]){
					//people  += g[0];
					break;
				}
			}
			--current;
			money[i] += people - g[current % N[i]];
		}
		delete []g;
	}
	
	//output
	for(int i = 1;i <= times;++i){
		out<<"Case #"<<i<<": ";
		out<<money[i-1]<<endl;
	}
	return 0;
}
