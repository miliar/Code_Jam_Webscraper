#include <iostream>
#include <string.h>
#include <map>
#include <algorithm>
#include <queue>
#include <cmath>
#include <stdlib.h>
#include <functional>
#include <iomanip>
#include <complex>
#include <stack>
#include <fstream>
#include <set>
#include <list>
#include <vector>
#include <climits>
#include <cfloat>
using namespace std;
typedef long long int ll;
#define EPS (1e-10) 
#define SZ(a) ((int)a.size())
#define SORT(v) sort((v).begin(), (v).end())
#define RSORT(v) sort((v).rbegin(),(v).rend())
#define MP make_pair

int main(){
	map<char,char> mp;
	mp['y']='a',mp['n']='b',mp['f']='c',mp['i']='d',mp['c']='e',mp['w']='f';
	mp['l']='g',mp['b']='h',mp['k']='i',mp['u']='j',mp['o']='k',mp['m']='l';
	mp['x']='m',mp['s']='n',mp['e']='o',mp['v']='p',mp['z']='q',mp['p']='r';
	mp['d']='s',mp['r']='t',mp['j']='u',mp['g']='v',mp['t']='w',mp['h']='x';
	mp['a']='y',mp['q']='z',mp[' ']=' ';
	int n;
	string s;
	std::ifstream cin( "/Users/admin/Downloads/A.in" );
	std::ofstream cout( "/Users/admin/Downloads/A.out" );
	cin>>n;
	cin.ignore();
	for(int ii=1;ii<=n;ii++){
		cout<<"Case #"<<ii<<": ";
		getline(cin,s);
		for(int i=0;i<SZ(s);i++){
			cout<<mp[s[i]];
		}
		cout<<endl;
	}

}