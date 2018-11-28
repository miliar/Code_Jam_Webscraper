#include <fstream>
#include <iostream>
#include <algorithm>
#include <cstdlib>
using namespace std;
ifstream in("input.txt");
ofstream out("output.txt");

long long cases, students, width, height;
long long student[1000], location[1000][2];
int pos[1000];
long long output[1000][2];

void ksort(){
	bool seen[1000];
	for(int i = 0; i < 1000; i++) seen[i] = false;
	
	for(int i = 0; i < students; i++){
		long long low = (1ll<<50);
		for(int k = 0; k < students; k++){
			if(seen[k]) continue;
			if(student[k] < low){
				pos[i] = k;
				low = student[k];
			}	
		}
		seen[pos[i]] = true;
	}
	sort(student,student+students);
}

bool canplace(long long x, long long y, long long size){
	for(int i = 0; i < students; i++){
		if( ((x-size)<location[i][0]+student[i]) + (x+size>location[i][0]-student[i]) == 2){
			if( ((y-size)<location[i][1]+student[i]) + (y+size>location[i][1]-student[i]) == 2){
				return false;
			}
		}
	}
	return true;
}

int main(){
	in>>cases;
	for(int i = 1; i <= cases; i++){
		cout<<i<<"\n";
		in>>students>>width>>height;
		for(int j = 0; j < students; j++) in>>student[j];
		ksort();
		for(int j = 0; j < students; j++) location[j][0] = location[j][1] = -1000000;
		//we now have it in ascending order. Treat like boxes. Go from largest to smallest.
		for(int j = students-1; j >= 0; j--){
			bool placed = false;
			while(!placed){
				long long x = ((long long)rand()*10000+rand())%(width), y = ((long long)rand()*10000+rand())%(height);
				if(canplace(x,y,student[j])){
					placed = true;
					location[j][0] = x;
					location[j][1] = y;
				}
			}
		}
		for(int j = 0; j < students; j++){
			output[pos[j]][0] = location[j][0];
			output[pos[j]][1] = location[j][1];
		}
		out<<"Case #"<<i<<": ";
		for(int j = 0; j < students; j++) out<<output[j][0]<<" "<<output[j][1]<<" ";
		out<<"\n";
	}
}