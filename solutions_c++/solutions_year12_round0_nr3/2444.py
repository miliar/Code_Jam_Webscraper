#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;

long long re[10];
int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int N;
	cin>>N;
	for(int k=0;k<N;k++){
		long res=0;
		long long a,b;
		cin>>a>>b;
		if (a>=10&&b>=10){ 
			int signs=1;
			long long step=1;
			long long t=a;
			while (t>=10) {t=t/10;signs++;step*=10;}
			for(long long i=a;i<=b;i++){
				long long ii=i;
				for(int p=0;p<signs;p++){
					long long last=ii%10;
					ii/=10;
					if (last!=0) {
						ii+=last*step;
						re[p]=ii;
						if (ii>i&&ii<=b) {
							bool f=false;
							for(int j=p-1;j>-1;j--){if (re[j]==ii) {f=true;break;}}
							if (!f) res++; 
						}
					}
				}
			}
		}
		cout<<"Case #"<<k+1<<": "<<res<<endl;
	}
	return 0;
}


