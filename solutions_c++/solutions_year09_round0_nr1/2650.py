#include <iostream>
using namespace std;
struct Trie {
	Trie *child[27];
	Trie() {
		for (int i = 0; i < 26; i++)
			child[i] = NULL;
	} 
};
FILE *fp = fopen("c:\\a.txt", "w");
int l, d, n;
int ans;
Trie *root;
char tmp[16];
char str[16][5000];
char aa[20];
void insert(char* word) 
{
	int branch;
	Trie *current = root;
	int i = 0;
	while (word[i]) {
		branch = word[i] - 'a';
		if (current->child[branch] == NULL) {
			current->child[branch] = new Trie; 
		}
		current = current->child[branch];
		i++;
	}
}

bool search(char* word)
{
	int branch;
	Trie *current = root;
	int i = 0;
	while (word[i]) {
		branch = word[i] - 'a';
		if (current->child[branch] == NULL) {
			return false;
		}
		current = current->child[branch];
		i++;
	}
	return true;
}

void bfs(int i) 
{
	int j;
	if (i == l + 1) ans++;
	for (j = 1; str[i][j]; j++) {
		aa[i] = str[i][j];
		aa[i + 1] = 0;
		if (search(aa+1)) {
			bfs (i + 1);
		}
	}
}
int main()
{

	int i, j;
	char str1[5000], a;
	scanf ("%d%d%d", &l, &d, &n);

	root = new Trie;
	for (i = 1; i <= d; i++) {
		scanf("%s", tmp);
		insert(tmp);
	}
	int k = 0;
	while(n--) {
		k++;
		memset(str, 0, sizeof(str));
		getchar();
		for (i = 1; i <= l; i++) { 
			j = 1;
			scanf("%c", &a);
			if (a == '(') {
				
				while (a!= ')') {
					scanf("%c", &a);
					str[i][j++] = a;
				}
				str[i][j - 1] = 0;
				continue;
			}
			str[i][j] = a;
		}

		ans = 0;
		memset(aa, 0, sizeof(aa));
		bfs(1);
		fprintf(fp,"Case #%d: %d\n", k, ans);

	}
	fclose(fp); 

}