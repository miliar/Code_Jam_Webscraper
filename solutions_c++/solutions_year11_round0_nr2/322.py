#include <iostream>
#include <map>
#include <cmath>
using namespace std;

const int N=200;

int c, d, n;
int t;
string x[N],y[N], z;
char ans[N];
bool f;
int len;
string tmp;
int main(){
	freopen("b.in", "r",stdin);	
	freopen("b.txt", "w",stdout);
	cin>>t;
	for(int L=1; L<=t; ++L){
		cin>>c;
		for(int i=0; i<c; ++i)
			cin>>x[i];//cout<<x[i]<<endl;}
		cin>>d;
		for(int i=0; i<d; ++i)
			cin>>y[i];
		cin>>n;
		cin>>z;
		len=0;
		for(int i=0; i<n; ++i)
		{
			ans[len]=z[i];
			++len;
			f=true;
			if (len!=1){
			
				for(int j=0; j<c; ++j)
				{
					if (x[j][0]==ans[len-2] && x[j][1]==z[i])
					{
						ans[len-2]=x[j][2];--len;f=false;
						break;	
					}
					if (x[j][1]==ans[len-2] && x[j][0]==z[i])
					{
						ans[len-2]=x[j][2];--len;f=false;
						break;	
					}	
				}
			}
			if (!f) continue;
			for(int j=0; j<d; ++j)
			{
				for(int k=0; k<len-1; ++k)
				//for(int k=len-2; k>=0; --k)
				{
					if (y[j][0]==ans[k] && y[j][1]==z[i])
					{
						len=0; break;	
					}	
					if (y[j][1]==ans[k] && y[j][0]==z[i])
					{
						len=0; break;	
					}	
				}
			}
				
			
		}
		
		
		cout<<"Case #"<<L<<": ";
		cout<<'[';
		for(int i=0; i<len; ++i)
		{
			if (i!=0) cout<<", ";
			cout<<ans[i];	
		}
		cout<<']'<<endl;
	}	
}
