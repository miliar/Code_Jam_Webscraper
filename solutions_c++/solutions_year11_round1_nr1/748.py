#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <functional>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

#define bg begin()
#define br break;
#define cl ceil
#define en end()
#define fl floor
#define fr(a,b,c) for(unsigned long long int a=b;a<c;a++)
#define lw 97
#define mp make_pair
#define nm 48
#define pb push_back
#define rp(a,b) for(unsigned long long int a=0;a<b;a++)
#define rs resize
#define rt return
#define sr sort
#define sz size()
#define up 65
#define wh while

typedef bool bl;
typedef double db;
typedef long long int lli;
typedef pair<double,double> pdd;
typedef pair<double,int> pdi;
typedef pair<double,string> pds;
typedef pair<int,double> pid;
typedef pair<int,int> pii;
typedef pair<int,string> pis;
typedef pair<string,double> psd;
typedef pair<string,int> psi;
typedef pair<string,string> pss;
typedef string st;
typedef vector<int> vi;
typedef vector<long long int> vl;
typedef vector<double> vd;
typedef vector<string> vs;

int main()
{
	lli inps;
	cin >> inps;
	
	for(lli i = 1; i<=inps; i++){
		lli N, D, G;
		cin >> N;
		cin >> D;
		cin >> G;
		if (D==0) {
			if(G!=100) {
				cout << "Case #" << i << ": Possible" << endl;
				continue;
			}
			else {
				cout << "Case #" << i << ": Broken" << endl;
				continue;
			}
		}
		if(G==0){
			if(D==0) {
							cout << "Case #" << i << ": Possible" << endl;
							continue;
			}
						else {
							cout << "Case #" << i << ": Broken" << endl;
							continue;
						}
		}

		if (D < 100 && G == 100) {
			cout << "Case #" << i << ": Broken" << endl;
			continue;
		}
		if(D==100) {
			cout << "Case #" << i << ": Possible" << endl;
			continue;
		}
		else {
			for(lli j = min(D, (100-D)); j >= 1; j--) {
				if(D%j==0&&((100-D)%j==0))
					if(100/j<=N) {
						cout << "Case #" << i << ": Possible" << endl;
						goto next;
					}
					else {
						cout << "Case #" << i << ": Broken" << endl;
						goto next;
					}
			}
		}
		next:;
	}

	return 0;
}
