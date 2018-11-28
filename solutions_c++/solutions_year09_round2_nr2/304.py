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
	freopen("B-large.in","r",stdin);
	//freopen("b-large.out","w",stdout);
	int ttt;
	cin>>ttt;
	int ttti;
	for(ttti=1;ttti<=ttt;++ttti){
		string s;
		cin>>s;
		string g=s;
		next_permutation(g.begin(),g.end());
		cout<<"Case #"<<ttti<<": ";
		cout<<s<<' ';
		if(g<s){
			int i=0;
			int kil=0;
			while(g[i]=='0'){
				i++;
				kil++;
			}
			kil++;
			cout<<g[i];
			i++;
			while(kil){
				cout<<0;
				kil--;
			}
			for(;i<g.size();i++)
				cout<<g[i];
			cout<<endl;
		}else{
			if(s==g){
				cout<<g[0]<<0;
				for(int i=1;i<g.size();i++)
					cout<<g[i];
				cout<<endl;
			}else
				cout<<g<<endl;
		}

		
	}
	return 0;
}