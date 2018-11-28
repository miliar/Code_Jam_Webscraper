#include<iostream>
#include<fstream>
using namespace std;
int main(){
	int t,n,s,p;
	ifstream input;
	ofstream output;
	input.open("B-large.in");
	output.open("B-large.out");
	input>>t;
	int j = 0;
	while (t--){
		input>>n>>s>>p;
		int count = 0,num;
		for (int m = 0;m<n;++m){
			input>>num;
			if (num - p <0) continue;
			int temp = num - p - p + 2;
			if (p - 2 < 0 || temp < 0){
				int max = p,a = 0;
				if (max < temp) max = temp;
				if (temp < 0) a+=temp;
				if (p - 2<0) a+= p-2;
				if (max-p >= a*-1) {
					++count;
					continue;
				}
			}
			if (temp < p-2) continue;
			else if ((temp == p-2 || temp == p-1) && s>0){
				--s;
				++count;
			}
			else if (temp > p-1) ++count;
		}
		output<<"Case #"<<++j<<": "<<count<<endl;	
	}
	input.close();
	output.close();
	return 0;
}
