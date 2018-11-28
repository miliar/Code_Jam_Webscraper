#include<cstdio>
#include<iostream>
#include<string>
#include<cstring>

using namespace std;

int T,c,d,n;
string tmp;
char com[50][50], opp[50];
char ans[2000];

inline int To(char ch){
	return (int)ch-65;
}

int main(){
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	
	cin>>T;
	for (int loop=1; loop<=T; loop++){
		memset(com, 0, sizeof(com));
		memset(opp, 0, sizeof(opp));
		
		cin>>c;
		for (int i=1; i<=c; i++){
			cin>>tmp;
			com[To(tmp[0])][To(tmp[1])] = tmp[2];
			com[To(tmp[1])][To(tmp[0])] = tmp[2];
		}
		
		cin>>d;
		for (int i=1; i<=d; i++){
			cin>>tmp;
			opp[To(tmp[0])] = tmp[1];
			opp[To(tmp[1])] = tmp[0];
		}
		
		cin>>n;
		cin>>tmp;
		int cnt = 0;
		for (int i=0; i<tmp.length(); i++){
			ans[++cnt] = tmp[i];
			while (cnt>1 && com[To(ans[cnt-1])][To(ans[cnt])]!=0){
				ans[cnt-1] = com[To(ans[cnt-1])][To(ans[cnt])];
				cnt--;
			}
			
			for (int j=cnt-1; j>0; j--){
				if (opp[To(ans[j])]==ans[cnt]){
					cnt = 0;
					break;
				}
			}
		}
		
		cout<<"Case #"<<loop<<": [";
		for (int i=1; i<cnt; i++)	cout<<ans[i]<<", ";
		if (cnt>0)	cout<<ans[cnt]<<']'<<endl;
		else cout<<']'<<endl;
	}
}