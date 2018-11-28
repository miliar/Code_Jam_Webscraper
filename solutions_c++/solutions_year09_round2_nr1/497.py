#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <map>

using namespace std;


int n , l;
char tmp[110];
char str[1101010];

map <string , bool> hash[110];
char name[100];
int len;

struct node{
	node *lc , *rc;
	string fet;
	double val;
	node(){
		lc = rc = NULL;
		val = 0;
		fet.clear();
	}
};

void dfs(node * nd , int pos)
{
	int i , j;
	char fet[100];
	int cnt = 0;
	for (i = pos ; i < len ; i ++){

		if (str[i] == '('){
			node * next = new node();
			for (j = i - 1 ; j >= 0 ; j --){
				if (str[j] == ')' || str[j] == '(' || isdigit(str[j]))break;
			} 
			for (j = j + 1 ; j < i ; j ++){
				if (isalpha(str[j]))break;
			}
			for (j = j ; j < i ; j ++){
				if (!isalpha(str[j]))break;
				fet[cnt ++] = str[j];
				str[j] = ' ';
			}
			fet[cnt] = '\0';
			
			next->fet = fet;
			cnt = 0;
			if (nd->lc == NULL)
				nd->lc = next;
			else
				nd->rc = next;
			dfs(next , i + 1);
		}
		else if (str[i] == ')'){
			str[i] = ',';
			for (j = i ; j >= 0 ; j --)
				if (str[j] == '('){
					str[j] = ',';
					break;
				}
			return;
		}
		else if (str[i] >= '0' && str[i] <= '9'){
			double tv;
			sscanf(str + i , "%lf" , &tv);
			nd->val = tv;
			while (str[i] >= '0' && str[i] <= '9' || str[i] == '.'){
				str[i] = ' ';
				i ++;
			}
			i --;
		}

	}
}

double cal(int index , node * nd)
{
	double tmp =  1 , ret = 1;

	tmp = nd->val;

	if (nd->lc == NULL)return tmp;

	if (nd->lc->fet.empty() == 0){
		if (hash[index][nd->lc->fet]){
			ret = cal(index , nd->lc);
		}
		else{
			ret = cal(index , nd->rc);
		}
	}
	else{
		ret = cal(index , nd->lc);
	}
	return ret * tmp;

}

int main()
{

	int t;
	int cas = 0;
	freopen("test.in" , "r" , stdin);
	freopen("test.out" , "w" , stdout);
	scanf("%d" , &t);
	while (t --){

		cas ++;
		printf("Case #%d:\n" , cas);
		scanf("%d" , &l);
		getchar();
		int i;
		node * root = new node();
		node * p = root;
		root->val = 1;
		for (i = 0 ; i < l ; i ++){
			gets(tmp);
			strcat(str , tmp);
		}
		//printf("%s\n" , str);

		len = strlen(str);
		dfs(root , 0);

		scanf("%d" , &n);
		for (i = 0 ; i < n ; i ++)
			hash[i].clear();
		for (i = 0 ; i < n ; i ++){
			int tp;
			string tn;
			scanf("%s" , name);
			scanf("%d" , &tp);
			int j;
			for (j = 0 ; j < tp ; j ++){
				scanf("%s" , name);
				tn = name;
				hash[i][tn] = 1;
			}
		}
		
		for (i = 0 ; i < n ; i ++){
			printf("%.7lf\n" , cal(i , root->lc));
		}


	}
	

	return 19890907;
}