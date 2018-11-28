#include<cstdio>
#include<string>
#include<vector>

using namespace std;

struct Node{
	int Count;
	Node *Next[26];
	Node() {
		for(int i = 0 ; i < 26 ; i++) {
			Next[i] = NULL;
		}
		Count = 0;
	}
};

int L,D,N,Ans;
Node *Root;
string Str;
char Buff[500];
vector <int> Edges[20];

void Insert() {
	Node *p = Root;
	for(int i = 0 ; i < Str.length(); i++) {
		int Ind = Str[i] - 'a';
		if (p->Next[Ind] == NULL) {
			p->Next[Ind] = new Node();
		}
		p = p->Next[Ind];			
	}
	p->Count++;
}

void DFS(int i,Node *p) {
	if (i >= L) {
		Ans++;
	}
	
	for(int j = 0 ; j < Edges[i].size() ; j++) {
		if (p->Next[Edges[i][j]]) {
			DFS(i + 1,p->Next[Edges[i][j]]);
		}
	}
}

int main() {
	freopen("A.txt","r",stdin);
	freopen("A.out","w",stdout);
	Root = new Node();
	
	scanf("%d%d%d",&L,&N,&D);
	for(int i = 0 ; i < N ; i++) {
		scanf("%s",Buff);
		Str = string(Buff);
		Insert();
	}
	
	for(int i = 0 ; i < D ; i++) {
		for(int k = 0 ; k < 20 ; k++) {
			Edges[k].clear();
		}
		scanf("%s",Buff);
		Str = string(Buff);
		int Pos = 0;
		bool Inner = false;
		for(int j = 0 ; j < Str.length() ; j++) {
			if (Str[j] == '(') {
				Inner = true;
				continue;
			}
			if (Str[j] == ')') {
				Inner = false;
				Pos++;
				continue;
			}
			int Ind = Str[j] - 'a';
			Edges[Pos].push_back(Ind);
			if (!Inner) {
				Pos++;
			}
		}
		
		Ans = 0;
		DFS(0,Root);
		
		printf("Case #%d: %d\n",i + 1 , Ans);
	}
	
//	while(1);
	return 0;
}
