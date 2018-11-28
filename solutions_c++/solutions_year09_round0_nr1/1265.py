#include<iostream>
#include<cstdio>
#include<string>
#include<set>
#include<vector>
#include<algorithm>
using namespace std;
set<string>dic;
int count1;
struct item{
	item(){
		links.resize(30);
		isnulls.resize(30);
		fill(isnulls.begin(),isnulls.end(),1);
	//	val="";
	}
//	string val;
	vector<item*>links;
	vector<int>isnulls;
};

item root;

void rex2(string&s,int cur,item*curitem){
	if(cur==s.size()){
		count1++;
		return;
	}		

	char c=s[cur];
	if(c=='('){
		int end=cur+1;
		while(s[end]!=')'){
			end++;
		}
		int i=cur+1;
		while(s[i]!=')'){
			if(!curitem->isnulls[s[i]-'a'])
				rex2(s,end+1,curitem->links[s[i]-'a']);
			i++;
		}
		return;
	}
	if(!curitem->isnulls[s[cur]-'a'])
		rex2(s,cur+1,curitem->links[s[cur]-'a']);
}


int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-small.out","w",stdout);
	int l,d,n;
	cin>>l>>d>>n;
	
	int i;
	string s;

	for(i=0;i<d;i++){
		cin>>s;
		int i1;
		item *cur= &root;
		for(i1=0;i1<l;i1++){
			if(cur->isnulls[s[i1]-'a']){
				cur->isnulls[s[i1]-'a']=0;
				cur->links[s[i1]-'a']=new item();
				//cur->links[s[i1]-'a']->val=cur->val+s[i1];
				cur=cur->links[s[i1]-'a'];
			}else
				cur=cur->links[s[i1]-'a'];
		}
	}

	for(i=0;i<n;i++){
		count1 =0;
		cin>>s;
	
		cout<<"Case #"<<i+1<<": ";
		rex2(s,0,&root);
		cout<<count1<<endl;
	}

	/*int l,n,d;
	cout<<15<<' '<<5000<<' '<<500<<endl;
	string s="abcdefghijaasdf";
	for(d=0;d<5000;++d){
		cout<<s<<endl;
		next_permutation(s.begin(),s.end());	
	}
	for(n=0;n<500;n++){
		int i;
		for(i=0;i<15;i++)
			cout<<'('<<"abcdefghijklmnopqrstuvwxyz"<<')'<<endl;
	}*/
	return 0;
}