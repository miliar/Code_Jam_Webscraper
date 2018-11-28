#include<iostream>
using namespace std;
struct node{
int g;
long long total;
int nextind;
int numgrps;
};
int main(){
	int t;
	cin>>t;
	for(int p=1;p<=t;p++){
		int R,k,N;cin>>R>>k>>N;
		node arr[N];
		int score[N];
		for(int i=0;i<N;i++){
			cin>>arr[i].g;
			arr[i].total=arr[i].g;
			arr[i].nextind=-1;
			score[i]=0;
		}
		for(int i=0;i<N;i++){
			int neind=(i+1)%N;
			long long tot=arr[i].g;
			int numgrps=1;
			while(1){
				if(tot+arr[neind].g > k)
					break;
				if(numgrps>=N)
					break;
				
				tot=tot+arr[neind].g;
				neind=(neind+1)%N;
				numgrps++;
			}
			arr[i].total=tot;
			arr[i].nextind=neind;
			
		}
		/*cout<<"**\n";
		for(int i=0;i<N;i++){
			cout<<arr[i].g<<" "<<arr[i].total<<" "<<arr[i].nextind<<"\n";
		}*/
		int start=0;
		long long cost=0;
		for(int i=0;i<R;i++){
			cost+=start[arr].total;
			start=start[arr].nextind;
			}
		cout<<"Case #"<<p<<": "<<cost<<"\n";
		
		
	}
}
