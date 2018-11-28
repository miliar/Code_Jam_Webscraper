#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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

#define forn(X,Y) for (int X = 0;X < Y;X++)
#define debug(x) cout << '>' << #x << ':' << x << '\n';

#define rep(X,Y,Z) for (int X = Y;X < Z;X++)
#define reset(Z,Y) memset(Z,Y,sizeof(Z))

#define sz(Z) ((int)Z.size())
#define all(W) W.begin(), W.end()
#define pb push_back

#define mp make_pair
#define A first
#define B second

#define inf 1023123123
#define eps 1e-11

#define MX(Z,Y) Z = max((Z),(Y))
#define MN(X,Y) X = min((X),(Y))

#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin();X!=(Y).end();X++)

using namespace std;

typedef long long ll;
typedef double db;
typedef vector<int> vint;

//ONE indexed

ll bit[3000005];
ll jmla[3000005];

struct FenwickTree {
	int n;
	
	FenwickTree (int _n) {
		n = _n;
		forn(i,n) bit[i+1] = 0;
		}
	void add (int pos, ll val) {
		while (pos <= n)		{
			//debug(n);
			//debug(pos);
			bit[pos] += val;
			pos += (pos & -pos);
			}
		}
	ll sum(int ending) {
		if (ending > n) ending = n;
		ll retval = 0;
		while (ending >= 1) {
			retval += bit[ending];
			ending -= (ending & -ending);
			}
		return retval;
		}
		
	ll sumarea(int mulai, int selesai) {
		if (mulai > selesai) return 0LL;
		return sum(selesai) - sum(mulai - 1);
		}
	};

int main() {
	//debug("irvan\n");
	int nc;
	//debug("irvan\n");
	scanf("%d",&nc);

	//debug("irvan\n");
	forn(z,nc) {
		printf("Case #%d: ",z+1);
		//debug("irvan\n");
		FenwickTree ir = FenwickTree(3000000);
		reset(jmla,0);
		//debug("irvan\n");
		int n;
		cin >> n;
	
		int tb = 1500000;
		ll steps = 0;
		forn(i,n) {
			//debug(i);
			//debug(steps);
			int a,b;
			cin >> a >> b;
			a += tb;
			db jawab = 0.0;
			int hitung = b;
			hitung /= 2;
			db tetet = 1.0;
			tetet /= 3.0;
			//debug("irvan");
			//debug(hitung);
			forn(i,3) {
				tetet *= (db)hitung;
				}
			jawab += tetet;
			tetet = 0.5;
			forn(i,2) {
				tetet *= (db)hitung;
				}
			jawab += tetet;
			tetet = 1.0 / 6.0;
			tetet *= (db)hitung;
			jawab += tetet;
			jawab += 0.1;
			//debug(jawab);
			steps += (ll)floor(jawab);
			//masukin ke input
			//debug("irvan");
			rep(j,a - b/2,a + b/2 + 1) {
				//debug(j);
				if (j == a && (b%2==0)) continue;
				//kalo kosong ditambah aja
			//	debug(bit[j]);
				if (jmla[j] == 0) {
					//debug(j);
					jmla[j] = 1;
					ir.add(j,1);
					continue;
					}
				//debug("irvanlagi");
				//debug(ir.sumarea(1,3000000));
				//kalo ngga...
				//cari ke kiri berapa yang 1
				//ada ga sih sebenernya?
				int kiri = 0;
				if (jmla[j-1]) {
					int leftlast = 1;
					int rightlast = j-1;
					while (rightlast >= leftlast) {
					
						//masi bisaaaaa
						int mid = (rightlast+leftlast)/2;
					//	debug(mid);
						int jml = ir.sumarea(mid,j-1);
						int jmlangka = j-1-mid+1;
						if (jml == jmlangka) {
							MX(kiri,jml);
							rightlast = mid-1;
							continue;
							}
						leftlast = mid+1;
						continue;
						}
					}
				int kanan = 0;
				if (jmla[j+1]) {
					int rightlast = 3000000;
					int leftlast = j+1;
					
					while (rightlast >= leftlast) {
						int mid = (rightlast+leftlast)/2;
					//	debug(mid);
						int jml = ir.sumarea(j+1,mid);
						int jmlangka = mid-j-1+1;
						if (jml == jmlangka) {
							MX(kanan,jml);
							leftlast = mid+1;
							continue;
							}
						rightlast = mid-1;
						}
					}
				//debug(kiri);
				//debug(kanan);
				//debug("irvanlagi");
				//si konjungsinya di enol in
				int plgkiri = j-kiri;
				int plgkanan = j+kanan;
				int deltakiri = j - plgkiri;
				int didelete = plgkanan - deltakiri;
				jmla[didelete] = 0;
				jmla[plgkiri-1] = 1;
				jmla[plgkanan+1] = 1;
			//	debug("sini");
				//debug(deltakiri);
				//debug(didelete);
				//debug(plgkiri);
				//debug(plgkanan);
				ir.add(didelete,-1);
				ir.add(plgkiri-1,1);
				ir.add(plgkanan+1,1);
				
				//tambah jawaban
			//	debug("sini");
				
				int total = kiri + kanan;
				ll sementara = 0LL;
				ll kali = total / 2 + 1;
				sementara = kali;
				if (total%2) sementara *= (kali+1); else sementara *= kali;
				int delta = abs(kanan-kiri) / 2;
				ll akhirnya=0;
				if (total%2 == 0) {
					akhirnya = (ll)delta * (ll)(delta+1) - (ll)delta;
					akhirnya = sementara - akhirnya;
					}
				else {
					akhirnya = (ll)delta * (ll)(delta+1);
					akhirnya = sementara - akhirnya;
					}
				
				steps += akhirnya;
				}
//debug("irvan");
			
			}
		
		cout << steps;
		cout << endl;
		}
		
			
			
		
	
	return 0;
	}


//Powered by [KawigiEdit] 2.0!









