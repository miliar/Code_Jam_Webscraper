#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <cmath>
#include <cstring>
#include <numeric>
#include <utility>
using namespace std;

int main () {
	fstream filestr;
	ofstream outstr;
	int cases;
	int tempa,tempb;
	int n;
	vector<int> a,b;
	filestr.open("/Users/HOOI/Downloads/A-large.in");
	outstr.open("/Users/HOOI/Documents/XCode/CodeJam/OUTPUT.txt");
	filestr >> cases;
	for (int cs=0;cs<cases;cs++){
		int res=0;
		a.clear();
		b.clear();
		filestr >> n;
		//Clear vars/vectors
		for (int i=0;i<n;i++){
			filestr >> tempa >> tempb;
			a.push_back(tempa); b.push_back(tempb);
			cout << a[i] << " b " << b[i] << endl;
		}
		for (int i=0;i<n;i++){
			for (int j=i+1;j<n;j++){
				if ( (a[i]<a[j] && b[i]>b[j]) || (a[i] > a[j] &&b[i]<b[j])) res++;
			}
		}
		outstr << "Case #"<<cs+1<<": "<< res <<endl;
		cout << "Case #"<<cs+1<<": "<< res <<endl;
	}
	filestr.close();
	outstr.close();
	return 0;
}