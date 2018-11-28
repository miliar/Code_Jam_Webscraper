// Google Code Jam -- Online Round 3
// 12th June 2010
//
// Problem D

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

#define MOD 1000000007

using namespace std;


// A few utility I/O functions
vector <string> split(const string &s,const char &separator=' '){vector <string> ret;int p1=0,p2;for (p2 = 0;p2 < s.size();p2++)if (s[p2]==separator){if (p2-p1>0) ret.push_back(s.substr(p1,p2-p1));p1=p2+1;}if (p2-p1 > 0) ret.push_back(s.substr(p1,p2-p1));return ret;}
template <class T> T get(istream &fin){string s;getline(fin,s);stringstream ss(s);T ret;ss >> ret;return ret;}
template <class T> vector <T> getv(istream &fin,const char &separator = ' '){string s;getline(fin,s);vector <string> convert = split(s,separator);vector <T> ret(convert.size());for (int i=0;i<convert.size();i++){stringstream ss(convert[i]);ss>>ret[i];}return ret;}
template <> vector <string> getv <string> (istream &fin,const char &separator){string s;getline(fin,s);return split(s,separator);}


int mem1[72][72][72][72];
int count(int num,int carry,int last,int sum,int base){
	if (carry < 0 || carry >= (base+1) / 2 || num < 0) return 0;
	if (mem1[num][carry][last][sum] != -1)
		return mem1[num][carry][last][sum];
	if (num == 0) return sum == 0 && carry == 0 ? 1 : 0;
	long long ret = 0;
	for (int i=last+1;i<base;i++)
		ret += count(num-1,carry-(i > sum),i,(base + sum - i) % base,base);
	return mem1[num][carry][last][sum] = (ret % MOD);
}
long long withzero(int rows,int sum,int carry,int base){
	return count(rows-1,carry,0,sum,base);
}
long long withoutzero(int rows,int sum,int carry,int base){
	return count(rows,carry,0,sum,base);
}

long long factorial[72];
long long nck[72][72];
int mem2[72][72][72];
int count2(int i,int rows,int carry,int &base,vector <int> &dig){
	if (i == -1) return carry == 0 ? 1 : 0;
	if (mem2[i][rows][carry] != -1) return mem2[i][rows][carry];
	long long ret = 0;
	for (int j = rows;j<=base;j++){
		for (int c1 = 0;c1 < (base+1)/2;c1++){
			int tot = carry * base + dig[i] - c1;
			if (tot < 0) continue;
			long long ans = withoutzero(j,tot%base,tot/base,base) * count2(i-1,j,c1,base,dig);
			ans %= MOD;
			ans *= nck[j][rows];ans %= MOD;
			ans *= factorial[rows];ans %= MOD;
			ret = (ret + ans) % MOD;
			if (rows > 0){
				ans = withzero(j,tot%base,tot/base,base) * count2(i-1,j,c1,base,dig);
				ans %= MOD;
				ans *= nck[j-1][rows-1];ans %= MOD;
				ans *= factorial[rows];ans %= MOD;
				ret = (ret + ans) % MOD;
			}
		}
	}
	return mem2[i][rows][carry] = ret;
}

int main(int argc,const char * argv[]){

	// File stuff
	istream *in__ = NULL;ostream *out__ = NULL;
	if (argc > 1) in__ = new ifstream(argv[1]);else in__ = &cin;
	if (argc > 2) out__ = new ofstream(argv[2]);else out__ = &cout;
	istream & in = *in__;ostream & out = *out__;

	out.setf(ios::fixed,ios::floatfield);cout.setf(ios::fixed,ios::floatfield);
	out.precision(7);cout.precision(7);

	memset(nck,0,sizeof(nck));
	nck[0][0] = 1;
	for (int i=1;i<71;i++)
		for (int j=0;j<i;j++){
			nck[i][j]=(nck[i][j]+nck[i-1][j]) % MOD;
			nck[i][j+1]=(nck[i][j+1]+nck[i-1][j]) % MOD;
		}
	memset(factorial,0,sizeof(factorial));
	factorial[0] = 1;
	for (int i=1;i<71;i++)
		factorial[i] = (factorial[i-1]*i) % MOD;


	// Main stuff starts here
	for (int TC = get <int>(in),cas = 1;cas <= TC;cas++){
		int res = 0;

		memset(mem1,-1,sizeof(mem1));
		memset(mem2,-1,sizeof(mem2));

		vector <long long> x = getv <long long> (in);

		vector <int> dig;
		long long N = x[0];
		int B = x[1];
		while (N){
			dig.push_back(N % B);
			N/=B;
		}
		res = count2(dig.size()-1,0,0,B,dig);


		out << "Case #" << cas << ": " << res << endl;
		if (argc == 4) cout  << "Case #" << cas << ": " << res << endl;
	}

	if (in__ != &cin) delete in__;
	if (out__ != &cout) delete out__;
	return 0;
}