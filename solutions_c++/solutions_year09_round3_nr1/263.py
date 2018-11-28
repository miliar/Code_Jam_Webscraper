#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
using namespace std;

ifstream fin("infile.in");
ofstream fout("outfile.out");

int main()
{
	int T; fin>>T;
	for(int t=1; t<=T; t++) {
		string number;
		fin>>number;
		map<char,int> M;
		vector<int> num;
		int base=1;
		int digit=0;
		M[number[0]]=1;
		num.push_back(1);
		for(int i=1; i<number.size(); i++) {
			if(M.count(number[i])==0) {
				base++;
				M[number[i]]=digit;
				num.push_back(digit);
				if(digit==0) digit=2;
				else digit++;
			}
			else {
				num.push_back(M[number[i]]);
			}
		}
		if(base==1) base=2;

		long long n=0;
		for(int i=0; i<num.size(); i++) {
			n *= base;
			n += num[i];
		}

		fout<<"Case #"<<t<<": "<<n<<endl;
	}
	
	return 0;
}