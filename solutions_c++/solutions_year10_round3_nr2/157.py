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
	int lo,hi,c;
	filestr.open("/Users/HOOI/Downloads/B-large.in");
	outstr.open("/Users/HOOI/Documents/XCode/CodeJam/OUTPUT.txt");
	filestr >> cases;
	for (int cs=0;cs<cases;cs++){
		int res=0;
		filestr >> lo >> hi >> c;
		cout << "lo="<<lo<<" hi ="<<hi<<" c="<<c<<endl;
		while ( (long long)lo*c < hi){
			int x = (int) (sqrt(1.0*hi)*sqrt(1.0*lo));
			if ( 1.0*hi/x > 1.0*(x+1)/lo){
				hi=x+1;
				cout << "hi is "<<hi<<endl;
				res++;
			}
			else {
				lo=x;
				cout << "lo is "<<lo<<endl;
				res++;
			}
		}
		outstr << "Case #"<<cs+1<<": "<< res <<endl;
		cout << "Case #"<<cs+1<<": "<< res <<endl;
	}
	filestr.close();
	outstr.close();
	return 0;
}