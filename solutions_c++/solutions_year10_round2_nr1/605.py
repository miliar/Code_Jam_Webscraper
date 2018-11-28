#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <list>
using namespace std;

class st{
public:
	char name[111];//the first one is not
	st* next;
	st* son;

	st(){
		memset(name,0,sizeof(name));
		next=NULL;
		son=NULL;
	}
    int	addpath(char * path){
		if(path[0]==0)
			return 0;

		char thisname[111];
		long i;
		i=0;
		if(path[0]=='/')path++;
		while(path[i]!='/'&&path[i]!=0){
			thisname[i]=path[i];
			i++;
		}
		thisname[i]=0;
		
		st *p=next;
		st *lastp;
		lastp=this;

		while(p!=NULL){
			if(!strcmp(p->name,thisname)){//ÏàÍ¬
				if(path[strlen(thisname)]!=0){
					if(p->son==NULL){
						p->son=new st;
					}
					return p->son->addpath(path+strlen(thisname)+1);
				}else 
					return 0;
			}
			lastp=p;
			p=p->next;
		}
		//cannot find;
		//cout<<"ADD:"<<thisname<<endl;/////////////
		lastp->next=new st;
		p=lastp->next;
		strcpy(p->name,thisname);
		if(path[strlen(thisname)]!=0){
			if(p->son==NULL)p->son=new st;
			return 1+ p->son->addpath(path+strlen(thisname)+1);
		}else 
			return 1;
	}
};

int main(){
	st *lists;
	long cc,tt;
	long n,m;
	long i;
	char path[111];
	scanf("%d",&tt);
	for(cc=0;cc<tt;cc++){
		lists=new st;
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++){
			scanf("%s",path);
			lists->addpath(path);
		}
		long sum=0;
		for(i=0;i<m;i++){
			scanf("%s",path);
			sum+=lists->addpath(path);
		}
		printf("Case #%d: %d\n",cc+1,sum);
		delete lists;
	}
	return 0;
}

/*
2 2
\a
\b
\a\a
\b\b

*/