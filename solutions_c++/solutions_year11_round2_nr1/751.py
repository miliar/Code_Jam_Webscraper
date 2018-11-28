# include <cstdio>
# include <iostream>
# include <fstream>
# include <algorithm>
# include <vector>
# include <string>
# include <set>
# include <utility>
# include <map>
# include <queue>
# include <stack>
# include <list>
# include <bitset>
# include <deque>
# include <cassert>
# include <iomanip>
# include <cmath>
# define pb push_back
# define forn(i,n) for (int i=0; i<(int)n; ++i)
# define ford(i,n) for (int i=n-1; i>=0; --i)
# define get(a,b); a b; cin >> b;
# define ull unsigned long long
# define ll long long
# define ld long double
# define mp make_pair
# define matrix vector < vector <int> > 
# define all(a) a.begin(), a.end()
# define INF 1e9
# define eps 1e-9
using namespace std;

int main(){
	ifstream cin ("input.txt");
	ofstream cout ("output.txt");
	int t;
	cin >> t;
	forn(iter,t){
		int n;
		cin >> n;
		string ln;
		vector <vector <int> > tab(n,vector <int> (n,-1));
		getline(cin,ln,'\n');
		forn(i,n){
			getline(cin,ln,'\n');
			forn(j,ln.size())
				if (ln[j] >='0' && ln[j]<='1'){
					tab[i][j] = ln[j]-'0';
				}
		}
		vector <double> wp;
		forn(i,n){
			double s,k;
			s = k = 0;
			forn(j,n)
				if (tab[i][j]>=0){
					k++;
					s+=tab[i][j];
				}
			wp.pb(s/k);
		}
		vector <double> owp(n,0);
		forn(i,n){
			double sum = 0,kkk = 0;
			forn(j,n)
				if (tab[i][j]>=0){
					double s,k;
					s = k = 0;
					forn(l,n)
						if (tab[j][l]>=0 && l!=i){
							s+=tab[j][l];
							k++;
						}
					sum += s/k;
					kkk++;
				}
			owp[i] = sum/kkk;
		}
		vector <double> oowp(n,0);
		forn(i,n){
			double s = 0,k=0;
			forn(j,n)
				if (tab[i][j]>=0){
					s += owp[j];
					k++;
				}
			oowp[i] = s/k;
		}
		vector <double> ans;
		forn(i,n)
			ans.pb(0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
		cout << "Case #" << iter+1 << ":\n";
		forn(i,n)
			cout << ans[i] << endl;
	}
    return 0;
}
