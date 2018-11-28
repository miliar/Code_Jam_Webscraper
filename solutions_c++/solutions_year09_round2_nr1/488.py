#include <cstdio>
#include <cstring>
#include <algorithm>
#include <functional>
#include <map>

using namespace std;

struct node{
    struct node * ltree, * rtree, * parent;
    char ft[100];
    double p;
};

struct ltstr
{
    bool operator()(const char* s1, const char* s2) const
    {
	return strcmp(s1, s2) < 0;
    }
};


using namespace std;

int main(){
    
    node * root, * cur;
    char name[100];
    char ft[200][100];
    char c;
    double p, ans;

    int t;
    scanf("%d", &t);
    
    for (int casno = 1; casno <= t; casno ++){
	int tmp;
	scanf("%d", &tmp);
	
	while ((c=getchar()) != '(');
	root = (node *)malloc(sizeof(node));
 	cur = root;
	cur -> ltree = cur -> rtree = NULL;
	cur -> parent = NULL;

	c = ' ';
	while (cur){
	    if (c != ')')
		while (isspace(c=getchar()));

	    if (isdigit(c)){
		double m = 1;
		p = m * (c - '0');
		while (isdigit(c=getchar()) || c == '.'){
		    if (isdigit(c)){
			m *= 0.1;
			p += m * (c - '0');
		    }
		}
		cur -> p = p;
	    }
	    else if (islower(c)){
		int len = 0;
		cur -> ft[len++] = c;
		while (islower(c = getchar())){
		    cur -> ft[len++] = c;
		}
		cur -> ft[len] = '\0';
	    }
	    else if (c == '('){
		if (cur -> ltree == NULL){
		    cur -> ltree = (node *)malloc(sizeof(node));
		    cur -> ltree -> parent = cur;
		    cur = cur -> ltree;
		}
		else{
		    cur -> rtree = (node *)malloc(sizeof(node));
		    cur -> rtree -> parent = cur;
		    cur = cur -> rtree;
		}
		cur -> ltree = cur -> rtree = NULL;
	    }
	    else if (c == ')'){
		cur = cur -> parent;
		c = getchar();
	    }
	}
	
	printf("Case #%d:\n", casno);
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i ++){
	    scanf("%s", name);
	    int nft;
	    scanf("%d", &nft);
	    map<const char *, int, ltstr> features;
	    for (int j = 0; j < nft; j ++){
		scanf("%s", ft[j]);
		features[ft[j]] = 1;
	    }
	    
	    cur = root;
	    ans = 1.0;
	    while (cur){
		ans *= cur -> p;
		if (features[cur -> ft] == 1){
		    cur = cur -> ltree;
		}
		else
		    cur = cur -> rtree;
	    }
	    printf("%0.7lf\n", ans);
	}
    }
    return 0;
}
