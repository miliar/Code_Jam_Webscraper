#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define For(i,b) for(int i = 0; i < (int)b; ++i)
#define Fori(i,a,b) for(int i = a; i < (int)b; ++i)
#define Ford(i,a,b) for(int i = a; i >=b; --i)
#define All(t) t.begin(),t.end()
#define Sort(a) sort(All(a))
#define Fill(a,b) memset(a,b,sizeof(a))
#define Forstl(it,x) for(typeof(x.begin()) it=x.begin(); it!=x.end(); ++it)
#define db(x) cout << #x << " = " << x << endl
#define mod(A, B) ((((A) % (B)) + (B)) % (B))
#define Exist(container, element) (container.find(element) != container.end())
#define sz(a) int((a).size()) 
typedef long long ll;

template <class T>
void out(vector<T> v)
{
  cout << "{";
  For(_i,v.size()) {if(_i) cout<<","; cout<<v[_i];}
  cout<<"}"<<endl;
}


// the number of palindromic number betwwen lower and upper
string itos (ll i) {stringstream s; s << i; return s.str();}
ll stoi (string s) {istringstream in(s); ll ret; in >> ret; return ret;}


int main ()
{
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	int T;
	string n;
	fin >> T;
	For(z,T)
	{
		fin >> n;
		string s = n;
		string t = s;
		string res;
		string k = s;
		sort(k.rbegin(), k.rend());
		if(k == s)
		{
            string orig = s;
            sort(All(orig));
            if(orig[0] != '0')
            {
				res = orig.substr(0,1) + "0" + orig.substr(1);
			}
			else
			{
				string zeros = "0";
				string rem;
				For(i,sz(orig))
				{
					if(orig[i] == '0')
						zeros += "0";
					else
					    rem += orig[i];
				}
				res = rem.substr(0,1) + zeros + rem.substr(1);
			}
		}
		else
		{
			next_permutation(All(t));
			res = t;
		}
		fout << "Case #" << z + 1 << ": " << res << endl;
	}
	getchar();
	return 0;
}
