#include <iostream>
#include <string>
#include <sstream>

#include <list>

#include <math.h>



using namespace std;

int main(int argc, char *argv[]){
	string line1;
	getline(cin, line1);
	stringstream ss1(line1);
	int num_cases;
	ss1>>num_cases;
#ifdef TRACE
	cout<<"Cases = "<<num_cases<<endl;
#endif
	
	for(int i=0;i<num_cases;i++){
		string line2;
		getline(cin, line2);
		stringstream ss2(line2);
		int num_coords;
		ss2>>num_coords;
		
		string linev1;
		getline(cin, linev1);
		stringstream ssv1(linev1);
		
		string linev2;
		getline(cin, linev2);
		stringstream ssv2(linev2);

		list<int> v1;
		list<int> v2;
		for(int j=0;j<num_coords;j++){
			int coord1, coord2;
			ssv1 >> coord1;
			ssv2 >> coord2;
			v1.push_back(coord1);
			v2.push_back(coord2);
		}


		v1.sort();
		v2.sort();
		v2.reverse();

		list<int>::iterator iter1=v1.begin();
		list<int>::iterator iter2=v2.begin();
		int sum =0;
		for(;iter1!=v1.end();iter1++,iter2++){
#ifdef TRACE
			cout<<*iter1<<" and "<<*iter2<<endl;
#endif
			sum+=(*iter1)*(*iter2);
		}
			

		cout<<"Case #"<<i+1<<": "<<sum<<endl;



	}


	return 0;
}

