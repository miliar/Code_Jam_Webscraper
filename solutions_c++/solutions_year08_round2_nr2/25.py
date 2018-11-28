// Google Code Jam -- Online Round 1
// 26th July 2008
//
// Problem B - 

#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <fstream>
#include <cmath>
#include <queue>
#include <set>
#include <algorithm>
#include <list>
#include <cstdio>

using namespace std;


// A few utility I/O functions
vector <string> split(const string &s,const char &separator=' '){vector <string> ret;int p1=0,p2;for (p2 = 0;p2 < s.size();p2++)if (s[p2]==separator){if (p2-p1>0) ret.push_back(s.substr(p1,p2-p1));p1=p2+1;}if (p2-p1 > 0) ret.push_back(s.substr(p1,p2-p1));return ret;}
template <class T> T get(istream &fin){string s;getline(fin,s);stringstream ss(s);T ret;ss >> ret;return ret;}
template <class T> vector <T> getv(istream &fin,const char &separator = ' '){string s;getline(fin,s);vector <string> convert = split(s,separator);vector <T> ret(convert.size());for (int i=0;i<convert.size();i++){stringstream ss(convert[i]);ss>>ret[i];}return ret;}
template <> vector <string> getv <string> (istream &fin,const char &separator){string s;getline(fin,s);return split(s,separator);}

int parent[1000010];
int par(int i){
	if (parent[i] == i) return i;
	return (parent[i] = par(parent[i]));
}

int main(int argc,const char * argv[]){

	// File stuff
	ifstream fin(argv[1]);
	ofstream fout(argv[2]);
	fout.setf(ios::fixed,ios::floatfield);
	fout.precision(7);

	vector <long long> primes;
	bool isPrime[1000010];
	memset(isPrime,1,sizeof(isPrime));
	for (int i=2;i<1000010;i++)
		if (isPrime[i]){
			primes.push_back(i);
			for (int j=2*i;j<1000010;j+=i)
				isPrime[j] = false;
		}

	//cout << primes.size() << endl;

	// Main stuff starts here
	for (int TC = get <int>(fin),cas = 1;cas <= TC;cas++){
		long long res = 0;

		for (int i=0;i<1000010;i++)
			parent[i] = i;
		vector <long long> v = getv <long long> (fin);
		
		long long A,B,P;A = v[0], B=v[1], P=v[2];
		long long range = B - A;

		for (int i=0;i<primes.size() && primes[i] <= range;i++)
			if (primes[i] >= P){
				long long base = (primes[i] - (A % primes[i])) % primes[i];

				for (long long x = base +primes[i];x <= range;x += primes[i]){
					parent[par(x)] = par(base);}
			}
		set <int> ans;
		for (int i=0;i<=range;i++){
			ans.insert(par(i));
		}

		fout << "Case #" << cas << ": " << ans.size() << endl;
		if (argc == 4) cout  << "Case #" << cas << ": " << ans.size() << endl;		
	}
	return 0;
}