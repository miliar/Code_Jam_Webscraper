#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<string>
#include<vector>
#include<unordered_map>
#include<iostream>
using namespace std;
int main(){
	// freopen("B-small-attempt0.in","r",stdin);
	// freopen("B-small.out","w",stdout);
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		int N;
		int S;
		int p;
		cin>>N>>S>>p;
		int* scores=new int[N];
		int m=0;
		for(int n=0;n<N;n++){
			int s;
			cin>>s;
			int q=s/3;
			if(q>=p)m++;
			else if(q==p-1 && s%3>0) m++;
			else if(S>0 && q==p-1 && s%3==0 &&q!=0){m++;S--;}
			else if(S>0 && q==p-2 && s%3==2){m++;S--;}
		}
		cout<<"Case #"<<t<<": "<<m<<endl;
	}
}
		