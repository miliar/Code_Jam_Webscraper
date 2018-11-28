#include <iostream>
using namespace std;
struct node{
	char c;
	int x;
};
node a[50];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,n,m,i,j,o,b,ans,oo,bb,e;
	cin>>t;
	for(e=1;e<=t;e++){
		ans=0;
		o=b=1;
		oo=bb=0;
		cin>>n;
		for(i=1;i<=n;i++)
			cin>>a[i].c>>a[i].x;
		for(i=1;i<=n;i++){
			if(a[i].c=='O'){
				while(a[i].x!=o){
					oo++;
					
					if(o>a[i].x)
						o--;
					else 
						o++;
					ans++;
				}
				int xx=oo-bb;
				if(xx<0){
					ans-=oo;
					oo=0;
				}
				else {
					ans-= bb;
					oo-=bb;
				}
				oo++;
				bb=0;
				ans++;
			} 
			else if(a[i].c=='B'){
				while(a[i].x!=b){
					bb++;
						
					if(b>a[i].x)
						b--;
					else 
						b++;
					ans++;
				}
				int xx=bb-oo;
				if(xx<0){
					ans-=bb;
					bb=0;
				}
				else {
					ans-= oo;
					bb-=oo;
				}
				oo=0;
				bb++;
				ans++;
			}
		}
		cout<<"Case #"<<e<<": "<<ans<<endl;
	}
	return 0;
}
		
