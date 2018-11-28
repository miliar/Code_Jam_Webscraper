#include <iostream>
#include <fstream>
#include <string>
#include <list>
using namespace std;

int main(){
	string ifile;
	cout << "enter the filename: ";
	cin >> ifile;

	ifstream infile(ifile.c_str());
	ofstream outfile((ifile.substr(0,ifile.length()-2)+"out").c_str());
	// check that the open succeeded
	if (!infile) {
		cerr << "error: unable to open input file: "
			<< ifile << endl;
		return -1;
	}
	if (!outfile) {
		cerr << "error: unable to create output file: "
			<< ifile.substr(0,ifile.length()-2)+"out" << endl;
		return -1;
	}

	int count = 1;
	int cases;
	infile >> cases;

	while(cases--){
        long long result = 0;
        long R, k;
        int N;
        list<long> mylist;
		infile >> R >> k >> N;
        int N2 = N;
        
        while(N2--)
        {
            long tmp;
            infile >> tmp;
            mylist.push_back(tmp);
        }
        while(R--)
        {
            long tmp = 0;
            int count = 0;
            while(tmp <= k && count < N)
            {            
                long tmp1 = *(mylist.begin());
                if(tmp+tmp1 > k)
                    break;
                tmp += tmp1;
                count++;
                mylist.pop_front();
                mylist.push_back(tmp1);
            }
            result += tmp;
            count = 0;
        }
		outfile << "Case #" << count++ << ": " << result << endl;
	}
	infile.close();
	outfile.close();
	return 0;
}