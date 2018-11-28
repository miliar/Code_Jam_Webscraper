

#include <iostream>
using namespace std;

int main()
{
	int n;
	cin>>n;
	for(int t=1;t<=n;++t)
	{
		cout<<"Case #"<<t<<": ";
		int n,m,a;
		cin>>n>>m>>a;
		bool ok = false;
		int ia,ja;
		for(int i=1;i<=n;++i){
			for(int j=1;j<=m;++j){
				if( i*j == a ){
					ok=true;
					ia = i;
					ja = j;
					break;
				}
			}
			if(ok)
				break;
		}
		if(ok){
			cout<<0<<' '<<0<<' '<<
				ia<<' '<<0<<' '<<
				ia<<' '<<ja<<endl;
			continue;
		}

		for(int i=1;!ok&&i<=n;++i){
			for(int j=1;!ok&&j<=m;++j){
				for(int p=1;!ok&&p<=i;++p){
					for(int q=1;!ok&&q<=j;++q){
						int area = 2*i*j - p*q - (i-p)*j - (j-q)*i ;
						if( area == a ){
							ok=true;
							cout<<p<<' '<<0<<' '
								<<0<<' '<<q<<' '
								<<i<<' '<<j<<endl;
							break;
						}
					}
					if(ok)
						break;
				}
			}
		}
		if(!ok)
			cout<<"IMPOSSIBLE"<<endl;
	}
}