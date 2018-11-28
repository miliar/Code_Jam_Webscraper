#include<cstdio>
#include<iostream>
using namespace std;
const int N=10000+100;
int n,D;
int d[N],l[N],f[N];
int Min(int a, int b){return a<b?a:b;}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int Test;
	cin>>Test;
	for (int test=1;test<=Test;test++){
		cin>>n;
		for (int i=0;i<n;i++){
			cin>>d[i]>>l[i];
			f[i]=0;
		}
		cin>>D;
		f[0]=d[0];
		int flag=false;
		for (int i=0;i<n;i++){
			int j=i+1;
			while (j<n && f[i]>=d[j]-d[i]){
				if (Min(d[j]-d[i],l[j])>f[j])
					f[j]=Min(d[j]-d[i],l[j]);
				j++;
			}
			if (f[i]>=D-d[i])
				flag=true;
		}
		cout<<"Case #"<<test<<": ";
		if (flag)
			cout<<"YES";
		else
			cout<<"NO";
		cout<<endl;
	}
	return 0;
}
