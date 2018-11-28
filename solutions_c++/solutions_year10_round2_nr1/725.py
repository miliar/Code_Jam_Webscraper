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
#include <queue>

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

struct node {
	string dir;
	int c;
	node* child[101];
	node(){dir="";c=0;}
	node(string& s){dir=s;c=0;}
};
void insert(node* &T,vs& v,int pos){
	if(pos==v.size()) return;
	bool ok=0;
	int c=T->c;
	for(int i=0;i<c;i++){
		if(T->child[i]->dir == v[pos]){
			insert(T->child[i],v,pos+1);
			ok=1;
		}
	}
	if(!ok){
		T->child[c] = new node(v[pos]);
		insert(T->child[c],v,pos+1);
		T->c++;
	}
}
int count(node* &T,vs& v,int pos){
	if(pos==v.size()) return 0;
	bool ok=0;
	int ret=0;
	int c=T->c;
	for(int i=0;i<c;i++){
		if(T->child[i]->dir == v[pos]){
			ret+=count(T->child[i],v,pos+1);
			ok=1;
		}
	}
	if(!ok){
		T->child[c] = new node(v[pos]);
		//cout<<"Created: "<<v[pos]<<endl;
		ret+=1+count(T->child[c],v,pos+1);
		T->c++;
	}
	return ret;
}
int main(){
	int T,N,M;
	cin>>T;
	for(int kase=1;kase<=T;kase++){
		node* T = new node();
		T->dir="root";
		cin>>N>>M;
		string path,s;
		for(int i=0;i<N;i++){
			cin>>path;
			for(int i=0;i<path.size();i++) if(path[i]=='/') path[i]=' ';
			stringstream ss;
			ss<<path;
			vs v;
			while(ss>>s){
				v.PB(s);
			}
			insert(T,v,0);
		}
		int res=0;
		for(int i=0;i<M;i++){
			cin>>path;
			for(int i=0;i<path.size();i++) if(path[i]=='/') path[i]=' ';
			stringstream ss;
			ss<<path;
			vs v;
			while(ss>>s){
				v.PB(s);
			}
			res+=count(T,v,0);
		}
		printf("Case #%d: %d\n",kase,res);
	}
}