#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
bool cmp(int a,int b) {return a>b;}
int main() {
	int hede=1;
	int C;
	long he;
	int P,K,L;
	int t;
	int j;
	vector<int> a;
	cin>>C;
	while(C) {
		cin>>P>>K>>L;
		for(int i=0;i<L;i++)
		{
			cin>>t;
			a.push_back(t);
		}
		sort(a.begin(),a.end(),cmp);
		//cout<<"=="<<endl;
		//for(int i=0;i<L;i++)
		//	cout<<a[i]<<" ";
		j=1;
		he=0;
		for(int i=0;i<L;)
		{
			for(int x=0;x<K;x++)
			{
				if(i==L) break;
				he+=a[i]*j;
				i++;
			}
			j++;
		}
		
		cout<<"Case #"<<hede<<": "<<he<<endl;
		
		a.clear();
		hede++;
		C--;
	}
	return  0;
}