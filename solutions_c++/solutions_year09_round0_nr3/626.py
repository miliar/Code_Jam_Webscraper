#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

struct testcase{
	int prob[19];
	string str;

	testcase(char *str) : str(str){
		for(int i=0; i<19;++i){
			prob[i]=0;
		}
	}

	void update(int idx){
		prob[idx]+=prob[idx-1];
		prob[idx]%=10000;
	}

	int search(){
		for(const char *p=str.c_str(); *p != '\0'; ++p){
			switch(*p){
				case 'w':
					prob[0]++;break;
				case 'e':
					update(1);
					update(6);
					update(14);break;
				case 'l':
					update(2);break;
				case 'c':
					update(3);
					update(11);break;
				case 'o':
					update(4);
					update(9);
					update(12);break;
				case 'm':
					update(5);
					update(18);break;
			//	case 'e':6
				case ' ':
					update(7);
					update(10);
					update(15);break;
				case 't':
					update(8);break;
			//	case 'o':9
			//	case ' ':10
			//	case 'c':11
			//	case 'o':12
				case 'd':
					update(13);break;
			//	case 'e':14
			//	case ' ':15
				case 'j':
					update(16);break;
				case 'a':
					update(17);break;
			//	case 'm':18
				default:break;
			}
		}
		return prob[18];
	}
};

int N;
vector<testcase> tests;

int input_read(char * filename)
{
	ifstream ifs;
	ifs.open(filename, ios::in); 
    

    ifs >> N;
	vector<char> buf(1000);
	ifs.getline(&buf[0],1000); //empty line read
	for(int i = 0; i < N; ++i){
		ifs.getline(&buf[0],1000);
		tests.push_back(testcase(&buf[0]));
	}

	return 0;
}

int main(){
	input_read("J:\\g\\C-large.in");
	
	ofstream o("J:\\g\\C-large.out");

	int n = 0;
	for(vector<testcase>::iterator i = tests.begin(), e = tests.end(); i != e; ++i){
		o << "Case #" << ++n << ": " 
			<< setw(4) << setfill('0') << (*i).search()
			<< endl;
	}
}

