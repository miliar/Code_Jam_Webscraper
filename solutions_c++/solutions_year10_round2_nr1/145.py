#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<string>
#include<queue>
#include<complex>
#include<numeric>
#include<bitset>

using namespace std;
typedef long long Int;
typedef vector<int> vint;
typedef vector<vint> vvint;
typedef pair<Int,Int> pint;

int c;
struct node{
	vector<string> s;
	vector<node *> next;
};
void add(vector<string> vs,node *n){
	for(int i=0;i<vs.size();i++){
		int j;
		for(j=0;j<(n->next).size();j++){
			if((n->s)[j]==vs[i]) break;
		}
		if(j==(n->next).size()){
			node *m=new node;
			(n->s).push_back(vs[i]);
			(n->next).push_back(m);
			n=m;
			c++;
		}else{
			n=(n->next)[j];
		}
	}
}

vector<string> parse(string str){
	int i;
	vector<string> ans;
	str+='/';
	string tmp;
	for(i=1;i<str.length();i++){
		if(str[i]=='/'){
			ans.push_back(tmp);
			tmp="";
		}else{
			tmp+=str[i];
		}
	}
	return ans;
}

int main(){
	int n,m,t;
	cin >> t;
	for(int l=0;l<t;l++){
		node root;
		cin >> n >> m;
		string in;
		for(int i=0;i<n;i++){
			cin >> in;
			add(parse(in),&root);
		}
		c=0;
		for(int i=0;i<m;i++){
			cin >> in;
			add(parse(in),&root);
		}
		printf("Case #%d: %d\n",l+1,c);
	}
	return 0;
}


