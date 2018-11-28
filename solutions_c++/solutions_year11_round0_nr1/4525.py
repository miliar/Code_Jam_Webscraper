// codejam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int debug = 0;
	//output file handler
	ofstream outputFile;
	//outputFile.open("A-small-attempt0-2.out");
	outputFile.open("A-large.out");
	if(!outputFile.is_open()){
		cout<<"Can't open output file"<<endl;
		char c;
			cin>>c;
		return -1;
	}

	//open the input file
	//ifstream inputFile("in.txt",ifstream::in);
	//ifstream inputFile("A-small-attempt0.in",ifstream::in);
	ifstream inputFile("A-large.in",ifstream::in);
	if(!inputFile.is_open()){
		cout<<"Can't open input file"<<endl;
		char c;
			cin>>c;
		return -1;
	}

	//reading input file
	int numTestCase;
	inputFile >> numTestCase;

	for(int i=0;i<numTestCase;++i){
		int num;
		inputFile >> num;

		int p; char r;
		int curr_pos[2];
		curr_pos[0] = 1;
		curr_pos[1] = 1;
		vector<int> button_list;
		vector<int> robot_color;

		vector<int> robot_button[2];

		for(int j=0;j<num;j++){
			inputFile >> r >> p;
			if(r=='O'){ 
				robot_color.push_back(0);
				robot_button[0].push_back(p);
			}
			else{ 
				robot_color.push_back(1);
				robot_button[1].push_back(p);
			}
			button_list.push_back(p);


		}

		int count = 0;
		size_t robot_next[2];
		robot_next[0] = 0;
		robot_next[1] = 0;
		for(int j=0; j<num;++j)
		{
			while(1){
				int r1 = robot_color[j];
				int r2 = 1-r1;
				if(curr_pos[r1]==button_list[j]){
					robot_next[r1]++;
					//push button
					if(robot_next[r2]<robot_button[r2].size()){
						if(curr_pos[r2]<robot_button[r2].at(robot_next[r2])) curr_pos[r2]++;
						else if(curr_pos[r2]>robot_button[r2].at(robot_next[r2]))curr_pos[r2]--;
					}
					count++;
					break;
				}
				else{
					int d1, d2;
					if(robot_next[r1]<robot_button[r1].size())
						d1 = abs(curr_pos[r1] - robot_button[r1].at(robot_next[r1]));
					else
						d1 = 0;
					if(robot_next[r2]<robot_button[r2].size())
						d2 = abs(curr_pos[r2] - robot_button[r2].at(robot_next[r2]));
					else d2 = 0;

					int step;
					if(d1!=0 && d2!= 0)
						step = (d1<d2?d1:d2);
					else
						step = 1;

					if(robot_next[r1]<robot_button[r1].size()){
						if(curr_pos[r1]<robot_button[r1].at(robot_next[r1])) curr_pos[r1]+=step;
						else if(curr_pos[r1]>robot_button[r1].at(robot_next[r1]))curr_pos[r1]-=step;
					}
					if(robot_next[r2]<robot_button[r2].size()){
						if(curr_pos[r2]<robot_button[r2].at(robot_next[r2])) curr_pos[r2]+=step;
						else if(curr_pos[r2]>robot_button[r2].at(robot_next[r2]))curr_pos[r2]-=step;
					}
					count+=step;
				}
				
			
			}
		}

		outputFile << "Case #"<<i+1<<": "<<count<<endl;

	
	}

	outputFile.close();
	inputFile.close();

	return 0;
}

