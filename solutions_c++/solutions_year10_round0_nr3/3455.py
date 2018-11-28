#include <stack>
#include <utility> 
#include <vector>
#include <queue>
#include <math.h>
#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <fstream>
#include <map>
using namespace std;

double gr[1001];
double sum[1001][1001];

class Lights{
public:
	void onoff(){
	    ifstream input;
		input.open("C-small-attempt1.in",ios::in);
		ofstream output;
		output.open("C-small-attempt1.out",ios::out);
		
		int t;
		input>>t;
		for(int i = 0; i < t; i++){
			long r,k,n;
			input>>r>>k>>n;
			long j;
			for (j = 0; j < n; j++){
				input>>gr[j];
			}
			long a,b;
			sum[0][0] = gr[0];
			for (a = 1; a < n; a++) sum[0][a] = sum[0][a-1] + gr[a];
			for (b = 1; b < n; b++){
				for (a = b; a < n; a++){
					sum[b][a] = sum[b-1][a] - gr[b-1];
				}
			}
			long index = -1;
			double count = 0;
			if (sum[0][n-1] <= k){
				count = sum[0][n-1] * r;
			}
			else{
			for (j = 0; j < r; j++){
				index++;
				if(index >= n){
						index = 0;
				}
				long start = index;
				double acc = sum[start][index];
				while(acc <= k){
					index++;
					if(index >= n){
						index = 0;
					}
					if(index >= start) acc = sum[start][index];
					else acc = sum[start][n-1] + sum[0][index];			
				}
				index--;
				if(index < 0) index = n-1;
		        if(index >= start) count += sum[start][index];
				else count += (sum[start][n-1] + sum[0][index]);
			}
			}
			output<<"Case #"<<i+1<<": "<<count<<endl;
		}
		
		input.close();
		output.close();
		
	};
};


void main()
{
	Lights s;
	s.onoff();
}


/*
	output<<"Case #"<<i+1<<": ";
			for(k = 0; k < arr.size(); k++) output<<arr[k];
			output<<endl;
*/
