#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
using namespace std;
int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int n,ii;
	cin>>n;
	for(ii=1;ii<=n;ii++){
		int t;
		cin>>t;
		int na,nb;
		cin>>na>>nb;
		int i;
		vector<int>a(1600,0);
		vector<int>b(1600,0);
		vector<int>akey(na);
		vector<int>bkey(nb);

		for(i=0;i<na;i++){
			string s;
			cin>>s;
			int q=(s[0]-'0')*600 + (s[1]-'0')*60 + (s[3]-'0')*10 + s[4]-'0';
			akey[i]=q;
			a[q]--;
			cin>>s;
			q=(s[0]-'0')*600 + (s[1]-'0')*60 + (s[3]-'0')*10 + s[4]-'0';
			b[q+t]++;
		}

		for(i=0;i<nb;i++){
			string s;
			cin>>s;
			int q=(s[0]-'0')*600 + (s[1]-'0')*60 + (s[3]-'0')*10 + s[4]-'0';
			bkey[i]=q;
			b[q]--;
			cin>>s;
			q=(s[0]-'0')*600 + (s[1]-'0')*60 + (s[3]-'0')*10 + s[4]-'0';
			a[q+t]++;
		}
		for(i=1;i<1600;i++){
			a[i]=a[i-1]+a[i];
			b[i]=b[i-1]+b[i];
		}
		
		
		int mina=1000;
		int minb=1000;
		if(na==0)
			mina=0;
		if(nb==0)
			minb=0;
		for(i=0;i<na;i++)
			if(a[akey[i]]<mina)
				mina=a[akey[i]];
		for(i=0;i<nb;i++)
			if(b[bkey[i]]<minb)
				minb=b[bkey[i]];
		mina*=-1;
		minb*=-1;
		if(mina<0)
			mina=0;
		if(minb<0)
			minb=0;
		cout<<"Case #"<<ii<<": "<<mina<<' '<<minb<<endl;
	}
	return 0;
}