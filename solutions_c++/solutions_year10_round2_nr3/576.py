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
int a[25]={-1,1,2,3,5,8,14,24,43,77,140,256,472,874,1628,3045,5719,10780,20388,38674,73562,140268,268066,513350,984911};
int main(){
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.out","w",stdout);

	int tt;
	cin>>tt;
	for(int t=1;t<=tt;++t){
		
		int n;
		cin>>n;
		cout<<"Case #"<<t<<": ";
		cout<<a[n-1]%100003<<endl;
		continue;
		int rez=0;
		for(int base=(1<<(n-1));base<(1<<n);base+=2){
			int cur=n;
			int yes=1;
			while(cur>1){
				if(!((base>>(cur-1))%2)){
					yes=0;
					break;
				}
				int newcur=0;
				for(int i=0;i<cur;++i){
					newcur+=((base>>i)%2);
				}
				cur=newcur;
			}
			rez+=yes;
		}
		cout<<"Case #"<<t<<": ";
		cout<<rez;
		cout<<endl;
	}
	return 0;
}