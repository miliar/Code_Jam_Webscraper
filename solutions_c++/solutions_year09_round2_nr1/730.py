#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;
 
typedef long long LL;
#define PB push_back
#define all(v) (v).begin(),(v).end()
#define vi vector<int>
#define vvi vector<vi>
#define vs vector<string>
#define pii pair<int,int>
#define INF 200000000
LL gcd(LL m,LL n){LL tmp;while(n!=0){tmp=m%n;m=n;n=tmp;}return m;}   
LL lcm(LL m,LL n){return (m*n)/gcd(m,n);}
string i2s(LL n){stringstream ss;ss<<n;return ss.str();}
LL s2i(string s){stringstream ss;ss<<s;LL n;ss>>n;return n;}

struct tree{
	string node;
	double weight;
	tree* left;
	tree* right;
};

tree* T;

tree* newnode(){
	tree* t=new tree;
	t->node="";
	t->weight=0;
	t->left=NULL;
	t->right=NULL;
	return t;
}

int pos;
int go(tree* T,vs& a,string fname,int lvl){
	while(pos<a.size() && a[pos]==")") pos++;
	if(pos==a.size()) return a.size();
	
	string str=a[pos];
	
	//cout<<str<<endl<<" "<<lvl<<endl;
	
	if(str=="("){
		pos++;
		str=a[pos];
		//cout<<"Creating new node for feature="<<fname<<" with wt="<<a[pos]<<endl;
		stringstream ss;
		ss<<str; 
		ss>>T->weight;
		T->node=fname;
		T->left=NULL;
		T->right=NULL;
		//cout<<T->weight<<endl;
		pos++;
		//cout<<a[pos]<<endl;
		if(a[pos][0]>='a' && a[pos][0]<='z'){ //subtree exist
			fname=a[pos];
			pos++;
			//cout<<"Creating left subtree"<<endl;
			T->left=newnode();
			go(T->left,a,fname,lvl+1);
			
			pos++;
			//cout<<"Creating right subtree"<<endl;
			T->right=newnode();
			go(T->right,a,fname+"-",lvl+1);
		}
	}
}

string format(string s){
	string ret="";
	for(int i=0;i<s.size();i++)
		if(s[i]=='(' || s[i]==')'){
			ret+=" ";
			ret+=s[i];
			ret+=" ";
		}	
		else 
			ret+=s[i];
	return ret;	
}
double res;
void solve(tree* T,set<string>& f){
	//cout<<T->node<<" "<<T->weight<<endl;
	if(T->left==NULL) return;
	//cout<<"hello"<<endl;
	if(f.find(T->left->node)!=f.end()){
		//cout<<T->left->node<<" "<<T->left->weight<<endl;
		res*=T->left->weight;
		solve(T->left,f);
	}
	else{
		res*=T->right->weight;
		solve(T->right,f);
	}	
} 
void test1(tree* T){
	if(T==NULL) return;
	cout<<T->node<<" "<<T->weight<<endl;
	test1(T->left);
	test1(T->right);
}
int main()
{
	int test,L,A;
	cin>>test;
	for(int t=1;t<=test;t++){
		cin>>L;
		
		T=new tree;
		string s;
		getline(cin,s);
		vs a;
		for(int i=0;i<L;i++){
			getline(cin,s);
			s=format(s);
			stringstream ss;
			ss<<s;
			while(ss>>s)
				a.PB(s);
		}
		
		pos=0;
		go(T,a,"root",0);
		
		printf("Case #%d:\n",t);
		cin>>A;
		string animal;
		int k;
		for(int i=0;i<A;i++){
			cin>>animal;
			cin>>k;
			set<string> f;
			for(int j=0;j<k;j++){
				cin>>s;
				f.insert(s);
			}	
			res=1;
			solve(T,f);
			//test1(T);
			cout<<res*(T->weight)<<endl;
		}		
	}
}