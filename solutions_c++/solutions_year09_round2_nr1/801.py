/*
 * GCJ_R1_A.cpp
 *
 *  Created on: 2009-9-13
 *      Author: yaoman
 */

#include <ctype.h>
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

struct Node{
	double p;
	string s;
};

Node tree[10000];
istringstream iss;
string list[110];
int num;

void DFS(int t){
	iss>>tree[t].p>>tree[t].s;
	if (tree[t].s=="#") return ;
	DFS(t*2);
	DFS(t*2+1);
}

double cal(int t, double p){
	p *= tree[t].p;
	if (tree[t].s=="#") return p;
	for (int i=0; i<num; i++){
		if (tree[t].s==list[i]){
			return cal(t*2,p);
		}
	}
	return cal(t*2+1,p);
}

int main(){
	int n,k,L,i,j,m;
	string str,s;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("ans.out","w",stdout);
	scanf("%d",&n);
	for (k=1; k<=n; k++){
		scanf("%d",&L);
		str = "";
		for (i=0; i<L; i++){
			while (getline(cin,s),s=="");
			str += s;
		}
		for (i=0; i<(int)str.size(); i++){
			if (str[i]==')'){
				for (j=i-1; j>=0; j--){
					if (str[j]!=' ') break;
				}
				if (isdigit(str[j])){
					str.replace(i,1," # ");
					continue;
				}
			}
			if (str[i]=='(' || str[i]==')') str[i] = ' ';
		}
		iss.str(str);
		DFS(1);
		printf("Case #%d:\n",k);
		scanf("%d",&m);
		for (i=0; i<m; i++){
			cin>>s;
			cin>>num;
			for (j=0; j<num; j++){
				cin>>list[j];
			}
			printf("%.9lf\n",cal(1,1));
		}
	}
	return 0;
}
