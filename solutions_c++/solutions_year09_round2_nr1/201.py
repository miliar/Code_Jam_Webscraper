#include<iostream>
#include<cstring>
using namespace std;
char s[8001],animal_feature[100][20];
struct tree{
	double weight;
	char feature[20];
	tree *left,*right;
};
tree node[1000];
int top;
void make_tree(char *&ptr,tree *tree_ptr){
//	printf("new tree %s\n",ptr);
	while(*ptr++!='(');
	int len;
	sscanf(ptr,"%lf%n",&tree_ptr->weight,&len);
//	printf("weight \"%lf\"\n",tree_ptr->weight);
	tree_ptr->feature[0]='\0';
	ptr+=len;
	for(;;){
		if(*ptr==' '){
			++ptr;
		}else if(*ptr==')'){
			break;
		}else{
			char *feature=tree_ptr->feature;
			while(*ptr!='(' && *ptr!=' ')
				*feature++=*ptr++;
			*feature='\0';
//			printf("feature \"%s\"\n",tree_ptr->feature);
			tree_ptr->left=&node[++top];
			make_tree(ptr,tree_ptr->left);
			tree_ptr->right=&node[++top];
			make_tree(ptr,tree_ptr->right);
		}
	}
	++ptr;
	return;
}
double dfs(tree *ptr,int n){
	if(ptr->feature[0]=='\0')
		return ptr->weight;
	for(int i=0;i<n;++i)
		if(strcmp(animal_feature[i],ptr->feature)==0)
			return ptr->weight*dfs(ptr->left,n);
	return ptr->weight*dfs(ptr->right,n);
}
int main(){
	int N;
	scanf("%d",&N);
	for(int k=1;k<=N;++k){
		{
			int L;
			char t[81],*ptr;
			scanf("%d",&L);
			gets(t);
			s[0]='\0';
			for(int i=0;i<L;++i){
				gets(t);
				strcat(s,t);
			}
			top=0;
			ptr=s;
			make_tree(ptr,&node[0]);
		}
		printf("Case #%d:\n",k);
		{
			int A;
			cin>>A;
			for(int i=0;i<A;++i){
				int n;
				scanf("%*s%d",&n);
				for(int j=0;j<n;++j)
					scanf("%s",animal_feature[j]);
				printf("%.7lf\n",dfs(&node[0],n));
			}
		}
	}
	return 0;
}
