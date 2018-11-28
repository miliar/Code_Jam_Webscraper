#include<iostream>
using namespace std;
int a[505][505];
int main(){
	int r,c,i,j,k,m,n,d,ii,jj;
	int left1,right1,up1,down1,ans,x;
	char ch;
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	cin>>r;
	for(c=1;c<=r;c++){
		cin>>n>>m>>d;
		for(i=0;i<n;i++){
			getchar();
			for(j=0;j<m;j++){
				ch=getchar();
				a[i][j]=ch-'0';
			}
		}
		ans=0;
		if(n<m)
			x=n;
		else
			x=m;
		for(k=3;k<=x;k++){
			for(i=0;i<=n-k;i++){
				for(j=0;j<=m-k;j++){
					up1=down1=left1=right1=0;
					for(ii=0;ii<k/2;ii++){
						for(jj=0;jj<k;jj++)
							up1+=a[i+ii][j+jj];
					}
					up1-=a[i][j+k-1];
					up1-=a[i][j];
					if(k%2==1)
						ii++;
					for(;ii<k;ii++){
						for(jj=0;jj<k;jj++)
							down1+=a[i+ii][j+jj];
					}
					down1-=a[i+k-1][j];
					down1-=a[i+k-1][j+k-1];
					if(up1!=down1)
						continue;
					for(jj=0;jj<k/2;jj++){
						for(ii=0;ii<k;ii++)
							left1+=a[i+ii][j+jj];
					}
					left1-=a[i][j];
					left1-=a[i+k-1][j];
					if(k%2==1)
						jj++;
					for(;jj<k;jj++){
						for(ii=0;ii<k;ii++)
							right1+=a[i+ii][j+jj];
					}
					right1=right1-a[i][j+k-1]-a[i+k-1][j+k-1];
					if(left1==right1){
						if(k>ans)
							ans=k;
					}
				}
			}
		}
		cout<<"Case #"<<c<<": ";
		if(ans>=3)
			cout<<ans<<endl;
		else
			cout<<"IMPOSSIBLE"<<endl;;
	}
}