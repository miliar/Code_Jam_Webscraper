#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <time.h>
#include <vector>
#include <time.h>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <stdio.h>
#define all(c) c.begin(), c.end() 
#define PI 3.141592653
#define PAUSE system("pause")
#define FOR(i,j) for(int i=0;i<j;i++)
#define VI vector<int> 
#define VS vector<string>
#define MAX(i,j) i>j? i:j
#define SZ(i) i.size()
using namespace std;

ifstream input("C:/Users/Yeqi SUN/Desktop/A-small-attempt0.in");
ofstream output("C:/Users/Yeqi SUN/Desktop/test.out");


typedef pair<int, int> P;
void main(){
	int N,M,T, x, y;
	
	string ss,temp;
	
	input >> T;
	FOR(i, T){
		vector<int> vx, vy;
		vector<P> vP;
		input >> N;
		FOR(j, N){
			input >> x >> y;
			vx.push_back(x);
			vy.push_back(y);
			vP.push_back(make_pair(x,y));
		}
		VI ind(200000,0);
		sort(vy.begin(),vy.end());
		int order  = 1;
		FOR(n, SZ(vy)){
			ind[vy[n]] = order++;
		}
		sort(vP.begin(),vP.end());
		int count = 0;
		FOR(m, SZ(vP)){
			count += abs(m+1- ind[vP[m].second]  );
		}
		output << "Case #" << i+1 << ": " << count/2 << endl;

		

	}







	PAUSE;
}