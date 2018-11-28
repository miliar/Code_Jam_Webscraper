#include<iostream>
 
#include<cmath>
#include<string>
#include<cstdio> 
#include<vector> 
#include<queue> 
#include<algorithm> 
#include<cstring>
#include<map>
#include<iostream>
#include<sstream>
using namespace std;

const int maxn=11000;
char tree[100000];
struct node {
	string name;
	double p;
	int l,r;
}T[maxn*3];
int Tnode=0,n;

bool IsLeaf( char *s){
	int i,n1,n2;
	n1=n2=0;
	for(i=0;s[i];i++){
		if( s[i]=='(' )n1++;
		if( s[i]==')' )n2++;
	}
	
	if( n1==1 && n2 == 1 ){
		for(i=0;s[i];i++)if( s[i]=='(' || s[i]==')' )s[i]=' ';
		return true;
	}
	else return false;

	
	return true;
}


void GetStr(string &lt,string &rt,string tree){

	int i,j,k;
	int pos=0;

	while( tree[pos]!= '(' )pos++;
	pos++;
	k=1;
	lt="(";
	while(k!=0){
		if( tree[pos]=='(' )k++;
		if( tree[pos]==')' )k--;
		lt+=tree[pos];
		pos++;
	}

	while( tree[pos]!= '(' )pos++;
	pos++;
	k=1;
	rt="(";
	while(k!=0){
		if( tree[pos]=='(' )k++;
		if( tree[pos]==')' )k--;
		rt+=tree[pos];
		pos++;
	}
	
}

char s[100000];
char str[100000];
int GetTree(string tree){
	int i,j,k,u;
	double p;
	
	//cout<<"tree: "<<tree<<endl;
	
	strcpy(s,tree.c_str());
	if( IsLeaf(s) ){
		stringstream line(s);
		line>>p;
	//	cout<<p<<endl;
		u=Tnode++;
		T[u].p=p;T[u].l=T[u].r=-1;
		return u;
	}

	
	s[0]=tree[1];
	for(i=2;tree[i]!='(';i++)s[i-1]=tree[i];
	s[i-1]=0;

	tree=tree.substr(i,100000);

	//for(i=0;s[i];i++)if( s[i]=='(' )s[i]=' ';
	//cout<<s<<endl;
	stringstream line(s);
	line>>p>>str;
	u=Tnode++;

	//cout<<str<<" "<<p<<endl;
	T[u].name=string(str);
	T[u].p = p;

	string lt,rt;
	GetStr(lt,rt,tree);
	T[u].l = GetTree(lt);
	T[u].r = GetTree(rt);
	//cout<<lt<<" "<<rt<<endl;

	//gets(s);
	

	return u;

}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int i,j,k,nca;
	scanf("%d",&nca);
	for(int ca=1;ca<=nca;ca++){
		scanf("%d",&n);
		getchar();
		Tnode=1;
		string name;
		char s[100];
		for(i=0;i<n;i++){
			string tmp;
			cin.getline(s,1000);
			name+=string(s);
		}

		
		int root=GetTree(name);

		map<string,int>mq;
		scanf("%d",&n);
		printf("Case #%d:\n",ca);
		
		for(i=0;i<n;i++){
			cin>>name>>k;
			mq.clear();
			while(k--){
				cin>>name;mq[name]=1;
			}
			
			int u=root;
			double p=1.0;
			while(u!=-1){
				if( T[u].l==-1 ) { p*=T[u].p; break;}
 				else {
					p*=T[u].p;
					if( mq[ T[u].name ] )u=T[u].l;
					else u=T[u].r;

				}
			}
			printf("%.7lf\n",p);
		}
	}
}

