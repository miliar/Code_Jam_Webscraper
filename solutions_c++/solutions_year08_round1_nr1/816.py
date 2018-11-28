#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <list>

using namespace std;



/*bool GreaterThan(int aa, int bb){
  return  (aa > bb);
}

bool LowerThan(int aa, int bb){
	return (aa < bb);
}*/


int main(){
	int n = 1;
	int m;
	ifstream infile("a-small.in");
	ofstream outfile("a-small.out");

	infile >> m;

	if (n == 0) return 0;

	while (n <= m){
		int num;
		infile >> num;

		list<int> listA(num);
		list<int> listB(num);
		listA.clear(); listB.clear();
		//outfile << "yoyo" << endl;
		int temp;
		for (int i = 0; i < num; i++){
			infile >> temp;
			listA.push_back(temp);
			
		}

		for (int i = 0; i < num; i++){
			infile >> temp;
			listB.push_back(temp);
			
		}

		listA.sort();
		listB.sort();
		listB.reverse();

		int result = 0;
		list<int>::iterator itA = listA.begin();
		list<int>::iterator itB = listB.begin();
		for (int i = 0; i < num; i++){
			//outfile << (*itA) << " " << (*itB) << "ye";
			result += (*itA) * (*itB);
			itA++; itB++;
		}

		outfile << "Case #" << n << ": " << result << endl;

		n++;
	}

	infile.close();
	outfile.close();

	return 0;
}