#include <cstdlib>
#include <iostream>
#include<cstdio>
#include<vector>

using namespace std;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	

	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		int n;
		cin>>n;
		
		vector<long long> a(n);
		vector<long long> b(n);
		for(int i=0;i<n;i++)cin>>a[i];
		for(int i=0;i<n;i++)cin>>b[i];
		
		sort(a.begin(),a.end());
		sort(b.begin(),b.end());
		reverse(b.begin(),b.end());
		
		long long ans=0;
		for(int i=0;i<n;i++)
		    ans+=a[i]*b[i];
		    
		cout<<"Case #"<< t <<": "<<ans<<endl;
	}
   // system("PAUSE");
    //return EXIT_SUCCESS;
    return 0;
}
