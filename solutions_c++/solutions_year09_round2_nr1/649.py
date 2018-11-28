#pragma warning(disable:4786)

#include <stdio.h>
#include <string>
#include <map>

using namespace std;

struct NODE {
	double val;
	string str;
}tree[10000];
char str[100000];
char line[10000];

void dfs(int left,int right,int root) {
	int i,j,k;
	for (i = left; i < right; i ++) {
		if (str[i] == '(') {
			// 
			// double , str..
			
			sscanf(str+i+1,"%lf",&tree[root].val);
			tree[root].str = "";
			for (j = i + 1; j < right; j ++) {
				if ((str[j] >= '0' && str[j] <= '9') || str[j] == '.' || str[j] == ' ')
					continue;
				else
					break;
			}
			int num = 0;
			if (str[j] == '(') {
				num ++;
				i = j;
			} else if (str[j] == ')') {
				return ;
			} else {
				for (k = j; k < right; k ++) {
					if (str[k] >= 'a' && str[k] <= 'z') {
						tree[root].str += str[k];
					} else 
						break;
				}
				for (; k < right; k ++) {
					if (str[k] == '(') {
						i = k;
						break;
					}
				}
			}
			break;
		} 
	}
	////// i...
	int num = 0;
	for (j = i; j < right; j ++) {
		if (str[j] == '(')
			num ++;
		else if (str[j] == ')') {
			num --;
			if (num == 0)
				break;
		}
	}
	dfs(i,j+1,root*2);
	num = 0;
	i = j + 1;
	for (++ j; j < right; j ++) {
		if (str[j] == '(')
			num ++;
		else if (str[j] == ')') {
			num --;
			if (num == 0)
				break;
		}
	}
	dfs(i,j+1,root*2+1);
}
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	int L;
	int i,j,k;
	int Case;
	int n,m;
	scanf("%d",&T);
	for (Case = 1; Case <= T; Case ++) {
		scanf("%d",&L);
	//	memset(str,0,sizeof(str));
		for (i = 0; i < L;  i ++) {
			scanf(" ");
			gets(line);
			strcat(str,line);
		}
		memset(tree,0,sizeof(tree));
		int num = 0;

		int len = strlen(str);

		dfs(0,len,1);
		/*
		for (i = 1; i < 20; i ++) {
			printf("%d %lf %s\n",i,tree[i].val,tree[i].str.c_str());
		}*/
		scanf("%d",&n);
		printf("Case #%d:\n",Case);
		for (i = 0; i < n; i ++) {
			scanf("%s",str);
			map<string,int> Map;
			scanf("%d",&m);
			for (j = 0; j < m; j ++) {
				scanf("%s",str);
				string STR(str);
				Map[STR] = 0;
			}
			int root = 1;
			double ans = tree[1].val;
			while (1) {
				if (tree[root].str == "") {
				//	ans *= tree[root].val;
					break;
				}
				if (Map.find(tree[root].str) == Map.end()) {
					root = root * 2 + 1;
					ans *= tree[root].val;
				} else {
					root = root * 2;
					ans = ans * tree[root].val;
				}
			}
			printf("%.7lf\n",ans);
		}

	}
	return 0;
}