#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<cmath>
#include<algorithm>
#include<list>
using namespace std;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int ttt;
	cin>>ttt;
	int ttti;
	for(ttti=1;ttti<=ttt;++ttti){
		int n;
		cin>>n;
		vector<string>a(n);
		int i,i1;
		for(i=0;i<n;i++)
				cin>>a[i];

		vector<int>b(n,-1);
		for(i=0;i<n;i++){
			int last=0;
			for(i1=0;i1<n;i1++)
				if(a[i][i1]-'0')
					last=i1;
			b[i]=last;
		}

		int rez=0;
		while(1){
			int yes=1;
			int nk=-1;
			for(i=0;i<n;i++){
				if(b[i]>i){
					nk=i;
					break;
				}
			}
			if(nk==-1)
				break;

			int nma=-1;
			for(i=nk;i<n;i++){
				if(b[i]<=nk){
					nma=i;
					break;
				}
			}

			while(nma>nk){
				swap(b[nma],b[nma-1]);
				nma--;
				rez++;
				yes=0;
			}

			if(yes)
				break;
		}
		cout<<"Case #"<<ttti<<": "<<rez<<endl;
	}
	return 0;
}