#include<iostream>
#include<vector>
#include<stdio.h>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("Output.txt","w",stdout);
	int count=0;
	int T, N, a,b;
	int z,j;
	vector<vector<int> > v;
	vector<int> v1;
	cin>>T;
	for(z=1;z<=T;z++){
		cin>>N;
		for(j=0;j<N;j++){
			cin>>a>>b;
			v1.push_back(a);
			v1.push_back(b);
			v.push_back(v1);
			v1.clear();
		}
		while(v.size()!=0){
			for(int j=1;j<v.size();j++){
				if( (v[0][0]<v[j][0] && v[0][1]>v[j][1]) || (v[0][0]>v[j][0] && v[0][1]<v[j][1]) )
					count++;
			}
			v.erase(v.begin(),v.begin()+1);
		}
		cout<<"Case #"<<z<<": "<<count<<endl;
		count=0;
		v.clear();
	}
	return 0;
}
