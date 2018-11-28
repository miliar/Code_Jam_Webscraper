#include<iostream>
#include<string>
using namespace std;

int		n, i, j, k, t, L, D, N, ans;

string  w[5008], s;

bool	b[20][256], flg;

int		main(){
		//freopen("input.txt","r",stdin);
		//freopen("output.txt","w",stdout);
		cin>>L>>D>>N;
		for(i=0; i<D; i++) cin>>w[i];
		for(n=1; n<=N; n++){
			cin>>s;
			memset(b, 0, sizeof(b));
			for(k=t=j=0; j<s.size(); j++){
				if (s[j]=='('){ t = 1; continue; }
				if (s[j]==')'){ t = 0; k++; continue; }
				b[k][s[j]] = true;
				if (t==0) k++;
			}
			ans = 0;
			for(i=0; i<D; i++){
				flg = true;
				for(j=0; j<L; j++) flg &= b[j][w[i][j]];
				if (flg) ans++;
			}
			cout<<"Case #"<<n<<": "<<ans<<endl;
		}
		return 0;
}
