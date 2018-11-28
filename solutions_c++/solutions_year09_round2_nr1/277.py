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
struct node{
	double p;
	string name;
	node* first;
	node* second;
	int has;
	node(){
		has=0;
		name="";
	}
};
void read(node*cur){
	double p;
	char c1=' ';
	while(isspace(c1))
		scanf("%c",&c1);
	if(c1=='0')
		p=0.0;
	else
		p=1.0;
	scanf("%c",&c1);
	scanf("%c",&c1);
	double st=0.1;
	while(c1>='0' && c1<='9'){
		p+=st*(c1-'0');
		st*=0.1;
		scanf("%c",&c1);
	}
	cur->p=p;

	while(isspace(c1))
		scanf("%c",&c1);
	if(c1==')')
		return;
	cur->has=1;
	while(c1>='a' && c1<='z'){
		cur->name+=c1;
		scanf("%c",&c1);
	}
	while(c1!='(')
		scanf("%c",&c1);
	cur->first=new node();
	read(cur->first);
	c1=' ';
	while(isspace(c1))
		scanf("%c",&c1);
	cur->second=new node();
	read(cur->second);

	while(c1!=')')
		scanf("%c",&c1);
}
double rex(double p,node*cur,set<string>&a){
	p*=cur->p;
	if(cur->has){
		//set<string>::iterator it1=a.find(cur->name);
		//set<string>::iterator it2=a.end();
		//for(set<string>::iterator it=a.begin();it!=a.end();it++)
		//	if(string((*it))==cur->name)
		//for(int i=0;i<a.size();i++)
		//	if(a[i]==(cur->name))
		//		return rex(p,cur->first,a);
		if(a.find(cur->name)!=a.end())
			return rex(p,cur->first,a);
		else
			return rex(p,cur->second,a);
	}else
		return p;
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("a-large.out","w",stdout);
	int ttt;
	cin>>ttt;
	int ttti;
	for(ttti=1;ttti<=ttt;++ttti){
		int l;
		cin>>l;
		char c=' ';
		while(c!='(')
			scanf("%c",&c);
		node root;
		read(&root);
		int n;
		cin>>n;
		vector<set<string> >a(n);
		int i;
		for(i=0;i<n;i++){
			string name;
			cin>>name;
			int k;
			cin>>k;
			int i1;
			string farka;
			for(i1=0;i1<k;i1++){
				cin>>farka;
				a[i].insert(farka);
			}
		}

		cout<<"Case #"<<ttti<<": "<<endl;
		for(i=0;i<n;i++){
			double p=rex(1,&root,a[i]);
			printf("%0.7f\n",p);
		}
	}
	return 0;
}