#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
	vector<int> v;
	vector<int>v1;
	int x;
	int n;
	cin >>n;
	
	for(int t=0; t<n; t++){
		bool f=0;
		v.clear(),v1.clear();
		int p;
		cin >>p;
		for(int c=0; c<p; c++){
			cin >> x;
			v.push_back(x);
		}
		sort(v.begin(),v.end());
		int sum = 0;
		for(int i=0; i<p; i++){
			sum = 0;
			int temp=0;
			for(int j=0; j<p; j++){
				if(j!=i){
					temp=temp^v[j];
				}
			}
			if(temp==v[i]){
				for(int j=0; j<p; j++){
					if(j!=i)
						sum+=v[j];
				}
			f=1;
			break;
			}
		}
		if(f==1){
			cout << "Case #" <<t+1<<": " << sum << endl;
		}
		else 
			cout << "Case #" <<t+1<<": " << "NO" << endl;
	}
	return 0;
}						 
