#include <cmath>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <set>

using namespace std;

set<string> setall;

int check_digit(int x)
{
	int dit = 0;
	do{
		x /= 10;
		++dit;
	} while(x!=0);
	return dit;
}

int pow10(int m)
{
	int n = 1;
	for(int i=0;i<m;++i) { n *= 10; }
	return n;
}

int reverse(string x, int dig)
{
	int dig_tot = check_digit(atoi(x.c_str()));
	string w = x.substr(0, dig_tot-dig);
	string z = x.substr(dig_tot-dig);
	
	return atoi((z+w).c_str());
}

void make_str(int x, string& s)
{
	stringstream ss;
	ss << x;
	ss >> s;
}

int check_possible(int x, int y, int dig)
{
	int sum = 0;
	for(int i=1;i < dig;++i) {
		string now;

		make_str(x, now);

		if (now[dig-i] != '0') {
			int r = reverse(now,i);
			if (x < r && r <= y) {
				stringstream ss;
				ss << x;
				ss << r;
				ss << y;
				if (setall.find(ss.str()) == setall.end()) {
					//cout << "x "<<x << " " << r << " " << y << endl;
					++sum;
					setall.insert(ss.str());
				} else {
					//cout << "Exist!!" << ss.str() << endl;
				}
			}
		}
	}
	return sum;
}

int check_case(int A, int B)
{
	int count = 0;
	int dig = check_digit(A);

	if (dig < 2) return 0;

	for(int i=A;i < B; ++i) {
		//if (i%10 == 0) continue;
		count += check_possible(i, B, dig); 
	}
	return count;
}

int main()
{
	int cases;
	cin >> cases;
	for(int i=1;i<=cases;++i) {
		int A, B;
		cin >> A >> B;
		setall.clear();
		cout <<"Case #"<<i<<": "<< check_case(A,B) << endl;
	}
}
