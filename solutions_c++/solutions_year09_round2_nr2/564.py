#include <fstream>
#include <algorithm>
#include <string>
using namespace std;

int main() {
	int n;
	ifstream fi("b.in");
	ofstream fo("b.out");
	fi >> n;
	string num;
	getline(fi, num);
	for (int i=0; i<n; i++) {
		getline(fi, num);
		fo << "Case #" << (i+1) << ": ";
		if (next_permutation(num.begin(), num.end()))
			fo << num;
		else {
			sort(num.begin(), num.end());
			if (num[0]=='0')
				for (int i=0; ; i++)
					if (num[i]!='0') {
						swap(num[0], num[i]);
						break;
					}
			fo << num[0] << '0' << num.c_str()+1;
		}
		fo << endl;
	}
}
