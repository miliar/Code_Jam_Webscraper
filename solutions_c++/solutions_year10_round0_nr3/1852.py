#include <iostream>

using namespace std;

long a[1005];
long long s[1005];
long next[1005];
int main(){
	int t;
	cin >> t;
	for(int f=1;f<=t;f++){
		int r,k,n;
		scanf("%d%d%d",&r,&k,&n);
		for(int i=0;i<n;i++)
			scanf("%d",&a[i]);
		for(int i=0;i<n;i++){
			s[i] = a[i];
			int j =i+1;
			if(j==n) j=0;
			for(;s[i]+a[j]<=k && j!=i;j++,j=(j==n)?0:j)
				s[i]+=a[j];
			next[i] = j;
		}
		int st=0;
		long long sum=0;
		for(int i=0;i<r;i++){
			sum+=s[st];
			st=next[st];
		}
		cout<<"Case #"<<f<<": "<<sum<<endl;
	}
	return 0;
}
