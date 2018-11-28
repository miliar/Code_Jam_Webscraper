#include <iostream>
#include <fstream>
#include <vector>
#include <utility>
#include <algorithm>
#include <cmath>
#include <math.h>
using namespace std;

int main()
{
	ifstream in("B-large.in");
	ofstream out("output1.txt");
	vector <int> v;
	vector <pair <int, int> > notDone;
	int T; in>>T;
	int temp;
	int maxCount=0;
	for (int m =0 ; m<T ; m++){
		maxCount=0;
		int N; in>>N;
		int S; in>>S;
		int P; in>>P;
		int min1 = max((3*P) -2,0);
		int min2 = max ((3*P) -4,0);
		for (int j =0;j<N;j++){
			in>>temp;
			// ana 3ayez azabat 7etet el zeros de 
			// 2 1 1 8 0 
			if (temp >= min1 && P<=temp){
				maxCount++;
			}else if (S!=0){
				if (temp>= min2 && P<=temp){
				maxCount++;
				S--;
				}
			}
			
		}
		out << "Case #"<<m+1<<": "<<maxCount<<endl;
		cout << "Case #"<<m+1<<": "<<maxCount<<endl;

	}
}



/*
			int c = ceil(v[i]/3.0);
			int f = floor(v[i]/3.0);
			temp = v[i]-(c+f);
			if (c>= P || f>=P || temp >=P){
				maxCount++;
				
			}else if (P-c == 1 && S!=0 && c!=0 ){
					maxCount++;
					S--;
			}
		}
		v.empty();
		v.clear();
		*/