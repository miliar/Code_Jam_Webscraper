#include<cstdio>
#include <cctype>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
#include <deque>
#include <math.h>
#include<stdio.h>
#include<memory.h>
using namespace std;


typedef stringstream ss;
typedef vector<string> vs;
typedef vector<int> vi;
typedef long long int64;

#define PI 3.14159265
#define pb push_back
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define fornm(i,n,m) for (int i=n; i<=(int)(m); i++)
#define forn(i,n) for (int i=0; i<(int)(n); i++)
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)

int dx[]={1,1,0,-1},dy[]={0,1,1,1};
#define MAXIMO 10000

int main()
{
	freopen("A-small-attempt0.in", "r", stdin); 	freopen("respuestaS.out", "w+", stdout);

	//freopen("A-large-practice.in", "r", stdin);  	freopen("respuestaLL.out", "w+", stdout);

    int T;
    
    cin>>T;
    map<char, char, less<char> > key;
    key['e']='o';
    key['j']='u';
    key['p']='r';
    key['m']='l';
    key['y']='a';
    key['s']='n';
    key['l']='g';
    key['c']='e';
    key['k']='i';
    key['d']='s';
    key['x']='m';
    key['v']='p';
    key['n']='b';
    key['r']='t';
    key['i']='d';
    key['b']='h';
    key['t']='w';
    key['a']='y';
    key['h']='x';
    key['w']='f';
    key['f']='c';
    key['o']='k';
    key['u']='j';
    key['g']='v';
    key['q']='z';
    key['z']='q';
    string A,B;
    vs vA,vB;
    set<char> va,vb;
    getline(cin,A);
    fornm(tc,1,T)
    {
	  getline(cin,A);
	  cout<<"Case #"<<tc<<": ";
	  forn(j,A.length())
         cout << key[A[j]];                     
      cout<<endl;
	  
	}
	
	return 0;
}
