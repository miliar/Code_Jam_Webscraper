#include<iostream>
#include<set>
#include<string>
using namespace std;
int main(){
	int t,n,s,q,i,c;
	bool f;
	string ss,p;
	cin>>n;
	for(t=1;t<=n;t++){
		cin>>s;
		getline(cin,ss);
		for(i=1;i<=s;i++){
			getline(cin,ss);
		}
		cin>>q;
		if(q==0){
			printf("Case #%d: 0\n",t);
			continue;
		}
		c=0;
		getline(cin,ss);
		set<string> st;
		while(q){
			q--;
			getline(cin,ss);
			st.insert(ss);
			if(st.size()==s){
				c=1;
				p=ss;
				break;
			}
		}
		f=1;
		st.clear();
		while(q--){
			getline(cin,ss);
			st.insert(ss);
			if(ss==p)	f=0;
			if(f){
				if(st.size()==s-1){
					c++;
					p=ss;
					f=1;
					st.clear();
				}
			}
			else{
				if(st.size()==s){
					c++;
					p=ss;
					f=1;
					st.clear();
				}
			}
		}
		printf("Case #%d: %d\n",t,c);
	}
	return 0;
}

