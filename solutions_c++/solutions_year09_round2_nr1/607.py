#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

struct Node{
	char feature[20];
	double prob;
	Node *left, *right;
};

Node space[1000];
int scnt;
string str;

void proc( int start, int end, Node* root){
	root->left = root->right = NULL;
	int i;
	double val;
	char name[20];
	bool flag[2];
	flag[0] = flag[1] = false;
	int cnt = 0;
	for(i=start;i<=end;++i){
		if( str[i]==' ' )	continue;
		if( str[i]=='(' )	++cnt;
		if( str[i]>='0' && str[i]<='9' && !flag[0] ){
			sscanf(&str[i],"%lf",&val);
			flag[0] = true;
		}
		if( str[i]>='a' && str[i]<='z' && !flag[1] ){
			sscanf(&str[i],"%s",name);
			flag[1] = true;
		}
	}
	strcpy( root->feature, name );
	root->prob = val;
	//printf("cnt = %d\n",cnt);
	if( cnt==1 )	return;
	root->left = &space[scnt++];
	root->right = &space[scnt++];
	
	int s1;
	s1 = 0;
	bool fL = true;
	cnt = 0;
	for(i=start;i<=end;++i){
		if( str[i]==' ' )	continue;
		if( str[i]=='(' ){
			++cnt;
			if( cnt==2 )	s1 = i;
		}
		if( str[i]==')' ){
			--cnt;
			if( cnt==1 ){
				if( fL )	proc( s1, i, root->right );
				else	proc( s1, i, root->left );
				fL = false;
				s1 = 0;
			}
		}
	}
}

void test( Node * root ){
	printf("test new node\n");
	printf("with value = %lf\n",root->prob);
	if( root->left==NULL )	return ;
	printf("with featue = %s\n",root->feature);
	test( root->left);
	test( root->right);
}

char list[120][50];

void vis( double &p , Node *root, int num ){
	//printf("vis( %lf, %lf, %s )\n",p,root->prob,root->feature);
	bool flag = false;
	p *= root->prob;
	if( root->left==NULL )	return;
	for(int i=0;i<num;++i){
		if( strcmp(root->feature, list[i])==0 ){
			flag = true;
			break;
		}
	}
	if( flag )	vis( p, root->right, num );
	else	vis( p, root->left, num );
}

int main(){
	char buf[100];
	//freopen("pa.in","r",stdin);
	freopen("A-small-attempt1.in","r",stdin);
	int turn, T;
	fgets(buf,100,stdin);
	sscanf(buf,"%d",&T);
	
	int L, i, len;
	for(turn=0;turn<T;++turn){
		fgets(buf,100,stdin);
		sscanf(buf,"%d",&L);
		str = string();
		scnt = 1;
		for(i=0;i<L;++i){
			fgets(buf,100,stdin);
			
			int j = 0;
			while( 1 ){
				if( buf[j]=='\n' ){
					buf[j] = '\0';
					break;
				}
				++j;
			}
			string tmp = string(buf);
			str = str + tmp;
			
		}
		space[0].left = space[0].right = NULL;
		proc( 0, str.size()-1, &space[0]  );
		fgets(buf,100,stdin);
		int kind;
		sscanf(buf,"%d",&kind);
		printf("Case #%d:\n",1+turn);
		for(i=0;i<kind;++i){
			fgets(buf,100,stdin);
			char *p = strtok(buf," ");
			p = strtok(NULL," ");
			int C;
			sscanf(p,"%d",&C);
			for(int j=0;j<C;++j){
				p = strtok(NULL, " ");
				sscanf(p,"%s",list[j]);
			}
			double pr = 1.0;
			vis( pr , &space[0], C );
			printf("%.7lf\n",pr);
		}
	}
	return 0;
}
