#include<cstdio>
#include<cstring>
struct node{
	node *list[26];
};


int L,D,N;

int calc(int len, node *root, char *s)
{
	if (len==0 && *s=='\0')
		return 1;
	if (*s!='('){
		if (root->list[ (*s) - 'a' ]!=NULL)
			return calc(len-1, root->list[(*s)-'a'], s+1);
		else
			return 0;
	}
	char *p=s;
	int ans = 0;
	while (*p!=')') p++;
	p++;
	s++;
	while (*s!=')'){
		if (root->list[ (*s) - 'a' ]!=NULL)
			ans += calc(len-1, root->list[(*s)-'a'], p);
		s++;
	}
	return ans;
}

int main(){
	int i, j;
	char s[2000];
	node R, *cur;

	memset(&R, 0, sizeof(R));

	scanf("%d%d%d",&L,&D,&N);
	for (i=0;i<D;i++){
		scanf("%s",s);
		cur=&R;
		for (j=0;j<L;j++){
			if (cur->list[s[j]-'a']==NULL){
				cur->list[s[j]-'a'] = new node;
				memset(cur->list[s[j]-'a'], 0, sizeof(node));
			}
			cur = cur->list[s[j]-'a'];
		}
	}

	for (i=0;i<N;i++){
		scanf("%s",s);
		printf("Case #%d: %d\n", i+1, calc(L, &R, s));
	}
	return 0;
}
