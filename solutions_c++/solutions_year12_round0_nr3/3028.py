#include<iostream>
#include<queue>
#include<sstream>
#include<string>
#include<fstream>
using namespace std;


string numI;
string numB;

void stringToQueue(const string &str, queue<char> &q){
	for(int i=0; i<str.size(); i++)
		q.push(str[i]);
}

void swap(int &A, int &B) {
	int temp;
	temp = A;
	A = B;
	B = temp;
}

void printQ(queue<char> &q) {
	for(int i=0; i<q.size(); i++) {
		cout << q.front();
		q.push(q.front());
		q.pop();
	}
}

bool compareI(const queue<char> &num) {
	queue<char> numQ = num;
	for(int i=0; i<numQ.size(); i++) {
			if(numQ.front() > numI[i])
				return 1;
			else if(numQ.front() < numI[i])
				return 0;
		
		numQ.push(numQ.front());
		numQ.pop();
	}
	return 0;
}

bool compareB(const queue<char> &num) {
	queue<char> numQ = num;
	for(int i=0; i<numQ.size(); i++) {
		if(numQ.front() < numB[i])
			return 1;
		else if(numQ.front() > numB[i])
			return 0;
		numQ.push(numQ.front());
		numQ.pop();
	}
	return 1;
}

int range(int A, int B) {
	int _c=0;

	ostringstream osB;
	osB<<B;
	numB = osB.str();

	for(int i=A; i<=B; i++)
	{
		queue<char> temp;
		ostringstream osI;
		osI << i;
		numI = osI.str();
		stringToQueue(numI, temp);
		for(int j=1; j<numI.size(); j++) {
			temp.push(temp.front());
			temp.pop();
			if(compareI(temp) && compareB(temp)) {
				//cout << i << ' ';
				//printQ(temp);
				//cout << endl;
				_c++;
			}
		}
	}
	return _c;
}

int main() {/*
	int a, b;
	cin >> a >> b;
	cout << range(a,b);
	return 0;
*/
	ifstream inFile("C-small-attempt0.in");
	ofstream outFile("C-small-out.out");
	int T;
	inFile >> T;
	//cin.ignore();
	int a, b;
	for(int i=1; i<=T; i++) {
		inFile >> a >> b;		
		outFile << "Case #" << i << ": "<< range(a,b) << endl;
	}

	inFile.close();
	outFile.close();
}
