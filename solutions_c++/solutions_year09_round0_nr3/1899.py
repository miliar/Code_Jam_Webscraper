
#include <cstring>
	using std::strcspn;
	using std::strchr;
#include <sstream>
#include <iostream>
#include <iomanip>
#include <string>
	using namespace std;


long count (const char* s, const char* w) {
	long n=0;
	if (!w[0])  return 1;

	while (s = strchr(s,w[0]),  s)  {				//cerr << n << "\t" << char(w[0]) << "\t" << s << endl;
		s++;
		n += count(s,w+1);
	};
	return n; 
}


int main() {
		const int max_s = 500;	// 
		int	N;
		char	s[max_s];
		char	w[] = "welcome to code jam";

	cin  >> N; 	cin.getline(s,max_s);
	
	for ( int n=1;   n<=N && cin;   n++)  {
		cout << "Case #" << n << ": ";
		cin.getline(s, max_s);					//cerr << "init: " <<  s << endl;
		long n = count((s), w);

		// result
		//cout << n << endl;
		stringstream ss;
		ss  << setw(4) << setfill('0') << n;
		string str = ss.str();
		cout  << str.substr(str.size()-4) << endl;
	}
}
