#include <iostream>
#include <sstream>
#include <vector>
#include <string.h>
#include <fstream>
using namespace std;
//void Print(vector<int> );
void Compute(int &, vector<int> , int , int, int, int &);
int XOR(vector<int> &);
void PrintOut(vector<int> &);

int main(){
	ifstream cin;
	string str;
	cin.open ("C-large.in", ifstream::in);
	string line;
	int numTests;
	getline( cin, line );
	istringstream iss( line );
	iss >> numTests;
	for(int i=0;i<numTests;i++){
		vector<int> vec;
		getline( cin, line );
		int count;
		istringstream iss( line );
		iss>> count;
		getline( cin, line );
		istringstream issNumbers( line );
		int number;
		while( issNumbers >> number ){
			vec.push_back(number);
		}
		cout<<"Case #"<<(i+1)<<":"<<" ";
		PrintOut(vec);
		cout<<endl;
	}
}

void PrintOut(vector<int> &vec){
	if(XOR(vec)!=0) cout<<"NO";
	else{
		int min=INT_MAX;
		int sum=0;
		for(int i=0;i<vec.size();i++){
			sum+=vec[i];
			if(vec[i]<min)
				min=vec[i];
		}
	cout<<(sum-min);
	}
}

/*void Print(vector<int> v){
	for(int i=0;i<v.size();i++)
	cout<<v[i]<<",";
	cout<<endl;
}*/

int XOR(vector<int> &v){
	int result=0;
	for(int i=0;i<v.size();i++)
	result^=v[i];
	return result;
}
