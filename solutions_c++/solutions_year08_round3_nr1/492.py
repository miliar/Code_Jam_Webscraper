#include<iostream>
#include<iomanip>
#include<fstream>
#include<string>
#include <vector>
#include <list>

using namespace std;
ofstream outfile("outp.out");//output file
ifstream infile("test.in");//input file 
bool cless(long long a, long long b){
	if (a < b)
		return false;
	else return true;
}

int main()
{
	int num_cases;
	infile>>num_cases;
	int num;
	int P,K,L;
	for (int i = 1; i <= num_cases; i++){
		infile>>P>>K>>L;
		list<long long> num1;
		list<long long>::iterator in1;
		long long answer = 0;
		int mm = L;
		for (int j = 0; j < mm; j++){
			infile>>num;
			if ( num != 0)
				num1.push_back(num);
			else 
				mm --;
		}
		
		if ( mm > (P * K)){
			outfile<<"Case #"<<i<<": IMPOSSIBLE";
		}
		else{
			num1.sort(cless);
			in1 = num1.begin();
			for (int j = 0; j < L; j++){
				if (j < K){
					answer += (*in1);
				}
				else{
					long long multi = j / K + 1;
					answer += ((*in1) * multi);
				}
				in1++;
			}
			outfile<<"Case #"<<i<<": ";
			outfile<<answer<<endl;
		}
	}
}