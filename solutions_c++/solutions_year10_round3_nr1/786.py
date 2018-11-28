#include<iostream>
#include<vector>
#include<map>
#include<string>

using namespace std;

int main(){
	int n;
	int x,y,c;
	int t;
	int a[1000],b[1000];
	cin>>t;	
	for(int w=0;w<t;w++){
		cin>>n;
		c=0;
		for(int i=0;i<n;i++){
			cin>>x>>y;
			a[i]=x;
			b[i]=y;
		}
		for(int i=0;i<n-1;i++){
			for(int j=i+1;j<n;j++){
				if(a[i]>a[j] && b[i]<b[j]){
					c++;
				}else if(a[i]<a[j] && b[i]>b[j]){
					c++;
				}
			}
		}
		cout<<"Case #"<<w+1<<": "<<c<<endl;
	}
	return 0;
}
