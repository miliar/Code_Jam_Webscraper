#include <iostream>
#include <vector>

using namespace std;

int main() {
	int tn;
	cin >> tn;
	for(int ti = 0; ti < tn;) {
		int tat, tbt, na, nb;
		cin >> tat >> na >> nb;
		int *aa = new int[na], *ad = new int[na], *ba = new int[nb], *bd = new int[nb];
		for(int i = 0, t; i < na; i++)
			cin >> t, cin.ignore(), ad[i] = 60 * t, cin >> t, ad[i] += t, cin >> t, cin.ignore(), aa[i] = 60 * t + tat, cin >> t, aa[i] += t;
		for(int i = 0, t; i < nb; i++)
			cin >> t, cin.ignore(), bd[i] = 60 * t, cin >> t, bd[i] += t, cin >> t, cin.ignore(), ba[i] = 60 * t + tat, cin >> t, ba[i] += t;
		for(int i = 0; i < na; i++)
			for(int j = i + 1, t; j < na; j++)
				if(ad[i] > ad[j]) t = ad[i], ad[i] = ad[j], ad[j] = t, t = aa[i], aa[i] = aa[j], aa[j] = t;
		for(int i = 0; i < nb; i++)
			for(int j = i + 1, t; j < nb; j++)
				if(bd[i] > bd[j]) t = bd[i], bd[i] = bd[j], bd[j] = t, t = ba[i], ba[i] = ba[j], ba[j] = t;
		tat = tbt = 0;
		int ia = 0, ib = 0;
		vector <int> a, b;
		for(int i = na + nb, actr = 0, bctr = 0; i; i--)
			if(na - ia && (ib == nb || ad[ia] < bd[ib])) {
				int t = a.size();
				if(t && a[t - 1] <= ad[ia]) a.pop_back();
				else tat++;
				if(!(t = b.size()) || b[--t] > aa[ia]) b.push_back(aa[ia]);
				else {
					while(t--)
						if(b[t] > aa[ia]) break;
					b.insert(b.begin() + (t + 1), aa[ia]);
				}
				ia++;
			}
			else {
				int t = b.size();
				if(t && b[t - 1] <= bd[ib]) b.pop_back();
				else tbt++;
				if(!(t = a.size()) || a[--t] > ba[ib]) a.push_back(ba[ib]);
				else {
					while(t--)
						if(a[t] > ba[ib]) break;
					a.insert(a.begin() + (t + 1), ba[ib]);
				}
				ib++;
			}
		cout << "Case #" << ++ti << ": " << tat << ' ' << tbt << endl;
	}
	return 0;
}
