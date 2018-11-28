#include<iostream>
#include<cstdio>
#include<cmath>
#include<vector>
#include<string>
#include<algorithm>
#include<set>
#include<map>
#include<list>
using namespace std;

int main(){
	//freopen("b.in","r",stdin);
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	int tt;
	cin>>tt;
	for(int t=1;t<=tt;++t){
		int c,l0,p0;
		cin>>l0>>p0>>c;
		//cout<<l0<<' '<<p0<<' '<<c<<' ';
		
		int l=l0,p=p0;
		int kil=0;
		while((p/double(l))>double(c)){
			double z1=sqrt(double(p)*double(l));
			int z=int(sqrt(double(p)*double(l)));
			if(z1-double(z)>=0.5)
				z++;
			if(z==l)
				z++;
			double k1=(z)/double(l);
			double k2=double(p)/(z);
			if(k1>k2)
				p=z;
			else
				l=z;
			kil++;
		}

		cout<<"Case #"<<t<<": ";
		cout<<kil;
		cout<<endl;
	}
	return 0;
}