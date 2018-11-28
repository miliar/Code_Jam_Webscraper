#include<stdio.h>
#include<string.h>
#include<stdlib.h>


char fea[120][15];
char Line[80000];
int k, len, f;

struct Tree{
	double p;
	char name[15];
	struct Tree *lch, *rch;		
};

void Creat(Tree *root)
{
	int i, j;
	char num[50];
	root->lch = root->rch = NULL;
	while(Line[k]!='(') k++;
	k++;
	while(Line[k]==' ') k++;
	for(j=0; Line[k]=='.' || (Line[k]<='9' && Line[k]>='0'); k++) num[j++]=Line[k];
	num[j] = '\0';
	root->p = atof(num);
	
	while(Line[k]==' ' && k<len) k++;

	if(Line[k]<='z' && Line[k]>='a'){
		for(i=0; Line[k]<='z' && Line[k]>='a'; k++) root->name[i++]=Line[k];
		root->name[i] = '\0';
		root->lch = new Tree;
		root->rch = new Tree;
		Creat(root->lch);
		Creat(root->rch);
	}
	k++;
	return;
}

bool Find(char *str)
{
	int i;
	for(i=0; i<f; i++)
		if(strcmp(str, fea[i])==0) return true;
	return false;
}

void dfs(Tree *root, double &res)
{
	if(root==NULL) return;
	res *= root->p;
	if(Find(root->name)) dfs(root->lch, res);
	else dfs(root->rch, res);
	return;
}

int main()
{
	int t, Case=0, L, i, j, N;
	double res;
	char ch;
	Tree *root;
	
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	scanf("%d", &t);
	while(t--){
		Case++;
		scanf("%d", &L);
		getchar();
		len = 0;
		while(L--){	
			while((ch=getchar())!='\n')
				Line[len++] = ch;
			Line[len++] = ' ';
		}
		Line[len++] = '\0';	
		k = 0;
		root = new Tree;
		Creat(root);
		
		scanf("%d", &N);
		printf("Case #%d:\n", Case);
		for(i=0; i<N; i++){
			scanf("%s", fea[0]);
			scanf("%d", &f);
			
			for(j=0; j<f; j++)
				scanf("%s", fea[j]);
			
			res = 1.0;
			dfs(root, res);
			printf("%.7f\n", res);
		}
	}
	return 0;
}


