#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

struct node{
	node* ptr[27];
	node(){ for(int i=0;i<27;i++) ptr[i] = NULL; }
}*head;

int L, D, N, nCase, cnt;
char s[20];
vector< vector<int> > cand;
bool check[27];

#define offset ('a'-1)

void insert(char *s, int len){
	node* P = head;
	for(int i=0;i<len;i++){
		if(P->ptr[s[i]-offset]==NULL)
			P->ptr[s[i]-offset] = new node();
		P = P->ptr[s[i]-offset];
	}
	P->ptr[0]=head;
}
void Find(node* P, int x){
	if(x==L){ ++cnt; return; }
	for(int i=0;i<cand[x].size();i++)
		if(P->ptr[cand[x][i]]!=NULL){
			Find(P->ptr[cand[x][i]], x+1);
		}
	
}



int main(){
	cin>>L>>D>>N;
	head = new node();
	for(int i=0;i<D;i++){
		cin>>s;
		insert(s, L);
	}
	cand = vector< vector<int> > (L);
	string exp;
	for(int i=0;i<N;i++){
		cin>>exp;
		for(int j=0, k=0;j<exp.length();j++,k++){
			cand[k] = vector<int>();
			memset(check, false, sizeof check);
			if(exp[j]=='('){
				++j;
				while(exp[j]!=')'){
					if(!check[exp[j]-offset])
						cand[k].push_back(exp[j]-offset);
					check[exp[j]-offset] = true;
					++j;
				}
			}
			else cand[k].push_back(exp[j]-offset);
//			for(int j=0;j<cand[k].size();j++) printf("%c", cand[k][j]+offset);
//			printf("\n");
		}
		cnt = 0;
		Find(head, 0);
		printf("Case #%d: %d\n", i+1, cnt);
	}
    return 0;
}

