#include <iostream>
#include <algorithm>

using namespace std;

char s[51][51];
int a[51][51];
int n,K;

int main(){
	int test;
	int i,j,x,y,p;
	int sum[3];

	freopen("A-large.in","r",stdin);
	freopen("Rotate.out","w",stdout);
	cin>>test;
	for (p=1;p<=test;p++) {
		cin>>n>>K;
		for (i=0;i<n;i++) {
			cin>>s[i];
			for (j=0;j<=n;j++) { 
				if (s[i][j]=='R') a[j][n-i-1]=1;
				else if (s[i][j]=='B') a[j][n-i-1]=2;
				else a[j][n-i-1]=0;
			}
		}

		/*
		cout<<endl;
		for (i=0;i<n;i++) {
			for (j=0;j<n;j++) cout<<a[i][j];
			cout<<endl;
		}
		*/

		//g
		for (i=0;i<n;i++) {
			y=n-1;
			for (j=n-1;j>=0;j--) {
				if (a[j][i]!=0) {
					if (y==j) {y--;continue;}
					a[y][i]=a[j][i];
					a[j][i]=0;
					y--;
				} 
			}
		}

		/*
		cout<<endl;
		for (i=0;i<n;i++) {
			for (j=0;j<n;j++) cout<<a[i][j];
			cout<<endl;
		}
		*/

		sum[1]=0;sum[2]=0;
		for (i=0;i<n;i++) {
			x=0,y=0;
			for (j=0;j<n;j++) {
				if (a[i][j]!=x) {
					sum[x]=max(sum[x],y);
					y=1;
					x=a[i][j];
				}else{
					y++;
				}
			}
			if (x>0) sum[x]=max(sum[x],y);
		}

		for (i=0;i<n;i++) {
			x=0,y=0;
			for (j=0;j<n;j++) {
				if (a[j][i]!=x) {
					sum[x]=max(sum[x],y);
					y=1;
					x=a[j][i];
				}else{
					y++;
				}
			}
			if (x>0) sum[x]=max(sum[x],y);
		}

		// \ 
		for (i=0;i<n;i++) {
			x=0,y=0;
			for (j=0;i+j<n;j++) {
				if (a[j][i+j]!=x) {
					sum[x]=max(sum[x],y);
					y=1;
					x=a[j][i+j];
				}else{
					y++;
				}
			}
			if (x>0) sum[x]=max(sum[x],y);
		}

		for (i=0;i<n;i++) {
			x=0,y=0;
			for (j=0;n-i-1-j>=0;j++) {
				if (a[n-1-j][n-i-1-j]!=x) {
					sum[x]=max(sum[x],y);
					y=1;
					x=a[n-1-j][n-i-1-j];
				}else{
					y++;
				}
			}
			if (x>0) sum[x]=max(sum[x],y);
		}

		//  /
		for (i=0;i<n;i++) {
			x=0,y=0;
			for (j=0;i-j>=0;j++) {
				if (a[j][i-j]!=x) {
					sum[x]=max(sum[x],y);
					y=1;
					x=a[j][i-j];
				}else{
					y++;
				}
			}
			if (x>0) sum[x]=max(sum[x],y);
		}
		for (i=0;i<n;i++) {
			x=0,y=0;
			for (j=0;i+j<n;j++) {
				if (a[n-1-j][i+j]!=x) {
					sum[x]=max(sum[x],y);
					y=1;
					x=a[n-1-j][i+j];
				}else{
					y++;
				}
			}
			if (x>0) sum[x]=max(sum[x],y);
		}
		
		cout<<"Case #"<<p<<": ";
		if (sum[1]>=K && sum[2]>=K) cout<<"Both"<<endl;
		else if (sum[1]>=K) cout<<"Red"<<endl;
		else if (sum[2]>=K) cout<<"Blue"<<endl;
		else cout<<"Neither"<<endl;
	};
	return 0;
}