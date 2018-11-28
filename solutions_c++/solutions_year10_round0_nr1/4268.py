#include <iostream>
#include <fstream>
using namespace std;

typedef struct snapper{
	bool power;
	bool on;
}snapper_t;

int main(int argc,char **argv)
{
	if(argc != 3){
		cout<<"usage : snapper input output"<<endl;
	}
	const char *input = argv[1];
	const char *output = argv[2];
	ifstream in(input);
	ofstream out(output);
	size_t times =0;
	int current = 0;
	in>>times;
	int N,K;
	while(times--){
		in>>N>>K;
		snapper_t snap[N];
		//init the snappers
		for(int i = 0;i < N;++i){
			snap[i].power = false;
			snap[i].on = false;
		}
		snap[0].power = true;	
		
		for(int i = 0;i < K;++i){
			for(int j = 0;j < N;++j){
				if(snap[j].power)
					snap[j].on = snap[j].on ? false : true;
			}
			for(int j = 0;j < N-1;++j){
				if(snap[j].power && snap[j].on)
					snap[j+1].power = true;
				else snap[j+1].power = false;
			}
		}
		++current;
		//output
		out<<"Case #"<<current<<": ";
		if(snap[N-1].power &&snap[N-1].on){
			out<<"ON"<<endl;
		}else{
			out<<"OFF"<<endl;
		}
	}
	return 0;
}
