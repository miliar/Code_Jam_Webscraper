#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<sstream>
#include<string>
#include<iterator>
#include<vector>
#include<set>
#include<map>
using namespace std;
typedef unsigned long long ull;
struct tree{
	double weight;
	struct Child{
		string feature;
		tree*left;
		tree*right;
		Child(string feature,tree*left,tree*right):feature(feature),left(left),right(right){
			if(left == 0||right==0)throw "";
		}
	};
	Child*child;
	tree(double weight,Child*child):weight(weight),child(child){}
	void print(){
		cout << "(" << weight;
		if(child){
			cout << " " << child->feature;
			child->left->print();
			child->right->print();
		}
		cout << ")";
	}
};
string parseFeature(istream&cin){
	string r;
	char c;
	while(cin.get(c)){
		if(!isalpha(c)){
			cin.putback(c);
			break;
		}
		r+=c;
	}
	return r;
}
tree*parseTree(istream&cin);
tree::Child*parseOption(istream&cin){
	char c;
	if(!(cin >> c))return 0;
	cin.putback(c);
	string feature = parseFeature(cin);
	if(feature.size()==0)return 0;
	tree*left = parseTree(cin);
	tree*right= parseTree(cin);
	return new tree::Child(feature,left,right);
}
tree*parseTree(istream&cin){
	char c;
	if(!(cin >> c))return 0;
	if(c != '('){
		cin.putback(c);
		return 0;
	}
	double w;
	cin >> w;
	tree::Child*child = parseOption(cin);
	if(!(cin >> c))throw "";
	if(c != ')')throw ")";
	return new tree(w,child);
}
tree*parse(istream&cin){
	return parseTree(cin);
}
double solve(tree*t,set<string>features){
	if(t->child == 0)return t->weight;
	if(features.count(t->child->feature)){
		return t->weight * solve(t->child->left,features);
	}else{
		return t->weight * solve(t->child->right,features);
	}
}
int main(){
	cout.sync_with_stdio(true);
	int k;
	string line;
	getline(cin,line);
	stringstream(line) >> k;
	for(int i=1;i<=k;++i){
		int n;
		{
			getline(cin,line);
			stringstream (line) >> n;
		}
		string s;
		for(int j=0;j<n;++j)getline(cin,line),s += line;
		tree*t=0;
		{	stringstream code(s);
			t = parse(code);
		}
		{
			getline(cin,line);
			stringstream ss(line);
			ss >> n;
		}
		cout << "Case #"<<i<<": " << endl;
		for(int j=0;j<n;++j){
			getline(cin,line);
			stringstream ss(line);
			string animal;
			int m;
			ss >> animal >> m;
			set<string>features;
			copy(istream_iterator<string>(ss),istream_iterator<string>(),std::inserter(features,features.end()));
			printf("%.20f\n",solve(t,features));
		}
	}
	cout << flush;
}

