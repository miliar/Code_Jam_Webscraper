#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main(){
	int n,t,tot;
	int a[2000],b[2000];
	cin>> t;
	for(int y=1;y<=t;y++){
		tot=0;
		cin >> n;
		for(int i=0;i<n;i++){
			cin >> a[i] >> b[i];
		}
		for(int i=0;i<n;i++){
			for(int j=i+1;j<n;j++){
				if((a[i]-a[j])*(b[i]-b[j])<0)tot+=1;
			}
		}
		cout<< "Case #"<<y<<": "<<tot<<endl;
	}
}
