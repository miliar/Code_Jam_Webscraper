#include <iostream>
#include <list>
#include <fstream>
#include <cmath>

using namespace std;

int main() {
	
	ifstream fin ("q1input.txt");
	ofstream fout ("q1output.txt");
	
	long long T, N, dest, temp, temptime, total = 0;
	char rob, rob1;
	list<char> robs;
	list<int> robA, robB;
	list<int> robA1, robB1;
	int posA = 1;
	int posB = 1;
	long long currtime = 0;
	
	fin >> T;
	
	for (int i=0; i<T; i++) {
		fin >> N;
		//loop to get sequence
		for (int j=0; j<N; j++) {
			fin >> rob >> dest;
			robs.push_back(rob);
			if (rob == 'B')
				robA.push_back(dest);
			else {
				robB.push_back(dest);
			}
		}
		
		//convert to presses
		while (!robA.empty()) {
			temp = abs(robA.front() - posA);
			robA1.push_back(temp);
			posA = robA.front();
			robA.pop_front();
		}
		
		while (!robB.empty()) {
			temp = abs(robB.front() - posB);
			robB1.push_back(temp);
			posB = robB.front();
			robB.pop_front();
		}
		
		rob1 = robs.front();
		//start here
		while (!robs.empty()) {
			if (rob1 == robs.front()){
				if (rob1 == 'B'){
					currtime += robA1.front() + 1;
					robA1.pop_front();
				}
				else {
					currtime += robB1.front() + 1;
					robB1.pop_front();
				}
			}
			else {
				rob1 = robs.front();
				if (robs.front() == 'B'){
					temptime = robA1.front();
					robA1.pop_front();
					if (currtime > temptime){
						total += currtime;
						currtime = 1;
					}
					else {
						total += currtime;
						currtime = temptime + 1 - currtime;
					}
					
				}
				else {
					temptime = robB1.front();
					robB1.pop_front();
					if (currtime > temptime){
						total+= currtime;
						currtime = 1;
					}
					else {
						total += currtime;
						currtime = temptime + 1 - currtime;
					}
				}
				
			}
			
			robs.pop_front();
		}
		total += currtime;
		fout << "Case #" << i+1 << ": " << total << endl;
		total = 0;
		posA = 1;
		posB = 1;
		currtime = 0;
		robA1.clear();
		robB1.clear();
		
		
	}
	
	return 0;
}