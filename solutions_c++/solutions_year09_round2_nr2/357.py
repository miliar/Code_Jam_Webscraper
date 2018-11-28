#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;
typedef long long int lint;
typedef pair<int,int> par;
 
#define sz size
#define pb push_back
#define all(x) (x).begin() , (x).end()
#define sqr(x) (x)*(x)
#define x first
#define y second
#define rep(i,n)  for (int (i)=0;(i)<(int)(n);(i)++)
#define Rep(i,a,n) for (int (i)=(int)(a);(i)<(int)(n);(i)++)


int main() {
	int t;
	cin >> t;
	for (int i=1;i<=t;i++) {
		string s;
		cin >> s;
		int e1 = 0;
		int small = 110;
		for (int j=int(s.sz()-1);j>=1;j--) {
			if (s[j] > s[j-1])
				e1 = 1;
			if (s[j] < small && s[j] != '0')
				small = s[j];
		}
		if (s[0] < small && s[0] != '0')
			small = s[0];
		if (e1 == 0) {
			string fim = "A0";
			fim[0] = small;
			int f = 0;
			for (int j=int(s.sz()-1);j>=0;j--) {
				if (small == s[j] && f == 0)
					f=1;
				else
					fim+=s[j];
			}
			cout << "Case #" << i << ": " << fim << endl;
		}
		small = 110;
		
		for (int k=(int)s.sz()-1;k>=0;k--) {
			char r = (char)100;
			char vec[100]={};
			for (int j=k;j<(int)s.sz();j++) {
				if (s[j]>s[k] && s[j] < r)
					r = s[j];
				vec[(int)s[j]]++;		
			}
			if (r != (char)100) {
				string fim = s.substr(0,k);
				fim+=r;
				vec[(int)r]--;
				for (int j=(int)'0';j<=(int)'9';j++) {
					for (int z=0;z<vec[j];z++)
						fim+=(char)j;				
				}
				cout << "Case #" << i << ": " << fim << endl;
				break;
			}			
		}
		
		/*
		for (int j=int(s.sz()-1);j>=1;j--) {
			if (s[j] < small && s[j] != '0')
				small = s[j];
			
			if (s[j] > s[j-1] && s[j-1] != '0') {
				char tmp = s[j-1];
				s[j-1] = s[j];
				s[j] = tmp;
				cout << "Case #" << i << ": " << s << endl;
				break;
			}
			else {
				if (s[j] > s[j-1]) {
					string sm = "A";
					sm[0] = small;
					string fim = s.substr(0,j-1) + sm + "0";
					int f = 0;
					int zero = 0;
					for (int z=j;z<int(s.sz()-1);z++) {
						if (small == s[z] && f == 0)
							f=1;
						else {
							if (s[z]=='0' && zero == 0)
								zero = 1;
							else
								fim+=s[z];
						}
					}
					cout << "Case #" << i << ": " << fim << endl;
					break;
				}
			}
		}
		*/
	
	}
	return 0;
}

