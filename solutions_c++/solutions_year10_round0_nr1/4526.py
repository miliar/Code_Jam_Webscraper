#include <stdio.h>
#include <vector>
#include <string>
#include <iostream>

struct Snapper{
	Snapper():power(false), on(false){}

	bool power;
	bool on;
};

void print(const std::vector<Snapper> &v){
	printf("[\n");
	for(int i = 0; i < v.size(); ++i){
		printf("%d:\tPower: %s\t\tON: %s\n", i, (v[i].power ? "YES" : "NO"),  (v[i].on ? "ON" : "OFF"));
	}
	printf("]\n");
	
};

int main(int argc, char* argv[]){

	std::string fileIn = "A_small.txt";

	//std::cout << "Filename: ";
	//std::cin >> fileIn;
	
	FILE* in = fopen(fileIn.c_str(), "r");
	FILE* out = fopen("A_out.txt", "w");
	int T = 0;
	fscanf(in, "%d\n", &T);

	for(int t = 0; t < T; ++t){
		int N = 0, K = 0;
		fscanf(in, "%d %d\n", &N, &K);
		
		std::vector<Snapper> snappers(N);
		snappers[0].power = true;

		for(int k = 0; k < K; ++k){
			//print(snappers);

			for(int s = 0; s < N; ++s){
				if(!snappers[s].power){
					break;
				}
				else{
					snappers[s].on = !snappers[s].on;
				}
			}


			for(int s = 1; s < N; ++s){
				if(snappers[s-1].on && snappers[s-1].power)
					snappers[s].power = true;
				else
					snappers[s].power = false;
			}
		}

		if(snappers.back().on && snappers.back().power){
			fprintf(out, "Case #%d: ON\n", t+1);
			printf("Case #%d: ON\n", t+1);
		}
		else{
			fprintf(out, "Case #%d: OFF\n", t+1);
			printf("Case #%d: OFF\n", t+1);
		}

	}

	fclose(in);
	fclose(out);

	return 0;
}