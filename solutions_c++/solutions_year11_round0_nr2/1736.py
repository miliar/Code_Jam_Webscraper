#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

vector<char> col;
char comb[26][26];
bool oppo[26][26];
int cnt[26];

int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	int t; cin>>t;
	int c,d,n;
	char c1,c2,c3;
	for (int k=1; k<=t; k++) {
		col.clear();
		memset(comb,0,sizeof(comb));
		memset(oppo,0,sizeof(oppo));
		memset(cnt,0,sizeof(cnt));

		cin>>c;
		for (int i=0; i<c; i++) {
			cin>>c1>>c2>>c3;
			comb[c1-'A'][c2-'A']=comb[c2-'A'][c1-'A']=c3;
		}
		cin>>d;
		for (int i=0; i<d; i++) {
			cin>>c1>>c2;
			oppo[c1-'A'][c2-'A']=oppo[c2-'A'][c1-'A']=true;
		}
		cin>>n;
		for (int i=0; i<n; i++) {
			cin>>c1; cnt[c1-'A']++;
			col.push_back(c1);
			int len = col.size();
			if (len>1 && (c2=comb[col[len-1]-'A'][col[len-2]-'A'])!=0) {
				cnt[col[len-1]-'A']--;
				cnt[col[len-2]-'A']--;
				col.pop_back(); col.pop_back();
				col.push_back(c2);
				cnt[c2-'A']++;
				len--;
			}
			for (int j=0; j<len-1; j++) {
				if (cnt[col[j]-'A']>0 && cnt[col[len-1]-'A']>0 && oppo[col[j]-'A'][col[len-1]-'A']) {
					col.clear();
					memset(cnt,0,sizeof(cnt));
					break;
				}
			}
		}
	
		cout<<"Case #"<<k<<": [";
		for (int i=0; i<col.size(); i++) {
			if (i!=0) cout<<", ";
			cout<<col[i];
		}
		cout<<"]\n";
	}
}
