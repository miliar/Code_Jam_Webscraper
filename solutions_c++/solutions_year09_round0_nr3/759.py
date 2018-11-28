#include <fstream>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <algorithm>
#include <functional>
#include <queue>
#include <stack>
#include <ctime>
#include <cmath>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <bitset>
#include <cassert>
#include <stack>
#include <limits>
using namespace std;


typedef long long int64;
typedef unsigned long long uint64;
#define pause system("pause");
#define set0(x) memset(x, 0, sizeof(x))

clock_t __time;
#define retime __time = clock();
#define outtime cout<<clock()-__time<<endl;
const double pi = acos(-1.0);
const double eps = 1e-11;

template<class T> T gcd(const T &a, const T &b) {return (b == 0) ? a : gcd ( b, a%b);}
template<class T> T lcm(const T &a, const T &b) {return a*(b/gcd(a,b));}

int toInt(string s) { istringstream sin(s); int t; sin>>t; return t;}
int64 toInt64(string s) { istringstream sin(s); int64 t; sin>>t; return t;}
string toString(int v ){ ostringstream sout; sout<<v; return sout.str();}
string toString(int64 v){ ostringstream sout; sout<<v; return sout.str();}

//   welcome to   c o d e   j a m
//   0123456789 101112131415161718
int wel[19];

int run(string s)
{
	set0(wel);
	for(int i = 0; i < s.size(); i++)
	{
		switch(s[i])
		{
		case 'm' :
			wel[5] += wel[4];
			if(wel[5] > 9999)
				wel[5] -= 10000;

			wel[18] += wel[17];
			if(wel[18] > 9999)
				wel[18] -= 10000;
			break;
		case 'a' :
			wel[17] += wel[16];
			if(wel[17] > 9999)
				wel[17] -= 10000;
			break;
		case 'j' :
			wel[16] += wel[15];
			if(wel[16] > 9999)
				wel[16] -= 10000;
			break;
		case ' ' :
			wel[7] += wel[6];
			if(wel[7] > 9999)
				wel[7] -= 10000;

			wel[10] += wel[9];
			if(wel[10] > 9999)
				wel[10] -= 10000;

			wel[15] += wel[14];
			if(wel[15] > 9999)
				wel[15] -= 10000;
			break;
		case 'e' :
			wel[1] += wel[0];
			if(wel[1] > 9999)
				wel[1] -= 10000;

			wel[6] += wel[5];
			if(wel[6] > 9999)
				wel[6] -= 10000;

			wel[14] += wel[13];
			if(wel[14] > 9999)
				wel[14] -= 10000;
			break;
		case 'd' :
			wel[13] += wel[12];
			if(wel[13] > 9999)
				wel[13] -= 10000;
			break;
		case 'o' :
			wel[4] += wel[3];
			if(wel[4] > 9999)
				wel[4] -= 10000;

			wel[9] += wel[8];
			if(wel[9] > 9999)
				wel[9] -= 10000;

			wel[12] += wel[11];
			if(wel[12] > 9999)
				wel[12] -= 10000;
			break;
		case 'c' :
			wel[3] += wel[2];
			if(wel[3] > 9999)
				wel[3] -= 10000;

			wel[11] += wel[10];
			if(wel[11] > 9999)
				wel[11] -= 10000;
			break;
		case 't' :
			wel[8] += wel[7];
			if(wel[8] > 9999)
				wel[8] -= 10000;
			break;
		case 'l' :
			wel[2] += wel[1];
			if(wel[2] > 9999)
				wel[2] -= 10000;
			break;
		case 'w' :
			wel[0]++;
			if(wel[0] > 9999)
				wel[0] -= 10000;
			break;
		}
	}
	return wel[18];
}


int main()
{
	int n;
	cin>>n;
	getchar();
	string s;
	for(int i = 0; i < n; i++)
	{
		getline(cin,s);
		int t;
		t = run(s);
		cout<<"Case #"<<i+1<<": "<<(t < 1000 ? "0":"")<<(t < 100 ? "0":"")<<(t < 10 ? "0":"")<<t<<endl;
	}
	return 0;
}