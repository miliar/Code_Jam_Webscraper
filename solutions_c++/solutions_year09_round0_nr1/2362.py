#include<iostream>
#include<string>
#include<vector>
using namespace std;
main(){
	int a,b,c,i,j,z,k;
	cin>>a>>b>>c;
	string s,s1;
	vector<string> v;
	for(i=0;i<b;i++){
		cin>>s;
		v.push_back(s);
	}
	int y;
	for(y=0;y<c;y++){
		cin>>s1;
		vector<int> open,close;
		string res;
		bool write = true;
		for(i=0;i<s1.size();i++){
			if(write==true)
				res+=s1[i];
			if(s1[i]=='('){
				open.push_back(i);
				write=false;
			}
			if(s1[i]==')'){
				close.push_back(i);
				write=true;
			}
		}
		int ans = 0;
		for(z=0;z<b;z++){
			s=v[z];
			int k=0;
			bool found=true;
			if(res.size()==s.size()){
				for(i=0;i<res.size();i++){
					if(res[i]=='('){
						int count=0;
						for(j=open[k]+1;j<close[k];j++)
							if(s[i]!=s1[j])
								count++;
						if(count==close[k]-open[k]-1){
							found=false;
							break;
						}
						k++;
					}
					else if(res[i]!=s[i]){
						found=false;
						break;
					}
				}
			}
			if(found==true)
				ans++;
		}
		cout<<"Case #"<<y+1<<": "<<ans<<endl;
	}
}
