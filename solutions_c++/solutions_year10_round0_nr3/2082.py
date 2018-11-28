//============================================================================
// Name        : BitTest.cpp
// Author      : lala
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <math.h>

using namespace std;

int main() {
	long long problems;
	long long runs;
	long long capacity;
	long long numberOfGroups;
	cin >> problems;
	for(long long i = 0; i < problems; i++){
		cin >> runs;
		cin >> capacity;
		cin >> numberOfGroups;
		long long groups[numberOfGroups];
		for(long long j = 0; j < numberOfGroups; j++)
			cin >> groups[j];

		long long queuePos = 0;
		long long euros = 0;
		for(long long j = 0; j < runs; j++){
			long long occupied = 0;
			long long groupsIn = 0;
			while(occupied < capacity){
				occupied += groups[queuePos];
				if(occupied > capacity){
					occupied -= groups[queuePos];
					break;
				}
				queuePos = (queuePos+1)%numberOfGroups;
				groupsIn++;
				if(groupsIn == numberOfGroups)
					break;
			}
			euros += occupied;
		}
		cout << "Case #" << i+1 <<": "<< euros << endl;
	}
	return 0;
}
