#include<iostream>
#include<map>
#include<string>
using namespace std;
struct tree{
	map<string,tree> child;
};
int sum=0;
int main(){
	int T;
	cin>>T;
	for(int k=1;k<=T;++k){
		int n,m;
		tree root;
		string s;
		sum=0;
		cin>>n>>m;
		for(int i=0;i<n;++i){
			tree *temp = &root;
			cin>>s;
			s+='/';
			int start=1,end;
			while((end=s.find('/',start))!=string::npos){
				temp = &temp->child[s.substr(start,end-start)];
				start=end+1;
			}
		}
		for(int i=0;i<m;++i){
			tree *temp = &root;
			cin>>s;
			s+='/';
			int start=1,end;
			while((end=s.find('/',start))!=string::npos){
				if(temp->child.count(s.substr(start,end-start))==0)
					++sum;
				temp = &temp->child[s.substr(start,end-start)];
				start=end+1;
			}
		}
		printf("Case #%d: %d\n",k,sum);
	}
	return 0;
}
