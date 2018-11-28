#include<iostream>
#include<vector>
#include<string>

#define NUM 26
using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T; cin>>T;
	for (int t=1; t<=T; t++) {
		vector<string> C,D;
		int c,d,n;
		string s;

		cin>>c;
		for (int i=0; i<c; i++) {
			cin>>s; C.push_back(s);
		}
		
		cin>>d;
		for (int i=0; i<d; i++) {
			cin>>s; D.push_back(s);
		}

		cin>>n;

		int counter[NUM];
		for (int i=0; i<NUM; i++) counter[i]=0;

		string curr;
		while(n--) {
			char ch; cin>>ch;
			int sz=curr.size();
			if(sz==0) { curr+=ch; counter[ch-'A']++; }
			else {
				char ch2=curr[sz-1];
				bool flag=false;
				for (int i=0; i<c; i++) {
					char c1=C[i][0], c2=C[i][1];
					if((ch==c1&&ch2==c2)||(ch==c2&&ch2==c1)) {
						counter[ch2-'A']--;
						curr[sz-1]=C[i][2];
						flag=true;
						break;
					}
				}

				if(!flag) {
					curr+=ch;
					counter[ch-'A']++;
					for (int i=0; i<d; i++) {
						if(counter[D[i][0]-'A'] && counter[D[i][1]-'A']) {
							curr="";
							for (int i=0; i<NUM; i++) counter[i]=0;
							break;
						}
					}
				}
			}
		}

		int sz=curr.size();
		cout << "Case #" << t << ": [";
		if(sz!=0) {
			cout << curr[0];
			for (int i=1; i<sz; i++) cout << ", " << curr[i];
		}
		cout << "]" << endl;
	}
	return 0;
}
