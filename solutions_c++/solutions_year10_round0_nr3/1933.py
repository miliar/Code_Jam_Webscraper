#include<iostream>
#include<vector>
using namespace std;
const int maxN=2000+5;
int r,k,n,a[maxN];
vector<int> q,w;
long long tot,loop,ans;
int main(){
	freopen("C-large.in","r",stdin);
	freopen("a.out","w",stdout);
	
	int T;
	scanf("%d",&T);
	for (int t=1;t<=T;++t){


	ans=0;tot=0;
	scanf("%d%d%d",&k,&r,&n);
	for (int i=0;i<n;++i) {
		scanf("%d",&a[i]);
		tot+=a[i];
	}
	if (tot<=r) ans=(long long )tot*k;
	else {
		q.clear();
		w.clear();
		q.push_back(0);
		int loop=k+1;
		tot=0;
		while (1>0){
			int x=q.back();
			int y=x;
			int now=0;
			while ((now+a[y])<=r){
				now+=a[y];
				y=(y+1)%n;
			}
			w.push_back(now);
			vector<int>::iterator it=find(q.begin(),q.end(),y);
			if (it!=q.end()){
				loop=q.end()-it;
				for (it;it!=q.end();++it) tot=tot+w[it-q.begin()];
				break;
			}
			else q.push_back(y);
		}
	//	cout<<loop<<" "<<tot<<" "<<k<<q.size()<<endl;
		while (k>q.size()){
			ans=ans+tot;
			k-=loop;
		}
		for (int i=0;i<k;++i) ans=ans+w[i];
	}
	cout<<"Case #"<<t<<": "<<ans<<endl;
	
}
	
	
	
}
