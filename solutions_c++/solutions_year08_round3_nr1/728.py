#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int amount;

class Case{

public:

	int P,K,L;

	int *letter;
	int *sorted;

	Case(fstream &f){

		f>>P>>K>>L;
		letter = new int[L];
		sorted = new int[L];

		for(int i=0;i<L;i++)
			f>>letter[i];
	}

	void solve(fstream& f,int order){

		for(int i=0;i<L;i++){

			int max=0;
			int or=0;
			for(int j=i;j<L;j++){

				if(letter[j]>max){

					max=letter[j];
					or=j;
				}
			}
			int temp = max;
			int tmporder = or;
			letter[or]=letter[i];
			letter[i]=max;
		}

		int result=0;

		int factor=1;
		for(int i=0;i<L;i+=K,factor++){

			for(int j=0;j<K;j++){

				if(i+j<L)
					result +=factor *letter[i+j];
			}
		}
			
		f<<"Case #"<<order<<": "<<result<<endl;
	}

	~Case(){

	}
};

int main(){

	fstream f;
	fstream f2;
	f.open("input.txt",ios::in);
	f2.open("output.txt",ios::out);

	f>>amount;

	for(int i=1;i<=amount;i++){

		Case C(f);
		C.solve(f2,i);
	}
	return 1;
}