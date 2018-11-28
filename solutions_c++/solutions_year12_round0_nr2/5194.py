#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <iomanip>
using namespace std;
struct Data{
	int p;
	int ok;
	int susp;
	Data( const int & p, const int & ok, const int &susp):
		p(p), ok(ok), susp(susp){}
	Data(){}
};
Data V[11];
void loadTotals(){
	V[0]= Data(0,0,0);
	V[1]= Data(1,1,1);
	for ( int i = 2;  i <=10; i++){
		V[i]=Data(i, ((i*3)-2), ((i*3)-4));
		
	}
}
void process( const int & test, const int & S, const int & p, std::vector<int> & googlers){
	int ok=0, susp=0;
	for(  unsigned int  i=0 ; i < googlers.size(); i++){
		if(googlers[i] >= V[p].ok) 
			ok++;
		else if(googlers[i] >= V[p].susp) 
			susp++;
	}
	int total = ok + (susp < S? susp:S);
	cout<< "Case #"<< test << ": " << total  << endl;
}

int main( char * arg, int argc){
	loadTotals();
	int tests;
	cin >> tests;
	
	string line;
	getline(cin, line);
	std::vector<int> googlers;
	for( int i = 1 ; i <= tests ; i++ ){
		int N, S, p,n;
		
		cin >>N;
		cin >> S;
		cin >> p;
		googlers.clear();
		for( int j = 0 ; j < N; j++){
			cin >> n;
			googlers.push_back(n);
		}
		process(i, S, p, googlers);
	}
	return 0;
}