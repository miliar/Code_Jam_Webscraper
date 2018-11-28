#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int c;
	int j=1;
	int dim,t,res;
	vector<int> a;
	vector<int> b;
	cin>>c;
	while(c) {
		res=0;
		cin>>dim;
		for(int i=0;i<dim;i++)
		{
			cin>>t;
			a.push_back(t);
		}
		for(int i=0;i<dim;i++)
		{
			cin>>t;
			b.push_back(t);
		}
		sort(a.begin(),a.end());
		sort(b.begin(),b.end());
		//for(int i=0;i<dim;i++)
		//	cout<<a[i]<<" ";
		//cout<<endl;
		//for(int i=0;i<dim;i++)
		//	cout<<b[i]<<" ";
		//cout<<endl;
		for(int i=0;i<dim;i++)
			res+=a[i]*b[dim-1-i];
		cout<<"Case #"<<j<<": "<<res<<endl;
		a.clear();
		b.clear();
		
			
		
		
		c--;
		j++;
	}
	return 0;
}
	