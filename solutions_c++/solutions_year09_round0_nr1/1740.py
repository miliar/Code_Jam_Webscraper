#include <stdio.h>
#include <cstring>
#include <vector>
#include <iostream>
#include <string>
#define Eo(x) {cerr << #x << " = " << x << endl;}
using namespace std;
class node{
	public: 
		int cnt;
		node(){ memset(next,0,sizeof(next)); cnt = 0;}
		node* next[29];
};
node *root;
vector <string> parse(string line){
	vector <string> ans0;
	while (line != ""){
		if (line[0] == '('){
			int pos = 0;
			while (line[pos] != ')') pos++;
			ans0.push_back(line.substr(1,pos-1));
			line = line.substr(pos + 1);
			
		}else{
			ans0.push_back(line.substr(0,1));
			line = line.substr(1);
		}
	}
	return ans0;
}

vector <string> var;
void add(string q){
	node * r = root;
	for ( int i = 0; i < q.size(); i++){
		if (r->next[q[i] - 'a'] == NULL) 
			r->next[q[i] - 'a'] = new node;
		r = r->next[q[i] - 'a'];
	}
	r->cnt++;
}

int ans(int i, node *r ){
	if (!r) return 0;
	if (i == var.size()){
		return r->cnt;
	}
	else{
		int _ans = 0;
		string &w = var[i];
		for ( int t = 0; t < w.size(); t++){
			_ans += ans(i + 1, r->next[w[t] - 'a']);
		}
		return _ans;
	}

}
int main(){
	string buff;
	int l,n,d;
	root = new node;
	freopen("input.txt", "r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d%d%d",&l,&d,&n);
	for ( int i = 0 ; i < d; i++){
		cin >> buff;
		add(buff);
	}
	for ( int i = 0 ; i < n; i++){
		cin >> buff;
		var = parse(buff);
/*		for ( int j = 0; j < var.size(); j++)
			cerr << var[j] << endl;*/
		cout << "Case #" << i + 1 << ": " << ans(0, root) <<endl; 
	}
}
