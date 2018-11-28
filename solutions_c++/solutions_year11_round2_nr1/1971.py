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
	vs team;
	string buf;
	lli inps;
	vd wp, owpa, oowp;
	

	cin >> inps;
	for (lli i = 0; i < inps; i++){
		wp.clear();
		owpa.clear();
		oowp.clear();
		cout << "Case #" << i+1 << ":" << endl;
		lli N;
		cin >> N;
		team.clear();
		for (lli j = 0; j < N; j++){
			cin >> buf;
			team.pb(buf);
		}

		for (lli j = 0; j < N; j++){
			db res = 0;
			lli mats = 0;
			lli wins = 0;
			lli loses = 0;
			db owp = 0;
			for (lli k = 0; k < team[j].sz; k++){
				if (team[j][k] != '.'){
					mats++;
					lli mats2 = 0;
					lli wins2 = 0;
					lli loses2 = 0;
					for (lli l = 0; l < team[k].sz; l++){
						if (l != j)
							if (team[k][l] != '.'){
								mats2++;
								if (team[k][l] == '1')
									wins2++;
								else
									loses2++;
							}
					}
					owp+=(double)wins2/mats2;
					if (team[j][k] == '1')
						wins++;
					else
						loses++;
				}
			}
			wp.pb((double)wins/mats);
			owpa.pb((double)owp/mats);
		}
		for (lli j = 0; j < N; j++){
			db suc=0;
			lli mats3 = 0;
			for (lli k = 0; k < N; k++){
				if (j!=k&&team[j][k]!='.'){
					suc+=owpa[k];
					mats3++;
				}
			}
			oowp.pb((double)suc/mats3);
		}
		for (lli j = 0; j < N; j++){
			printf("%.12g\n", wp[j]*0.25 + owpa[j] * 0.5 + oowp[j] * 0.25);
		}
	}

	return 0;
}
