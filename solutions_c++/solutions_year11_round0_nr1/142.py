
#include <iostream>

using namespace std;

int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int t;
	cin >>t;
	for (int u=0;u<t;u++){
		int n;
		cin >> n;
		int ans=0;
		int timo=0,timb=0,poo=1,pob=1;
		char cha;
		
		for (int i=0;i<n;i++) {
			char ch;
			int w;
			
			scanf("%c%c%d",&cha,&ch,&w);
			if (ch=='O') {
				timo= max(timo+abs(w-poo)+1,ans+1);
				ans=max(ans,timo);
				poo=w;
			} else {
				timb= max(timb+abs(w-pob)+1,ans+1);
				ans=max(ans,timb);
				pob=w;
			}
			
		}
		cout <<"Case #" <<u+1<<": "<<ans<<endl;
	}
	return 0;
}
