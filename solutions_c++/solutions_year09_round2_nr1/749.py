#include<cstdio>
#include<cstdlib>
#include<cstring>
struct Feature
{
double w;
char f[11];
Feature* left;
Feature* right;
};
double rate;
char f[100][11];
int n;
int compare(const void* a,const void* b)
{
return strcmp((char*)a,(char*)b);
}
void readNode(Feature* &node)
{
char ch;
node=new Feature;
node->left=NULL;
node->right=NULL;
scanf(" ( %lf",&node->w);
while((ch=getc(stdin))==' ' || ch=='\n');
if(ch!=')')
	{
	node->f[0]=ch;
	if(scanf("%[a-z]s",&node->f[1])==0)
		node->f[1]='\0';
	readNode(node->left);
	readNode(node->right);
	while(getc(stdin)!=')');
	}
}
void clear(Feature* node)
{
if(node->left)
	clear(node->left),clear(node->right);
delete node;
}
void cal(Feature* node)
{
rate*=node->w;
if(node->left!=NULL)
	{
	if(bsearch(node->f,f,n,sizeof(f[0]),compare)!=NULL)
		cal(node->left);
	else 
		cal(node->right);
	}
}
int main()
{
Feature* root=NULL;
int nT,i,k,t,nA;
scanf("%d",&nT);
for(t=1;t<=nT;++t)
	{
	scanf("%*d");
	readNode(root);
	scanf("%d",&nA);
	printf("Case #%d:\n",t);
	for(k=0;k<nA;++k)
		{
		scanf("%*s%d",&n);
		for(i=0;i<n;++i)
			scanf("%s",f[i]);
		qsort(f,n,sizeof(f[0]),compare);
		rate=1.0;
		cal(root);
		printf("%.7lf\n",rate);
		}
	clear(root);
	}
}