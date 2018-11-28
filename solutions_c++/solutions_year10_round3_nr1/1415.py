#include <fstream>
#include <map>
#include <iostream>
#include <string>


using namespace std;

int main(){
	ifstream fin("milk2.in");
	ofstream fout("milk2.out");
	int tests;
	fin>>tests;
	
	
	int count;
	for(int i=0;i<tests;i++){
		map<int,int> time;
		map<int,int>::iterator mit;
		count = 0;
		int N;
		fin>>N;
		for(int j=0;j<N;j++){
			int start,end;
			fin>>start>>end;
			
			for(mit=time.begin();mit!=time.end();mit++){
				int first = mit->first;
				int second = time[mit->first];
				if(start<first){
					if(end>second){
						count++;
					}
				}else{
					if(end<second){
						count++;
					}
				}
			}
			time[start] = end;
		}
		fout<<"Case #"<<i+1<<": "<<count<<endl;
	
			
	}
	return 0;
}