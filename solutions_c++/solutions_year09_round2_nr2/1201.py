#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char* argv[]){
	ifstream input("input.txt", ifstream::in);
	ofstream output("output.txt", ofstream::out);
	int n;
	input >> n;
	string buf;
	getline(input, buf);
	cout << n;
	for(int i=0; i<n; i++){
		output << "Case #" << i+1 << ": ";
		getline(input, buf);
		vector<int> digits;
		for(int j=0; j<buf.length(); j++){
			digits.push_back(buf[j] - '0');
			cout << digits[j];
		}
		cout << endl;
		int closest = digits.size()-1;
		int val = 10;
		bool sat = false;
		for(int j=digits.size()-1; j>=0; j--){
			for(int k=digits.size()-1; k>j; k--){
				if(digits[k]>digits[j]){
					if(digits[k]<=val){
						closest = k;
						val = digits[k];
						sat = true;
					}
				}
			}
			if(sat){
				int tmp = digits[j];
				digits[j] = digits[closest];
				digits[closest] = tmp;
				sort(digits.begin()+j+1, digits.end());
				for(int q=0; q<digits.size(); q++){
					output << digits[q];
					cout << digits[q];
				}
				cout << endl;
				break;
			}
			if(j==0){
				digits.push_back(0);
				sort(digits.begin(), digits.end());
				for(int p=0; p<digits.size(); p++){
					if(digits[p] != 0){
						digits[0] = digits[p];
						digits[p] = 0;
						break;
					}
				}
				for(int q=0; q<digits.size(); q++){
					cout << digits[q];
					output << digits[q];
				}
				cout << endl;
				break;
			}
		}
		output << endl;
	}
	cout << "Hello world";
	return 0;
}
