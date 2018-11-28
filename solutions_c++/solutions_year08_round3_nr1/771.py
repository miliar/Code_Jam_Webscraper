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
		string linef;
		getline(cin, linef);
		stringstream ss2(linef);

		int P,K,L;
		ss2>>P;
		ss2>>K;
		ss2>>L;

		int total=0;
		int flag=0;

	

		string lines;
		getline(cin, lines);
		stringstream ss3(lines);

		list<int> l1;
		for(int j=0;j<L;j++){
			int item;
			ss3>>item;
			l1.push_back(item);
		}


		l1.sort();
		l1.reverse();

		int bucket=0;

		for(list<int>::iterator iter=l1.begin();iter!=l1.end();iter++){
			int factor=bucket/K+1;
			//Put in the next avaialble key
			if(factor<=P){
				//cout<<*iter<<"x"<<factor<<endl;
				total += (*iter)*factor;
			}
			else{
				cout<<"Case #"<<i+1<<": Impossible"<<endl;
				flag=1;
				break;
			}
			bucket++;
		}
		if(!flag)
			cout<<"Case #"<<i+1<<": "<<total<<endl;

	}
	return 0;
}

