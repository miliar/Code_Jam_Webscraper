#include <iostream>
#include <string>
#include <list>
using namespace std;

struct TreeNode;
typedef list<TreeNode*> List;
struct TreeNode{
	string name;
	List children;
	void TreeNode::Insert(TreeNode& node){
		TreeNode* p = &node;
		children.push_back(p);
	}
};

TreeNode* not(TreeNode *a,string name){
	list<TreeNode*>::iterator it;
	for( it = a->children.begin(); it != a->children.end(); ++it )
		if((*it)->name==name) return *it;
	return NULL;
}

int main(){
	freopen("c:/A-large.in","r",stdin);
	freopen("c:/A-large.out","w",stdout);
	int t,tt,n,m,r,i;
	string str,name;
	cin>>tt;
	for(t=1;t<=tt;t++){
		r=0;
		cin>>n>>m;
		TreeNode *root=new TreeNode;
		for(i=0;i<n;i++){
			int pp=1,qq;
			cin>>str;
			TreeNode *pos=root;
			while(qq=str.find('/',pp)){
				name=str.substr(pp,qq-pp);
				pp=qq+1;
				TreeNode *qos=not(pos,name);
				if(qos==NULL){
					TreeNode *newt=new TreeNode;
					newt->name=name;
					pos->Insert(*newt);
					pos=newt;
				}
				else {
					pos=qos;
				}
			}
		}
		for(i=0;i<m;i++){
			int pp=1,qq;
			cin>>str;
			TreeNode *pos=root;
			while(qq=str.find('/',pp)){
				name=str.substr(pp,qq-pp);
				pp=qq+1;
				TreeNode *qos=not(pos,name);
				if(qos==NULL){
					r++;
					TreeNode *newt=new TreeNode;
					newt->name=name;
					pos->Insert(*newt);
					pos=newt;
				}
				else {
					pos=qos;
				}
			}
		}
		
		cout<<"Case #"<<t<<": "<<r<<endl;
	}
}
