#include <iostream>

using namespace std;

int main(){
	
	int t,x,n,sum,min,flag;
	cin >> t;
	for (int casei=1; casei<=t;casei++){
		cin >> n;
		sum=0;
		flag=0;
		min=0xffffff;
		for (int i=0;i<n;i++){
			cin >> x;
			if (x < min)
				min=x;
			sum+=x;
			flag^=x;
		}
		cout << "Case #"<<casei<<": ";
		if(flag)
			cout << "NO" <<endl;
		else
			cout<<sum-min<<endl;
	}
	return 0;
}
