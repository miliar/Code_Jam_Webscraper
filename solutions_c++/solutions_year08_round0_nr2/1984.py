#include <vector>
#include <fstream>
#include <list>
#include <string>

using namespace std;

struct hours 
{
   double hrs;
   double mins;
   bool tag; // A true, B false
};

int ToInt(char fir, char sec){
	int first = fir - '0'; 
	int second = sec - '0';

	return first*10 + second;
}

bool CompareTo(hours & one, hours & two){
   return ( one.hrs < two.hrs ||
	       (one.hrs == two.hrs && one.mins < two.mins  ));

}

int Solve(vector<hours> & arr, vector<hours> & dep){
	int result = dep.size();
	int arrsize = arr.size();
	if (arr.size() == 0) return result;
	if (dep.size() == 0) return 0;
	
	bool arrtag = arr[0].tag;
	bool deptag = dep[0].tag;

	list<hours> ls;
	for (int i = 0; i < arrsize; i++){
		ls.push_back(arr[i]);
		//outfile << "arr" << arr[i].hrs << arr[i].mins << endl;

	}

	for (int i = 0; i < result; i++){
		ls.push_back(dep[i]);
		//outfile << "dep" << dep[i].hrs << dep[i].mins << endl;
	}

	

	ls.sort(CompareTo);

	list<hours>::iterator curr;
	int count = 0;
	//list<hours>::iterator next;
	for (curr = ls.begin(); curr != ls.end(); curr++){
		//outfile << "sorted" << (*curr).hrs << (*curr).mins << endl;
		if  (curr->tag == arrtag){
			count++;
		} else {
			if (count > 0) count--;
		}
	}
	
	result = dep.size() - (arr.size() - count);

	return result;
}

int main(){
	int n = 1;
	int m;
	ifstream file;
	ofstream outfile;
	file.open("../b-small.in");
	outfile.open("../b-small.out");

	file >> m;

	
	vector<hours> depA, depB, arrA, arrB;
	while (n <= m){
		int turnaround;
		file >> turnaround;

		int numA, numB;
		file >> numA;
		file >> numB;

		depA.clear(); depB.clear(); arrA.clear(); arrB.clear();

		

		for (int i = 0; i < numA; i++){
			string  temp;
			file >> temp; // departure
			hours temphr;
		    temphr.hrs = ToInt(temp[0], temp[1]);
			temphr.mins = ToInt(temp[3], temp[4]) + 0.5;
			temphr.tag = true;
		
			depA.push_back(temphr);

			file >> temp; // arrive
			hours temphr1;
			temphr1.hrs = ToInt(temp[0], temp[1]);
			temphr1.mins = ToInt(temp[3], temp[4]) + turnaround;
			temphr1.tag = true;
			
			arrA.push_back(temphr1);
		}

		for (int i = 0; i < numB; i++){
			string temp;
			file >> temp; // departure
			hours temphr;
		    temphr.hrs = ToInt(temp[0], temp[1]);
			temphr.mins = ToInt(temp[3], temp[4]) + 0.5;
			temphr.tag = false;
		
			depB.push_back(temphr);

			file >> temp; // arrive
			hours temphr1;
			temphr1.hrs = ToInt(temp[0], temp[1]);
			temphr1.mins = ToInt(temp[3], temp[4]) + turnaround;
			temphr1.tag = false;
		
			arrB.push_back(temphr1);
		}

		outfile << "Case #" << n << ": " 
			    << Solve(arrB, depA) << " " << Solve(arrA, depB) << endl;

		n++;
	}

	file.close();
	outfile.close();

	return 0;
}