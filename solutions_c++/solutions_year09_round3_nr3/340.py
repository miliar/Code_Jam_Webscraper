#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<algorithm>
#include<set>
#include<map>
#include<cstring>
using namespace std;

int main(){
	int n;
	cin >> n;
	for(int i=0 ; i<n ; i++){
		int cell,num;
		cin >> cell >> num;
		vector<int> vi;
		for(int j=0 ; j<num ; j++){
			int temp; cin >> temp;
			vi.push_back(temp);
		}
		int ans=100000;
		while(1){
			int cnt=0;
			for(int j=0 ; j<vi.size() ; j++){
				int cur=vi[j];
				int left=0,right=cell+1;
				for(int k=0 ; k<j ; k++){
					if(vi[k]<cur && left<vi[k]) left=vi[k];
					if(cur<vi[k] && vi[k]<right)right=vi[k];
				}
				cnt+=cur-left-1;
				cnt+=right-cur-1;
			}
			ans=min(cnt,ans);
			if(!next_permutation(vi.begin(),vi.end())) break;
		}
		cout <<"Case #"<<i+1<<": "<<ans<<endl;
	}
	return 0;
}