#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(int argc, char *argv[]) {
	int n, t;
	cin>>t;
	for (int i=0;i<t;i++){
		cin>>n;
		bool e=0;
		vector<int> c;
		int vxor, a, sm=0, s=0;
		for (int j=0; j<n;j++){
			cin>>a;
			c.push_back(a);
		}
		sort(c.begin(), c.end());
		for(int j=1;j<n;j++){
			for(int k=0;k<j;k++){
				sm+=c[k];
			}
			vxor=c[j];
			s=c[j];
			for(int l=j+1;l<n;l++){
				vxor=vxor^c[l];
				s+=c[l];
			}
			if (sm==vxor){
				cout<<"Case #"<<i+1<<": "<<s<<endl;
				e=1;
				break;}
		}
		if (!e)
			cout<<"Case #"<<i+1<<": NO"<<endl;
	}
	return 0;
}

