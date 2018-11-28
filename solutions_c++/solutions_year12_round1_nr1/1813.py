#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include<fstream>

using namespace std;

double stroke_exp(int a, int b, vector<double> &v){
	double tmp_p;
	vector<double> result;
	long count=0;

	/* completely input */
	tmp_p=1.0;
	for(int i=0; i<a; i++){
		tmp_p=tmp_p*v[i];
	}
	//cout << tmp_p<< endl;
	//cout << (tmp_p*(b-a+1)+(1-tmp_p)*(b-a+1+b+1)) << endl;
	result.push_back((tmp_p*(b-a+1)+(1-tmp_p)*(b-a+1+b+1)));

	/* giveup by enter */
	result.push_back(b+2);
	//cout << b+2 << endl;

	/*push_backspace*/
	for(int i=1;i<=a;i++){
		tmp_p=1.0;
		for(int j=0;j<a-i;j++){
			tmp_p=tmp_p*v[j];
		}
		//cout << tmp_p*(i+i+b-a+1)+(1-tmp_p)*(i+i+b-a+1+b+1) <<endl;
		result.push_back(tmp_p*(i+i+b-a+1)+(1-tmp_p)*(i+i+b-a+1+b+1));
	}
	
	sort(result.begin(), result.end());
	return result[0];
}

int main(int argc, char **argv){
	string buf;
	int in_num;
	int a;
	int b;
	vector<double> p;
	vector<double> result;
	stringstream buf2;
	double tmp;
	int c=1;
	
	if(argc==1){
		cout << "Please input file name!!" << endl;
		return -1;
	}

	ifstream ifs(argv[argc-1]);
	//cout << "File open succeeded!" << endl;
	ifs >> buf;
	in_num=atoi(buf.c_str());
	for(int j=0;j<in_num; j++){
		ifs >> buf;
		a=atoi(buf.c_str());
		ifs >> buf;
		b=atoi(buf.c_str());
		// cout << a << ", " << b << ": File input is completed!" << endl;
		for(int i=0;i<a;i++){
			ifs>>buf;
			//cout <<"before: " << buf << endl;
			p.push_back(atof(buf.c_str()));
			//cout << "after: " <<p[i] << endl;
		}
		tmp=stroke_exp(a, b, p);
		result.push_back(tmp);
		p.clear();
	}
	
	for (int i=0; i<in_num;i++){
		cout << "Case #" << i+1 << ": " << result[i] << endl;
	}

	return 0;
}
