#include <stdio.h>
#include <malloc.h>
#include <string.h>

#define L 15
#define D 5000
#define N 500

int l,d,n;

typedef struct node{
	char c;
	struct node *lchild;
	struct node *rchild;
}*pnode;

void Init_node(pnode p,char c){
	p->c = c;
	p->lchild = NULL;
	p->rchild = NULL;
}

pnode Insert_node(pnode temp,char c){
	pnode child = temp->lchild;
	if(child==NULL){
		child = (pnode)malloc(sizeof(pnode));
		Init_node(child,c);
		temp->lchild = child;
	}
	while(child->rchild!=NULL){
		if(child->c==c){
			return child;
		}
		child = child->rchild;
	}
	if(child->c == c){
		return child;
	} else {
		child->rchild = (pnode)malloc(sizeof(pnode));
		Init_node(child->rchild,c);
		return child->rchild;
	}

}

pnode IsChild(pnode p,char c){
	if(p->lchild!=NULL){
		p = p->lchild;
		while(p!=NULL){
			if(p->c==c)
				return p;
			p = p->rchild;
		}
	}
	return NULL;
}

int Cout(pnode head,char tree[][27],int m){
	if(m==l){
		return 1;
	}
	int i = 0;
	int sum = 0;
	pnode temp;
	while(tree[m][i]!='\0'){
		if(temp = IsChild(head,tree[m][i])){
			sum += Cout(temp,tree,m+1);
		}
		i++;
	}
	return sum;
}

int main(){
	//if(freopen("A-large.in", "r", stdin)!=NULL){
	//	freopen("A-large.out", "w", stdout);
	//}
	
	int k;
	int i,j;
	char test[L*28+1];
	char tree[L][27];
	pnode Head = (pnode)malloc(sizeof(pnode));
	pnode temp ;
	Init_node(Head,0);
	scanf("%d%d%d",&l,&d,&n);
	getchar();
	for(i=0;i<d;i++){
		temp = Head;
		for(j=0;j<l;j++){
			char c;
			scanf("%c",&c);
			temp = Insert_node(temp,c);
		}
		getchar();
	}
	for(i=0;i<n;i++){
		scanf("%s",test);
		int p=0;
		int q=0;
		for(j=0;j<l;j++){
			q = 0;
			if(test[p]=='('){
			
				p++;
				while(test[p]!=')'){
					tree[j][q] = test[p];
					q++;
					p++;
				}
				p++;
			}else {
				tree[j][q] = test[p];
				p++;
				q++;
			}
			tree[j][q]='\0';
		}
		k = Cout(Head,tree,0);
		printf("Case #%d: %d\n",i+1,k);
	}
	fclose(stdout);
	return 0;
}

