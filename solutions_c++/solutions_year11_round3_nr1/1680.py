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
#define clr clear()
#define en end()
#define fl floor
#define fr(a,b,c) for(unsigned long long int a=b;a<c;a++)
#define lw 97
#define mp make_pair
#define nm 48
#define pb push_back
#define rp(a,b) for(unsigned long long int a=0;a<b;a++)
#define rsz resize
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
typedef vector<long long int> vlli;
typedef vector<double> vd;
typedef vector<string> vs;



int main()
{
	lli inps;

	cin >> inps;

	rp(i, inps){
		cout << "Case #" << i + 1 << ":" << endl;
		vs str;
		str.clr;
		lli R;
		cin >> R;
		lli C;
		cin >> C;
		string buf;
		rp(j,R){
			cin >> buf;
			str.pb(buf);
		}
		while(1){
			lli k;
			lli a = 0;
			lli b = 0;
			rp (j, R){
				rp(k, C){
					if(str[j][k]=='#') {
						str[j][k]='/';
						goto next;
					}
					b++;
				}
				a++;
				b=0;
			}
			rp(j, R){
				cout << str[j] << endl;
			}
			goto next2;
			next:;
			if(str[a][b+1]=='#')
				str[a][b+1]='\\';
			else {
				cout << "Impossible" << endl;
				goto next2;
			}
			if(a+1 < str.sz && str[a+1][b]=='#')
				str[a+1][b]='\\';
			else {
				cout << "Impossible" << endl;
				goto next2;
			}
			if(a+1 < str.sz && str[a+1][b+1]=='#')
				str[a+1][b+1]='/';
			else {
				cout << "Impossible" << endl;
				goto next2;
			}
		}
		next2:;
	}

	return 0;
}
