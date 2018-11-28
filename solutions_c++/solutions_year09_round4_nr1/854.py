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
#include <cstring>
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

bool isUpperCase(char c){return c>='A' && c<='Z';}//NOTES:isUpperCase(
bool isLowerCase(char c){return c>='a' && c<='z';}//NOTES:isLowerCase(
bool isLetter(char c){return c>='A' && c<='Z' || c>='a' && c<='z';}//NOTES:isLetter(
bool isDigit(char c){return c>='0' && c<='9';}//NOTES:isDigit(
char toLowerCase(char c){return (isUpperCase(c))?(c+32):c;}//NOTES:toLowerCase(
char toUpperCase(char c){return (isLowerCase(c))?(c-32):c;}//NOTES:toUpperCase(

template<class T> inline bool isPrimeNumber(T n)//NOTES:isPrimeNumber(
  {if(n<=1)return false;for (T i=2;i*i<=n;i++) if (n%i==0) return false;return true;}
template<class T> inline vector<pair<T,int> > factorize(T n)//NOTES:factorize(
  {vector<pair<T,int> > R;for (T i=2;n>1;){if (n%i==0){int C=0;for (;n%i==0;C++,n/=i);R.push_back(make_pair(i,C));}
   i++;if (i>n/i) i=n;}if (n>1) R.push_back(make_pair(n,1));return R;}

int toInt(string s) { istringstream sin(s); int t; sin>>t; return t;}
int64 toInt64(string s) { istringstream sin(s); int64 t; sin>>t; return t;}
string toString(int v ){ ostringstream sout; sout<<v; return sout.str();}
string toString(int64 v){ ostringstream sout; sout<<v; return sout.str();}

string mat[42];
int n;

bool pd(int p)
{
	for(int i = p; i < n; i++)
	{
		if(mat[p][i] == '1')
			return true;
	}
	return false;
}

bool pd2(int p, int q)
{
	for(int i = p; i < n; i++)
	{
		if(mat[q][i] == '1')
			return false;
	}
	return true;
}

void mswap(int a, int b)
{
	string t;
	t = mat[a];
	for(int i = a; i > b; i--)
	{
		mat[i] = mat[i-1];
	}
	mat[b] = t;
}

int main()
{
	int cas;
	cin>>cas;
	for(int icas = 1; icas <= cas; icas++)
	{
		int sum;
		sum = 0;
		cin>>n;
		set0(mat);
		for(int i = 1; i <= n; i++)
			cin>>mat[i];
		for(int i = 1; i <= n; i++)
		{
			if(pd(i))
			{
				for(int j = i; j <= n; j++)
				{
					if(pd2(i,j))
					{
						sum += (j-i);
						mswap(j,i);
						break;
					}
				}
			}
		}
		cout<<"Case #"<<icas<<": "<<sum<<endl;
	}
	return 0;
}