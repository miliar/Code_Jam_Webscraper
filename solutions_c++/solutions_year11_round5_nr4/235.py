#include<iostream>
#include<vector>
#include<cstdio>
using namespace std;

struct node
{
	int data;
	int index;
	vector<node*> child;
	node(int d, int i, vector<node*> c){
		data = d;
		index = i;
		child = c;
	}
	node(int d, int i){
		data = d;
		index = i;
	}
	void print(){
		printf("%d %d, ", data, index);
		for(int i = 0; i < child.size(); i++)printf("%d ", child[i]->data);
		printf("\n");
		for(int i = 0; i < child.size(); i ++)child[i]->print();

	}
};

node* mergenode(node* a, node * b){
	node* newnode;
	vector<node*> newchild;
	if(a->data < b->data){
		newchild = a->child;
		newchild.push_back(b);
		newnode = new node(a->data, a->index +1, newchild);
	}
	else {
		newchild = b->child;
		newchild.push_back(a);
		newnode = new node(b->data, b->index +1, newchild);
	}
	return newnode;
}

vector<node*> merge(vector<node*> a, vector<node*> b)
{
	int i = 0, j = 0;
	vector<node*> ans;
	while(i < a.size() && j < b.size()){
		node *newnode;
		if(a[i]->index == b[j]->index){
			vector<node*> newchild;
			if(a[i]->data < b[j]->data){
				newchild = a[i]->child;
				newchild.push_back(b[j]);
				newnode = new node(a[i]->data, a[i]->index +1, newchild);
			}
			else {
				newchild = b[j]->child;
				newchild.push_back(a[i]);
				newnode = new node(b[j]->data, b[j]->index +1, newchild);
			}
			i++;
			j++;
			ans.push_back(newnode);
		}
		else if(a[i]->index < b[j]->index){

			if(ans.size() >0 && ans[ans.size()-1]->index == a[i]->index){
				ans[ans.size()-1] = mergenode(a[i], ans[ans.size()-1]);

			}
			else ans.push_back(a[i]);
			i++;

		}
		else {

			if(ans.size() > 0 && ans[ans.size()-1]->index == b[j]->index){
				ans[ans.size()-1] = mergenode(b[j], ans[ans.size()-1]);
			}
			else {

				ans.push_back(b[j]);
			}
			j++;
		}

	}
	while(i < a.size()){
		if(ans.size() > 0 && ans[ans.size()-1]->index == a[i]->index){
			ans[ans.size()-1] = mergenode(a[i], ans[ans.size()-1]);
		}
		else ans.push_back(a[i]);
		i++;
	}
	while(j < b.size()){
		if(ans.size() > 0 && ans[ans.size()-1]->index == b[j]->index){
			ans[ans.size()-1] = mergenode(b[j], ans[ans.size()-1]);
		}
		else ans.push_back(b[j]);
		j++;
	}
	return ans;
}

vector<node*> add(vector<node*> a, int d)
{
	node *newnode = new node(d, 0);
	vector<node*> l;
	l.push_back(newnode);
	return merge(a, l);
}

vector<node*> delmin(vector<node*> a)
{
	int min = 0x7fffffff;
	int minpos = -1;
	for(int i = 0; i < a.size(); i++){
		if(a[i]->data < min){
			min = a[i]->data;
			minpos = i;
		}
	}
	if(minpos != -1){
		node *l = a[minpos];
		a.erase(a.begin() + minpos);
		return merge(a, l->child);
	}
	else return a;
}

int findmin(vector<node*> a)
{
	int min = 0x7fffffff;
	for(int i = 0; i < a.size(); i++){
		if(a[i]->data < min)min = a[i]->data;
	}
	return min;
}
vector<node*> dui[500000];
int main()
{
	int n, m;
	scanf("%d%d", &n, &m);
	for(int i = 0; i < n; i++){
		int x;
		scanf("%d", &x);
		dui[i].push_back(new node(x, 0));
	}
//	printf("finish initial\n");
	for(int i = 0; i < m; i++){
//		printf("%d===========\n", i);
		int op;
		scanf("%d", &op);
		if(op == 0){
			int a,b;
			scanf("%d%d", &a, &b);
			dui[a] = merge(dui[a], dui[b]);
		}
		if(op == 1){
			int a,b;
			scanf("%d", &a);
			if(dui[a].size()>0){
				printf("%d\n",findmin(dui[a]));
				dui[a] = delmin(dui[a]);
//				printf("size %d\n",dui[a].size());
			}
			else printf("-1\n");
		}
		if(op == 2){
			int a,b;
			scanf("%d%d", &a, &b);
			vector<node*> newtree;
			newtree.push_back(new node(b,0));
			dui[a] = merge(dui[a], newtree);
		}
	}
/*	for(int i = 9998; i >=0; i--){
		dui[i] = merge(dui[i+1],dui[i]);
/*		for(int j = 0; j < dui[i].size(); j++){
			dui[i][j]->print();
			printf("--------------------\n");
		}
		printf("==========================test\n");
		}*/

}
