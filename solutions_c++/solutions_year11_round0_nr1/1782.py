#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <vector>
#include <stdlib.h>
#include <cmath>

using namespace std;
 
#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)

int main(){
	//get inputs

	int ncase = 0;
	cin >> ncase;


	for(int icase = 0; icase<ncase; icase++){
		int N;
		cin >> N;

		int dis[N];
		char color[N];
		int orapos = 1;
		int bluepos = 1;
		int orastep = 0;
		int bluestep = 0;

		for(int i = 0; i < N; i++){
			cin >> color[i] >> dis[i];
		}


		int sum = 0;

		for(int i = 0; i<N; i++){
			if(color[i] == 'O'){
				int dist = dis[i] - orapos;
				if(dist < 0)
					dist = -dist;
				if(dist - orastep <0) 
					dist = 0;
				else
					dist = dist - orastep;
				sum += dist +1;
				bluestep += dist+1;
				orastep = 0;
				orapos = dis[i];
			}else{
				int dist = dis[i] - bluepos;
				if(dist < 0)
					dist = -dist;
				if(dist - bluestep <0) 
					dist = 0;
				else
					dist = dist - bluestep;
				sum += dist +1;
				orastep += dist +1;
				bluestep = 0;
				bluepos = dis[i];	
			}
		}	

		cout << "Case #" << icase+1 << ": "; 
		cout << sum;
		cout << endl;
	}


	return 0;
}
