#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

int main() {
	int T;
	cin>>T;
	vector<int> bulbs(T);
	vector<int> snaps(T);
	for(int i=0;i<T;i++)
		cin>>bulbs[i]>>snaps[i];
	for (int i=0;i<T;i++) {
		int normalized =  2 << (bulbs[i]-1);
		cout<<"Case #"<<i+1<<": ";
		if (!((snaps[i]+1)%normalized)) cout<<"ON"<<endl;
		else cout<<"OFF"<<endl;
	}
}
