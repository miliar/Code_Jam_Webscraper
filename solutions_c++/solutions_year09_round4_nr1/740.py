#include<iostream>
#include<vector>
#include<string>
#include <iomanip>
#include<sstream>
#include<set>

#define mmax 10000
using namespace std;
vector<int> nums;
int N;

int main(){
	int T;
	cin>>T;
	for(int ii=0; ii<T; ii++){
		cin>>N;
		string tmp; 
		nums.clear(); nums.resize(0) ;
		int res=0;
		getline(cin, tmp); 
		for(int i=0; i<N; i++){
			getline(cin, tmp);
			int c=0;
			for(int j=0; j<N; j++){
				if(tmp[j]=='1')c=j;
			}
			nums.push_back(c);
		}      // cout<<1;
		for(int num=0; num<N; num++){
			//first num <=num starting with num index
			for(int j=num; j<N; j++){
				if(nums[j]<=num){
					for(int k=j; k>=num+1; k--){
						swap(nums[k], nums[k-1]);
						res++;
					}
					break;
				}
			}
		}
		cout<<"Case #"<<ii+1<<": "<<res<<"\n";
		
	}
	
}
