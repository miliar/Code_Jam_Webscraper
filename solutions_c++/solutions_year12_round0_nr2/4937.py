#include<iostream>
#include<vector>
#include<string>

using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int k =1;k<=t;k++) {
		int n,p,mini;
		cin>>n>>mini>>p;
		int count = 0;
		int count2=0;
		for(int i=0 ;i<n;i++) {
			int x ;
			cin>>x;
			int s = max(p,3*p-4);
			int r = max(p,3*p-3);
			int v = max(p,3*p-2);
			
			if ( x >= (v) ) {
				count++;
			}
			else if (s <= x && x<= r) {
				if(mini>0){
					count++;
					mini--;
				}
			}
			
		}
		cout<<"Case #"<<k<<": "<<count<<endl;
		//<<count2<<endl;			
	}
}
