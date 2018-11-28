#include <iostream>
using namespace std;
int main(){
	int t,n,k,i,j,z,v[60],x[60],tot;
	string str;
	cin >> t;
	for(int q=1;q<=t;q++){
		cin>>n;
		z=1;
		for(i=0;i<n;i++){
			cin >> str;
//			cout<<str<<endl;
			v[i]=0;			
			for(j=0;j<n;j++){
				v[i]*=2;
				v[i]+=str[j]-'0';
			}			
//			cout<<v[i]<<endl;
			x[i]=0;
			z*=2;
		}
		z/=2;
		tot=0;
		while(z>0){
//			cout<<z<<endl;
			for(i=0;i<n;i++)
				if(x[i]==0 && v[i]%z==0){
//					cout<<"divisibile per "<<z<< ": "<<v[i]<<endl;
					for(j=0;j<i;j++){
						if(x[j]==0)
							tot++;
					}
					x[i]=1;
					break;
				}
			z/=2;
		}
		cout<<"Case #"<<q<<": "<<tot<<endl;
	}
}
