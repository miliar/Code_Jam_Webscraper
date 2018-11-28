//============================================================================
// Name        : watersheds.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>

using namespace std;

int map[100][100];
char drain_map[100][100];
int main() {

	int n;

	ifstream fcin;
	ofstream fcout;
	fcout.open("B.out");
	fcin.open("B-large.in");
//	fcin.open("B-small.in");
	fcin >> n;
	for(int i = 0 ; i < n ; ++i )
	{
		int h,w;
		fcin >> h >> w;
		for(int j = 0 ; j < h ; ++j )
		{
			for(int k = 0 ; k < w ; ++k)
			{
				fcin >> map[j][k];
				drain_map[j][k]=0;
			}
		}
		char label_letter = 'a';
		for(int j = 0 ; j < h ; ++j)
		{
			for(int k = 0 ; k < w ; ++k)
			{
				if(drain_map[j][k]==0){
					if( j == 0 && k == 0 ) drain_map[j][k] = label_letter;
					int sink_j=j;
					int sink_k=k;
					while(true)
					{
						int current = map[sink_j][sink_k];
						int next_j=sink_j,next_k=sink_k;
						if(sink_j > 0 && map[sink_j-1][sink_k] < current){
							current = map[sink_j-1][sink_k];
							next_j = sink_j-1;
							next_k = sink_k;
						}
						if(sink_k > 0 && map[sink_j][sink_k-1] < current){
							current = map[sink_j][sink_k-1];
							next_j = sink_j;
							next_k = sink_k-1;
						}
						if(sink_k < w-1 && map[sink_j][sink_k+1] < current){
							current = map[sink_j][sink_k+1];
							next_j = sink_j;
							next_k = sink_k+1;
						}
						if(sink_j < h-1 && map[sink_j+1][sink_k] < current){
							current = map[sink_j+1][sink_k];
							next_j = sink_j+1;
							next_k = sink_k;
						}
						if(sink_j==next_j && sink_k==next_k){
							if(drain_map[j][k]!=0){
								drain_map[sink_j][sink_k] = drain_map[j][k];
							}else if(drain_map[sink_j][sink_k]!=0){
								drain_map[j][k] = drain_map[sink_j][sink_k];
							}else{
								++label_letter;
								drain_map[sink_j][sink_k] = label_letter;
								drain_map[j][k] = label_letter;
							}
							break;
						}
						sink_j = next_j; sink_k = next_k;
					}
				}
			}
		}
		fcout << "Case #" << i+1 << ":" << endl;
		for(int j = 0 ; j < h ; ++j )
		{
			for(int k = 0 ; k < w ; ++k )
			{
				if(k != 0) fcout << " ";
				fcout << drain_map[j][k];
			}
			fcout << endl;
		}
	}
	return 0;
}
