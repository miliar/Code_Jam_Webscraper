#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

int main() {
	int t;
	cin >> t;
	
	for (int i=0;i<t;i++) {
		int c,d,n;
		
		vector<int> list;
		int combinemap[128]={0}; // map[a] = t:b
		int opposemap[128]={0};
		
		cin >> c;
		for (int j=0;j<c;j++) {
			string s;
			cin >> s;
			combinemap[s[0]] = (s[1]&0xff) | (s[2]<<8)&~0xff;
			combinemap[s[1]] = (s[0]&0xff) | (s[2]<<8)&~0xff;
		}
		
		cin >> d;
		for (int j=0;j<d;j++) {
			string s;
			cin >> s;
			opposemap[s[0]] = s[1];
			opposemap[s[1]] = s[0];
		}

		cin >> n;
		for (int j=0;j<n;j++) {
			char cc;
			cin >> cc;
			//cout << cc << endl;
			if (list.size()>0) {
				if ((char)combinemap[cc] == list.back()) {
					list.back() = (char)(combinemap[list.back()]>>8);
					continue;
				}
			}
			if (opposemap[cc]) {
				for (int k=0;k<list.size();k++) {
					if (opposemap[cc] == list[k]) {
						list.clear();
						//list.erase(list.begin()+k,list.end());
						cc = 0;
						break;
					}
				}
			}

			if (cc) list.push_back(cc);
		}
/*		
		// combine
		int p=0;
		while (p+1<list.size()) {
			if ((char)combinemap[list[p]] == (char)list[p+1]) {
				//cout << (char)list[p+1] << " ? " << (char)combinemap[list[p]] << " > " << (char)(combinemap[list[p]]>>8)<< endl;
				list.erase(list.begin()+p);
				list[p] = (char)(combinemap[list[p]]>>8);
				if (p>1) p--;
				continue;
			}
			p++;
		}
*/
		// oppose
//		int p=0;
//		while (p+1<list.size()) {
//			p++;
//		}

		cout << "Case #" << (i+1) << ": [";
		for (int i=0;i<list.size();i++) {
			cout << (char)list[i];
			if (i<list.size()-1) cout << ", ";
		}
		cout << "]" << endl;
	
	}

	return 0;
}
