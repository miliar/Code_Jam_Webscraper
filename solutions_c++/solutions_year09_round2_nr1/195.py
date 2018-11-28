#pragma warning(disable:4786)

#include<assert.h>
#include<stdio.h>
#include<string.h>
#include<string>
#include<set>
using namespace std;

#define root 0

typedef string str;

struct Node{
	double p;
	str feat;
	int yes,no;
};

int marker;
Node node[80005];

set<str> ss;

int L;

int ntok;
char token[80005][150];
int  type[80005];

char buf[800005];

int x;
int Tree(){
	int cur = marker++;
	sscanf(token[x], "%lf", &node[cur].p);
	x++;

	if(type[x] == 0 && x < ntok){
		node[cur].feat = str(token[x]);
		x++;
		node[cur].yes = Tree();
		node[cur].no = Tree();
	}
	else{
		node[cur].feat = "";
		node[cur].yes = -1;
		node[cur].no = -1;
	}

	return cur;
}

int main(){

	int n,i,q,j;
	int N,T;
	double p;
	char *t;

	scanf("%d",&T);
	for(N=1;N<=T;N++){

		scanf("%d",&L);

		j = 0;
		gets(buf);
		for(i=0;i<L;i++){
			gets(buf+j);
			j+=strlen(buf+j);
		}
//		printf(">>>%s<<<\n",buf);
		L = j;
		for(i=0;i<L;i++)if(buf[i]=='(' || buf[i]==')')
			buf[i] = ' ';
//		printf(">>>%s<<<\n",buf);
		
		ntok = 0;
		t = strtok(buf," \n\r");
		while(t!=NULL){
			sscanf(t,"%s",token[ntok]);
			if(sscanf(token[ntok],"%lf",&p)==1)
				type[ntok] = 1;
			else
				type[ntok] = 0;
			ntok++;
			t = strtok(NULL," \n\r");
		}

//		printf(">>>%d   \n",ntok);

//		for(i=0;i<ntok;i++)
//			printf(">>> %s %d\n",token[i],type[i]);

		x = 0;
		marker = root;
		Tree();

//		printf(">>>%d   \n",x);
//
//		for(i=0;i<=2;i++)
//			printf(">>>>>>>>>>>>>>> %d : %d %d\n",i,node[i].yes,node[i].no);

		assert(x==ntok);

		scanf("%d",&q);
		printf("Case #%d:\n",N);
		while(q--){
			ss.clear();
			scanf("%s%d",buf,&n);
			for(i=0;i<n;i++){
				scanf("%s",buf);
				ss.insert(str(buf));
			}

			p = 1.0;
			i = root;

			while(1){
				p*=node[i].p;
				if(node[i].yes == -1)
					break;
				
				if(ss.find(node[i].feat)!=ss.end())
					i = node[i].yes;
				else
					i = node[i].no;
			}
			printf("%.10lf\n",p);
		}


	
			
	}

	return 0;
}