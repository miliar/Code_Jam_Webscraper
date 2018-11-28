#include<iostream>
#define fr(i,a,b) for(i=a;i<=b;++i)
using namespace std;
const int maxn=1002;
int x[maxn][maxn],i,j,k,ans,ca,ti,n,p;
bool ok(int a,int b){
	int i,j,i2,j2;
	fr(i,1,n)
		fr(j,1,n)
			if(x[i][j]!=-1){
				i2=a-i+a;
				j2=j;
				if(i2>=1&&i2<=n&&j2>=1&&j2<=n&&x[i2][j2]!=-1&&x[i2][j2]!=x[i][j])
					return false;
				i2=i;
				j2=b-j+b;
				if(i2>=1&&i2<=n&&j2>=1&&j2<=n&&x[i2][j2]!=-1&&x[i2][j2]!=x[i][j])
					return false;
			}
	return true;
}
int main(){
	freopen("a1.in","r",stdin);
	freopen("a1.out","w",stdout);
	cin>>ca;
	fr(ti,1,ca){
		cin>>k;
		n=k+k-1;
		memset(x,255,sizeof(x));
		fr(i,1,k){
			p=k-i;
			fr(j,1,i){
				++p;
				cin>>x[i][p++];
			}
		}
		fr(i,k+1,n){
			p=i-k;
			fr(j,1,n-i+1){
				++p;
				cin>>x[i][p++];
			}
		}
		/*fr(i,1,n){
			if(ti!=39)
				break;
			fr(j,1,n)
				if(x[i][j]==-1)
					cout<<" ";
				else
					cout<<x[i][j];
			cout<<endl;
		}*/
		ans=n+n;
		fr(i,1,n)
			fr(j,1,n)
				if(ok(i,j)){
					int w=abs(i-k)+abs(j-k)+k;
					if(w<ans)
						ans=w;
					
				}
		cout<<"Case #"<<ti<<": "<<ans*ans-k*k<<endl;
	}
}