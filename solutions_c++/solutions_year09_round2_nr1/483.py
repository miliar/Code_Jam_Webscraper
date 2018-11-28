#include "stdio.h"
#include "iostream"
#include "string.h"
#include "math.h"
#include "string"
#include "vector"
#include "set"
#include "map"
#include "queue"
#include "list"
#include "stack"

using namespace std;
struct node
{
	double wei;
	string fe;
	node *lf,*rh;
};
void gettree(node *p);
void buildtree(node *p);

void buildtree(node *p)
{
	p->fe="";
	char ch;
	while(ch=cin.peek(), ch!='(' && !(ch<='z' && ch>='a'))
		cin.ignore();

	if(ch<='z' && ch>='a') cin>>p->fe;
	while(ch=cin.peek(), ch!='(' )
		cin.ignore();
	cin.ignore();
	cin>>p->wei;

	while(ch=cin.peek(),ch!=')' && ch!='(' && !(ch<='z' && ch>='a')) 
		cin.ignore();

	if(ch==')'){
		p->lf=p->rh=NULL;
		cin.ignore();
		return ;
	}
	p->lf=new node;
	buildtree(p->lf);

	while(ch=cin.peek(),ch!=')' && ch!='(' && !(ch<='z' && ch>='a')) 
		cin.ignore();

	if(ch==')'){
		p->rh=NULL;
		cin.ignore();
		return ;
	}

	p->rh=new node;
	buildtree(p->rh);
	while(ch=cin.peek(),ch!=')') 
		cin.ignore();
	cin.ignore();
	return;
}

void destroytree(node *p)
{
	if(p->lf!=NULL) destroytree(p->lf);
	if(p->rh!=NULL) destroytree(p->rh);
	delete p;
}

void dealquiery(node *root)
{
	string tmp;
	cin>>tmp;
	int n;
	cin>>n;
	string fea[101];
	int i;
	for(i=0;i<n;i++)
		cin>>fea[i];
	double ans=1.0;
	node *p=root;
	while(p->lf!=NULL && p->rh!=NULL){
		ans*=p->wei;
		bool flag=1;
		for(i=0;i<n;i++){
			if(p->lf->fe==fea[i]){
				p=p->lf;
				flag=0;
				break;
			}
		}
		if(flag){
			p=p->rh;
		}
	}
	ans*=p->wei;
	printf("%.7lf\n",ans);
	return;

}
int main()
{
	int cs;
	scanf("%d",&cs);
		freopen("out.txt","w",stdout);

	for(int ii=1;ii<=cs;ii++){
		printf("Case #%d: \n",ii);
		int tmp;
		cin>>tmp;
		node *root=new node;
		buildtree(root);
		//	root->fe=root->lf->fe;
		int qui;
		cin>>qui;
		//	cout<<"ok";
		while(qui--){
			dealquiery(root);
		}
		destroytree(root);

	}

}

