#include <set>
#include <string>
#include <vector>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <queue>
#include <sstream>
using namespace std;

struct trie_node{
    bool word;
    struct trie_node* child[26];
};

struct trie{
    struct trie_node *sub;
};

struct trie * trie_init(void)
{
    struct trie * sub = (struct trie*)calloc(sizeof(struct trie), 1);   
    sub->sub = (struct trie_node*)calloc(sizeof(struct trie_node), 1);
    return sub;
}

struct trie * trie_insert(struct trie*& trie, const char *str)
{
    struct trie_node *cur = trie->sub;
    char *ptr = const_cast<char*>(str);    
    while(*ptr != '\0'){
	if(cur->child[*ptr - 'a'] == NULL){
	    cur->child[*ptr - 'a'] = (struct trie_node*)calloc(sizeof(struct trie_node), 1);	    
	}
	cur = cur->child[*ptr++ - 'a'];	
    }
    cur->word = true;
}

struct trie_node* trie_search(struct trie_node* node, char ch)
{
    if(node->child[ch - 'a'] == NULL){
	return NULL;
    }
    else
	return node->child[ch - 'a'];
}

bool trie_find(struct trie * trie, const char *str)
{
    char *ptr = const_cast<char*>(str);
    struct trie_node *sub = trie->sub;
    while(*ptr != '\0'){
	if(sub->child[*ptr - 'a'] == NULL)
	    return false;
	else
	    sub = sub->child[*ptr++ - 'a'];
    }
    if(sub->word)
	return true;
    else
	return false;
}

vector<vector<char> > parse(const string& in)
{
    int j, n = (int)in.size();
    bool par;    
    vector<char> ret;
    vector<vector<char> > ans;
    for(j = 0, par = false; j < n; j++){
	if(in[j] == '('){
	    if(!ret.empty()){
		ans.push_back(ret);
	    }
	    else{
		ret.clear();
		par = true;
	    }
	}
	else if(in[j] == ')'){
	    ans.push_back(ret);
	    ret.clear();
	    par = false;
	}
	else if(in[j] >= 'a' && in[j] <= 'z'){
	    if(par)
	    	ret.push_back(in[j]);	    
	    else{
		ret.push_back(in[j]);
		ans.push_back(ret);
		ret.clear();
	    }
	}
    }
    if(!ret.empty())
	ans.push_back(ret);
    return ans;
}

bool prefix(struct trie * trie, const string& s)
{
    struct trie_node *sub = trie->sub;
    int j, sz = (int)s.size();
    for(j = 0; j < sz; j++){
	if(sub->child[s[j] - 'a'] == NULL)
	    return false;
	sub = sub->child[s[j] - 'a'];
    }
    if(!sub)
	return false;
    else
	return true;
}

void dfs(const vector<vector<char> >& v, int j, string s, struct trie *trie, int& ans)
{
    if(j == v.size()){
	if(trie_find(trie, s.c_str())){
	    ans++;
	}
	return;
    }
    else{	
	if(s.size() != 0){
	    if(!prefix(trie, s))
		return;
	}
	for(int k = 0; k < v[j].size(); k++){
	    dfs(v, j + 1, s + v[j][k], trie, ans);
	}
    }
}

int solve(const vector<vector<char> >& v, struct trie * trie)
{
    int ans = 0;
    string s = "";
    dfs(v, 0, s, trie, ans);
    return ans;
}

int main()
{
    string in;
    int j, L, D, N, ans;
    struct trie * trie = trie_init();
    scanf("%d%d%d", &L, &D, &N);
    for(j = 0; j < D; j++){
	cin>>in;
	trie_insert(trie, in.c_str());
    }
    for(j = 1; j <= N; j++){
	cin>>in;
	vector<vector<char> > v = parse(in);
	ans = solve(v, trie);
	printf("Case #%d: %d\n", j, ans);
    }
    return 0;
}
