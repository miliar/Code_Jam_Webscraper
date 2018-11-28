#include<cstdio>
#include<cstring>
#define MAXWIDTH 26
struct Trie
{
	bool safe;
	Trie* child[MAXWIDTH];
	void Init()
	{
		int i;
		for(i = 0; i < MAXWIDTH; i++)
			 child[i] = NULL;
		safe = true;
	}
};

void Insert(Trie* root,char* s)
{
	int i;
	Trie* tmp = root;
	for(i = 0; s[i]; i++){
		if(tmp->child[s[i] - 'a'] == NULL){
			Trie* newp = new Trie;
			newp->Init();
			tmp->child[s[i] - 'a'] = newp;
		}
		tmp = tmp->child[s[i] - 'a'];
	}
	tmp->safe = false;
}

int ans;

void dfs(Trie* root,char* s,int cur)
{
	int i;
	if(s[cur] == '\0'){
		if(root->safe == false)
			ans++;
		return;
	}
	if(s[cur] == '('){
		int p;
		for(p = 1; s[cur + p] != ')'; p++);
		for(i = 1; s[cur + i] != ')'; i++){
			if(root->child[s[cur + i] - 'a'] != NULL)
				dfs(root->child[s[cur + i] - 'a'], s, cur + p + 1);
		}
	}
	else if(root->child[s[cur] - 'a'] != NULL)
		dfs(root->child[s[cur] - 'a'], s, cur + 1);

}

int main()
{
//	freopen("ans1.txt","w",stdout);
//	freopen("A-large.in","r",stdin);
	int L,D,N;
	char s[27*15];
	Trie root;
	while(scanf("%d%d%d",&L,&D,&N)!=EOF){
		int i;
		root.Init();
		for(i = 0; i < D; i++){
			scanf("%s",s);
			Insert(&root,s);
		}
		
		for(i = 0; i < N; i++){
			ans = 0; 
			scanf("%s",s);
			dfs(&root,s,0);
			printf("Case #%d: %d\n",i+1,ans);
		}
	}
	return 0;
}



