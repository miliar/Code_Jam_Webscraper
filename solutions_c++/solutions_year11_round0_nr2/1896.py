#include<iostream>
#include<complex>
#include<vector>
#include<cmath>
#include<algorithm>
#include<string>
#include<cstdio>
#include<memory.h>
using namespace std;
int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin>>t;
	for (int k=0; k<t; k++){
		int cc,d,n;
		char a[200],b[200],c[200],x[200],y[200];
		cin>>cc;
		for (int i=0; i<cc; i++)
			cin>>a[i]>>b[i]>>c[i];
		cin>>d;
		for (int i=0; i<d; i++)
			cin>>x[i]>>y[i];
		cin>>n;
		vector <char> ans;
		for (int i=0; i<n; i++){
			char ch;
			cin>>ch;
			//cout<<ch<<endl;
			if (ans.size()==0)
				ans.push_back(ch);
			else{
				bool p=0;
				for (int j=0; j<cc; j++)
					if ((ans[ans.size()-1]==a[j] && ch==b[j]) || (ans[ans.size()-1]==b[j] && ch==a[j])){
						ans.pop_back();
						ans.push_back(c[j]);
						p=1;
						break;
					}
				if (!p){
					for (int j=0; j<d; j++)
						for (int z=0; z<ans.size(); z++)
						if ((!p) && ((ans[z]==x[j] && ch==y[j]) || (ans[z]==y[j] && ch==x[j]))){
							ans.clear();
							p=1;
							break;
						}
				}
				if (!p)
					ans.push_back(ch);
			}
		}
		cout<<"Case #"<<k+1<<": [";
		if (ans.size()>0)
			cout<<ans[0];
		for (int i=1; i<ans.size(); i++)
			cout<<", "<<ans[i];
		cout<<"]"<<endl;
	}
    return 0;
}