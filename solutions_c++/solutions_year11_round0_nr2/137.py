#include <iostream>

bool ops[300][300];
int num[300],com[300][300],sa[300];

using namespace std;
int main(){
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int t;
	cin >> t;
	for (int u=1;u<=t;u++){
		memset(ops,0,sizeof(ops));
		memset(com,0,sizeof(com));
		int c,d,n;
		char ch;
		cin >> c;
		scanf("%c",&ch); 
		char ca,cb,cc;
		for (int i=0;i<c;i++){
			
			scanf("%c%c%c%c",&ca,&cb,&cc,&ch);
			com[cb][ca]=com[ca][cb]=cc;			
		}
		scanf("%d%c",&d,&ch);
		for (int i=0;i<d;i++){
			scanf("%c%c%c",&ca,&cb,&ch);
			ops[ca][cb]=ops[cb][ca]=true;
		}
		scanf("%d%c",&n,&ch);
		int l=0,r=-1;
		memset(num,0,sizeof(num));

		for (int i=0;i<n;i++){
			scanf("%c",&ch);
		//	cout << r<<sa<<endl;
			if (r>=l) {
				if (com[sa[r]][ch]) {
					num[sa[r]]--;
					num[com[sa[r]][ch]]++;
				   	sa[r]=com[sa[r]][ch];
				  	 
				
				} else {
					sa[++r]=ch;
					num[ch]++;
					for (char chh='A';chh<='Z';chh++) {
						if (ops[chh][ch]&&num[chh]) {
							memset(num,0,sizeof(num));
							r=-1;
							break;
						}
					}	
				}
			} else {sa[++r]=ch; num[ch]++;}
		}
		cout <<"Case #"<<u<<": [";
		if (r>=l) {
			cout << (char)sa[0];
			for (int i=1;i<=r;i++) {
				cout <<", "<<(char)sa[i];
			}
		}
		cout <<']'<<endl;
	}

}
