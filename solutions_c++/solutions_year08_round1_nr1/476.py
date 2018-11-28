#include <iostream>
#include <fstream>
#include <string>
#include <utility>
#include <vector>
using namespace std;

void getData(ifstream & infile,int & n,vector<int> & v1,vector<int> & v2){
	int temp;
	infile>>n;
	for (int i=1;i<=n;i++){
		infile>>temp;
		v1.push_back(temp);
	}
	for (int i=1;i<=n;i++){
		infile>>temp;
		v2.push_back(temp);
	}
}

int calc(int n,vector<int> v1,vector<int> v2){
	int temp;
	int sum=0;
	for (int i=0;i<n;i++){
		for (int j=i+1;j<n;j++){
			if (v1.at(i)>v1.at(j)){
				temp=v1.at(i);
				v1.at(i)=v1.at(j);
				v1.at(j)=temp;
			}
		}
	}
	for (int i=0;i<n;i++){
		for (int j=i+1;j<n;j++){
			if (v2.at(i)<v2.at(j)){
				temp=v2.at(i);
				v2.at(i)=v2.at(j);
				v2.at(j)=temp;
			}
		}
	}
	for (int i=0;i<n;i++){
		sum+=v1.at(i)*v2.at(i);
	}
	return sum;
}

int main(){
	int T;
	int n;
	vector<int> v1;
	vector<int> v2;
	ifstream infile("a.in");
	ofstream outfile("a.out");

	infile>>T;
	for (int i=1;i<=T;i++){
		v1.clear();
		v2.clear();
		getData(infile,n,v1,v2);
		outfile<<"Case #"<<i<<": "<<calc(n,v1,v2)<<endl;
	}
	return 0;
}