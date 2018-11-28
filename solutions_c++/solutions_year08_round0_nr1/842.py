#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
using namespace std;
int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int n;
	cin>>n;
	int ii;
	for(ii=1;ii<=n;ii++){
		int s;
		cin>>s;
		vector<string>engines(s);
		char a[200];
		int i;
		gets(a);
		for(i=0;i<s;i++){
			gets(a);
			engines[i]=a;
			//cout<<engines[i]<<"!!!!!!!!!!!!!!!!!!"<<endl;
		}
		int q;
		cin>>q;
		gets(a);
		vector<string>quer(q);
		for(i=0;i<q;i++){

			gets(a);
			quer[i]=a;
			//cout<<quer[i]<<"$$$$$$$$$$$$$$$$$$$$$"<<endl;
		}

		vector<pair<int,int> >b(0);

		for(i=0;i<q;i++){
			int i1;
			for(i1=0;i1<s;i1++)
				if(quer[i]==engines[i1])
					b.push_back(make_pair(i1,i));
		}

		vector<int>work(s);
		for(i=0;i<s;i++){
			work[i]=10000;
			int i1;
			for(i1=0;i1<b.size();i1++)
				if(b[i1].first==i){
					work[i]=i1;
					break;
				}
		}

		int pot=-1;
		int max=-1;
		int rez=0;
		for(i=0;i<s;i++)
			if(work[i]>max){
				max=work[i];
				pot=i;
			}

		int curind=0;
		for(i=0;i<q;i++){
			if(b[curind].second==i){
				//work update
				int i1;
				work[b[curind].first]=1000;
				for(i1=curind+1;i1<b.size();i1++)
					if(b[i1].first==b[curind].first){
						work[b[curind].first]=b[i1].second;
						break;
					}
				curind++;
			}

			if(quer[i]==engines[pot]){
				rez++;
				max=-1;
				int nom=-1;
				int i1;
				for(i1=0;i1<s;i1++)
					if(i1!=pot && work[i1]>max){
						max=work[i1];
						nom=i1;
					}
				pot=nom;
			}
		}
		cout<<"Case #"<<ii<<": "<<rez<<endl;
	}
/*	cout<<1<<endl;
	cout<<100<<endl;
	vector<string>a(100);
	for(int i=0;i<100;i++){
		cout<<'A'<<i<<endl;
		if(i<10){
			a[i].resize(2);
			a[i][0]='A';
			a[i][1]=i+'0';
		}else{
			a[i].resize(3);
			a[i][0]='A';
			a[i][1]=(i/10)+'0';
			a[i][2]=(i%10)+'0';
		}
	}
	cout<<1000<<endl;
	for(i=0;i<1000;i++){
		cout<<a[i%100]<<endl;
	}*/
	return 0;
}