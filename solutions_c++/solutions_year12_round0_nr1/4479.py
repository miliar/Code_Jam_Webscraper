/*
 Author: Mohamed Naguib
 Language: C++
*/
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>

using namespace std;

#define pb push_back
#define all(v) 				v.begin(),v.end()
#define sz 				size()
#define rep(i,m) 		for(int i=0;i<m;i++)
#define REP(i,k,m) 		for(int i=k;i<m;i++)
#define mem(a,b) 		memset(a,b,sizeof(a))
#define mp 				make_pair

typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;

#define OO ((int)1e9)
#define MAX 100000

string change(string in){
	string ret="";
	rep(i,in.sz){
		if(in[i]=='y')
			ret += "a" ;
		if(in[i]=='n')
			ret += "b" ;
		if(in[i]=='f')
			ret += "c" ;
		if(in[i]=='i')
			ret += "d" ;
		if(in[i]=='c')
			ret += "e" ;
		if(in[i]=='w')
			ret += "f" ;
		if(in[i]=='l')
			ret += "g" ;
		if(in[i]=='b')
			ret += "h" ;
		if(in[i]=='k')
			ret += "i" ;
		if(in[i]=='u')
			ret += "j" ;
		if(in[i]=='o')
			ret += "k" ;
		if(in[i]=='m')
			ret += "l" ;
		if(in[i]=='x')
			ret += "m" ;
		if(in[i]=='s')
			ret += "n" ;
		if(in[i]=='e')
			ret += "o" ;
		if(in[i]=='v')
			ret += "p" ;
		if(in[i]=='z')
			ret += "q" ;
		if(in[i]=='p')
			ret += "r" ;
		if(in[i]=='d')
			ret += "s" ;
		if(in[i]=='r')
			ret += "t" ;
		if(in[i]=='j')
			ret += "u" ;
		if(in[i]=='g')
			ret += "v" ;
		if(in[i]=='t')
			ret += "w" ;
		if(in[i]=='h')
			ret += "x" ;
		if(in[i]=='a')
			ret += "y" ;
		if(in[i]=='q')
			ret += "z" ;
		if(in[i]==' ')
			ret += " ";
	}
	return ret;
}

int main(){
	freopen ("A-small-attempt0.out","w",stdout);
	freopen ("A-small-attempt0.in","r",stdin);
	int t;
	cin>>t;
	string in;
	getline(cin,in);
	for(int i=0;i<t;i++){
		getline(cin,in);
		cout << "Case #" << i+1 <<": " << change(in) << endl ;
	}
	return 0;
}
