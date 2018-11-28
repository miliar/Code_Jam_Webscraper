#pragma warning(disable:4786)
#include<stdio.h>
#include<map>
#include<string>
using namespace std;

#define ROOT 1

int nex, nnw;
int n,c;
struct Node{
	int stat;
	map<string, int> chi;
	Node(int s = 0){
		stat = s;
		if(s==0)
			c++;
		chi.clear();
	}

} node[100000];

char s[1000];

int main(){
	int T,N;
	char *t;
	char d[1000];
	string name;

	int dir,chidir;

	scanf("%d",&T);

	for(N=1;N<=T;N++){
	
		scanf("%d%d",&nex,&nnw);

		node[ROOT] = Node(1);
		n = 2;
		
		while(nex--){
			scanf("%s",s);
			t = strtok(s,"/\n");
			dir = ROOT;

			while(t!=NULL){
				sscanf(t,"%s",d);
				name = string(d);

				chidir = node[dir].chi[name];
				if(chidir==0){
					node[dir].chi[name] = n;
					node[n] = Node(1);
					chidir = n;
					n++;
				}
				dir = chidir;

				t = strtok(NULL,"/\n");
			}
		}

		c = 0;

		while(nnw--){
			scanf("%s",s);
			t = strtok(s,"/\n");
			dir = ROOT;
			while(t!=NULL){
				sscanf(t,"%s",d);
				name = string(d);

				chidir = node[dir].chi[name];
				if(chidir==0){
					node[dir].chi[name] = n;
					node[n] = Node();
					chidir = n;
					n++;
				}
				dir = chidir;

				t = strtok(NULL,"/\n");
			}
		}

		printf("Case #%d: %d\n",N,c);
	}

	return 0;
}