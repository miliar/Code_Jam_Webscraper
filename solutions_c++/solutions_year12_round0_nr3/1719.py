//============================================================================
// Name        : fff.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <vector>
using namespace std;


int sizeofint(int value){
	if(value<10)
		return 1;
	if(value<100)
		return 2;
	if(value<1000)
		return 3;
	if(value<10000)
		return 4;

	if(value<100000)
		return 5;
	if(value<1000000)
		return 6;
	if(value<10000000)
		return 7;
	if(value<100000000)
		return 8;
}

int unitofint(int value){
	if(value<10)
		return 1;
	if(value<100)
		return 10;
	if(value<1000)
		return 100;
	if(value<10000)
		return 1000;

	if(value<100000)
		return 10000;
	if(value<1000000)
		return 100000;
	if(value<10000000)
		return 1000000;
	if(value<100000000)
		return 10000000;
}


int mul(int value){
	if(value<1)
		return 0;
	if(value == 1)
		return 1;
	int temp = 0;
	for(;value>0;value--){
		temp+=value;
	}
	return temp;
}

int main() {


	ifstream in;
	ofstream out;
	in.open("in.ini");
	out.open("out.ini");
	int casecount;
	in>>casecount;
	for(int i=0; i<casecount; ++i){
		int start;
		int end;
		in>>start;
		in>>end;
		int number = end-start;
		int count =0;
		if(number<2){
			count = 0;
		}else{
			//int array[number];
			vector<int> array;
			for(int i=0; i<=number; ++i){
				array.push_back(i+start);
				//array[i] = i+start;
			}

			for(int i=0; i<=number; ++i){
				int value = array[i];
				int unit = unitofint(value);
				int size = sizeofint(value);
//				cout << "size "<< size<<endl;
//				cout << "value "<< value<<endl;

				int currentcount = 0;
				//cout << "new round" << endl <<endl;
				for(int j=0; j<size; ++j){
					//cout << "value "<< value<<endl;

					if(value>=start && value<=end){
						//cout << "start "<< start<<endl;
						//cout << "array[value-start] "<< array[value-start]<<endl;
						if(array[value-start]!=0){
							currentcount++;
							//cout << "currentcount "<< currentcount<<endl;
						}
						array[value-start]=0;
					}

					int before = value/10;
					int after = value%10;
					//cout << "unitofint(after) " << unit <<endl;
					value = after*unit+before;
				}
				currentcount--;
				if(currentcount<0)
					currentcount = 0;
				//cout << "currentcount "<< currentcount<<endl;
				//cout << "b3foi4 count"<< count<<endl;
				//cout << "mul(currentcount) "<< mul(currentcount)<<endl;
				count+=mul(currentcount);
				//cout << "count"<< count<<endl;


			}
		}


		out << "Case #" << i+1 << ": "<<count << "\n";

	}
	cout << "finish"<<endl;
	return 0;
}
