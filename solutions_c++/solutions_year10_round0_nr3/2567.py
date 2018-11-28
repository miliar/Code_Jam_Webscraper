#include<iostream>
using namespace std;
int nn,ii,ans,now,j,k,p,r,n;
int a[10000];
int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>nn;
	for(int ii=0;ii<nn;ii++){
		cin>>r>>k>>n;
		for (int i=0;i<n;i++)
			cin>>a[i];
		ans =0;
		p = 0;
		for(int i=0;i<r;i++){
			now =0; j=0;
			while(j<n && now+a[p]<=k){
				now+=a[p];
				j++;
				p++;
				if(p==n)p=0;
			}
			//cout<<now<<" ";
			ans +=now;
		}
		cout<<"Case #"<<ii+1<<": "<<ans<<endl;
	}
	fclose(stdin);
	fclose(stdout);
}
			
		
