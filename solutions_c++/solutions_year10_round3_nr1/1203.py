#include <iostream>
#include <utility>
#include <vector>


using namespace std;

int main(){
	int i,a,b,z;
	cin>>i;
	for(int j=0;j<i;j++){
		vector<pair<int,int> > v;
		cin>>z;
		int counter=0;
		while(z--){
			cin>>a>>b;
			pair<int,int> c(a,b);
			for(int k=0;k<v.size();k++){
				if(v[k].first<c.first && v[k].second>c.second)
				{
					++counter;
					continue;
				}			
				if(v[k].first>c.first && v[k].second<c.second)
					++counter;
			}
			v.push_back(c);
		}
		cout<<"Case #"<<j+1<<": "<<counter<<endl;	
	}
}
