#include<iostream>

using namespace std;

int main(){
	int N;
	cin>>N;
	for(int t=1; t<=N; t++){
		long long n, A, B, C, D, x0, y0, M;
		long long a[128][2];
		cin>>n>>A>>B>>C>>D>>x0>>y0>>M;
		for(int x=x0, y=y0, i=0; i<n; i++){
			a[i][0]=x; a[i][1]=y;
			x=(A*x+B)%M;
			y=(C*y+D)%M;
		}
		int ans=0;
		for(int i=0; i<n; i++) for(int j=i+1; j<n; j++) for(int k=j+1; k<n; k++)
			if((a[i][0]+a[j][0]+a[k][0])%3==0&&(a[i][1]+a[j][1]+a[k][1])%3==0)
				ans++;
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
	return 0;
}

