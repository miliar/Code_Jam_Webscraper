#include<iostream>
#include<sstream>
#include<string>
#include<map>
using namespace std;
struct node{
	map<string,node*> next;
};
int main(){
	int t,n,m,ans;
	node *root,*now;
	string st,line;
	cin>>t;
	for(int tt=1;tt<=t;++tt){
		root=new node;
		cin>>n>>m;
		getchar();
		while(n--){
			getline(cin,line,'\n');
			istringstream iss(line);
			now=root;
			getline(iss,st,'/');
			while(getline(iss,st,'/')){
				if(now->next.find(st)!=now->next.end()){
					now=now->next.find(st)->second;
				}
				else{
					now->next[st]=new node;
					now=now->next[st];
				}
			}
		}
		ans=0;
		while(m--){
			getline(cin,line,'\n');
			istringstream iss(line);
			now=root;
			getline(iss,st,'/');
			while(getline(iss,st,'/')){
				if(now->next.find(st)!=now->next.end()){
					now=now->next.find(st)->second;
				}
				else{
					now->next[st]=new node;
					now=now->next[st];
					++ans;
				}
			}
		}
		printf("Case #%d: %d\n",tt,ans);
	}
	
}
