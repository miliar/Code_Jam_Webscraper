#include<iostream>
#include<algorithm>
#include<cmath>

using namespace std;

int main(){
	int a[110];
	char ch[110];
//	int o[110],b[110];
	int po,pb;
	int flag;
	int sum;
	int x,y,z;
	int t,n;
	cin>>t;
	//scanf("%di",&t);
	//cin>>t;
	for(int i=1;i<t+1;i++){
		//scanf("%c %d"
		po=1;
		pb=1;
		flag=0;
		sum=0;
		cin>>n;
		for(int j=0;j<n;j++){
			cin>>ch[j]>>a[j];
		}
		x=0;
		for(int j=0;j<n;j++){
			if(ch[j]=='O'){
				if(flag==2){
					if(x>abs(a[j]-po)){
						sum+=x;
						x=1;
					}else{
						sum+=x;
						x=abs(a[j]-po)-x+1;
					}
					po=a[j];
					flag=1;
				}else{
					x+=abs(a[j]-po)+1;
					po=a[j];
					flag=1;
				}
			}else{
				if(flag==1){
					if(x>abs(a[j]-pb)){
						sum+=x;
						x=1;
					}else{
						sum+=x;
						x=abs(a[j]-pb)-x+1;
					}
					pb=a[j];
					flag=2;
				}else{
					x+=abs(a[j]-pb)+1;
					pb=a[j];
					flag=2;
				}

			}
		}
		sum+=x;
		cout<<"Case #"<<i<<": "<<sum<<endl;
	}
	return 0;
}
