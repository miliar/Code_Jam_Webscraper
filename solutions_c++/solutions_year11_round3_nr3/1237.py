#include<iostream>
using namespace std;
const int N = 10003;
int main(){
	int T;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int n,l,h;
	int flag;
	int a[N];
	cin>>T;
	int i,j;
	int cas=1;
	while(T--){
		cin>>n>>l>>h;
		for(i=0;i<n;i++)
			cin>>a[i];
		for(j=l;j<=h;j++){
			flag=0;
			for(i=0;i<n;i++){
				if(a[i]%j!=0&&j%a[i]!=0){
					flag=1;
					break;
				}
			}
			if(flag==0)
				break;
		}
		cout<<"Case #"<<cas++<<": ";
		if(flag==0)
			cout<<j<<endl;
		else
			cout<<"NO"<<endl;
	}
	return 0;
}