#include<iostream>
#include<cmath>
#include<algorithm>
using namespace std;
int aa[10],n,p;
bool f[101];
int main()
{
    freopen("C-small-attempt0.in","r",stdin);//
	freopen("1.txt","w",stdout);
	int t,i,j;cin>>t;for(int cas=1;cas<=t;cas++){
	    cin>>n>>p;
		for(i=0;i<p;i++)cin>>aa[i];
		int minn=0x7fffffff;
		do{
			 memset(f,0,sizeof(f));
			 int sum=0;
			 for(i=0;i<p;i++)
			 {
			     f[aa[i]]=1;
				 for(int k=aa[i]-1;k>=1&&f[k]==0;k--)sum++;
				 for(int k=aa[i]+1;k<=n&&f[k]==0;k++)sum++;		
			 }
			 minn=min(minn,sum);
		}while(next_permutation(aa,aa+p));
		cout<<"Case #"<<cas<<": "<<minn<<endl;	
	}
}
