#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
#include <map>
using namespace std;

map<string, bool> m;

class tree{
	
	public:
	
	double val;
	string feature;
	tree* left;
	tree* right;
	
	tree(){
		feature = "";
		left = NULL;
		right = NULL;
	}
	
	double solve(){
		double ans = val;
		
		if(m.find(feature)==m.end()){
			if(left==NULL){
				return ans;
			}
			else{
				ans *= left->solve();
				return ans;
			}
		}
		else{
			if(right==NULL){
				return ans;
			}
			else{
				ans *= right->solve();
				return ans;
			}
		}
	}
	
	void print(){
		cout<<"( "<<val<<" "<<feature<<" "<<endl;
		if(right!=NULL)
		right->print();
		if(left!=NULL)
		left->print();
		cout<<")"<<endl;
	}
	
};



tree* parse(){
	
	tree* ptr = new tree();
	
	char c;
	cin>>c;
	
	double d;
	
	cin>>d;
	
	//cout<<d<<endl;
	
	ptr->val = d;
	
	//cin>>c;
	
	string s;
	cin>>s;
	
	if(s==")"){
		return ptr;
	}
	else{
		//string s;
		//cin>>s;
		
		ptr->feature = s;
		
		tree* ptr1 = parse();
		tree* ptr2 = parse();
		
		ptr->right = ptr1;
		ptr->left = ptr2;
		
		cin>>c;
		
		return ptr;
	}
}
	

int main(){
	
	int n;
	
	cin>>n;
	
	for(int i=0; i<n; i++){
		int l;
		cin>>l;
		
		tree* maint = parse();
		
		//maint->print();
		//cout<<endl;
		int a;
		
		cin>>a;
		
		cout<<"Case #"<<i+1<<":"<<endl;
		
		for(int j=0; j<a; j++){
			string s;
			cin>>s;
			
			int no;
			
			cin>>no;
			
			m.clear();
			
			for(int k=0; k<no; k++){
				cin>>s;
				
				m[s] = true;
			}
			
			printf("%.7f\n",maint->solve());
		}
		
		 
	}
	
	return 0;
}
	
	
