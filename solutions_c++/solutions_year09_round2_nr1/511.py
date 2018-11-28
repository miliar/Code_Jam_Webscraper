#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
using namespace std;

#define FOR(i,n) for( i = 0 ; i<n ; i++)
#define RFOR(i,a,b)  for( i = a ; i<b ; i++)
#define CLR(a) memset(a,0,sizeof(a))
#define MCLR(a) memset(a,-1,sizeof(a))
#define i64 __int64
#define eps 1e-11
#define inf (1<<29)
struct node{
	double val;
	string name;
	node *left,*right;
	node *par;
};
char a[10000],b[10000];
string arr[110];
int kk;
bool ase(string a)
{
	int i;
	for(i = 0;i<kk;i++)
		if(arr[i] == a)
			return true;
		return false;
}
map <string,bool> mp;
int main()
{
	//freopen("A-large.in","r",stdin);
	//freopen("a.out","w",stdout);
	int tc,	fg =1;
	cin>>tc;
	while(tc--)
	{
		int ln,i,j;
		cin>>ln;
		getchar();
		node *root = new node();
		root->par = NULL,root->left = NULL,root->right = NULL;
		node *now = root;
		bool flag = false;
		while(ln--)
		{
			gets(a);
			if(flag)
				continue;
			bool ch = false;
			for(i = 0;i<strlen(a);i++)
				if(a[i]!=' ' && a[i]!=')' && a[i]!=')')
				{
					ch = true;
					break;
				}
			if(!ch)
				continue;


			FOR(i,strlen(a))
				if(a[i] == '(')
					break;
				string p;
			for(j = i+1;j<strlen(a);j++)
				p+=a[j];
			strcpy(a,p.c_str());
			double vv;
			sscanf(a,"%lf %s",&vv,b);
			string tt = b;
			if(tt[0] == ')')
			{
				now->val = vv;
				now->left = now->right = NULL;
				if(now == root)
				{
					flag = true;
					continue;
				}
				if(now == now->par->left)
				{
					now->par->right = new node();
					node *tmp = now->par;
					now = now->par->right;
					now->par = tmp;
					now->left = now->right = NULL;
					
				}
				else
				{
					if(now!=root) now = now->par;
					while(now->right!=NULL)
					{
						if(now == root)
							break;
						now = now->par;
					}
					if(now != root ||(now == root && now->right == NULL))
					{
						if(now->right == NULL)
						{
							now->right = new node();
							node *tmp = now;
							now = now->right;
							now->par = tmp;
							now->left = now->right = NULL;
						}
					}
					else
						flag = true;
				}
				continue;		
			}
			else
			{
				if(b[strlen(b) - 1] == ')')
					b[strlen(b)- 1] = 0;
				tt = b;
				now->val = vv,now->name = tt;
				now->left = new node();
				node *tmp = now;
				now = now->left;
				now->par = tmp;
				now->left = now->right = NULL;
			}
			
			
		}
		printf("Case #%d:\n",fg++);
		int q;
		cin>>q;		
		while(q--)
		{
			mp.clear();
			string nn;
			cin>>nn>>kk;
			for(i = 0;i<110;i++)
				arr[i] = "";
		
			FOR(i,kk)
			{
				cin>>arr[i];
				mp[arr[i]] = true;
			}
			double res = 1.00;
			now = root;
			while(true)
			{
				if(now == NULL)
					break;
				res*=now->val;
				if(now->left == NULL && now->right == NULL)
					break;
				else if(mp[now->name])
					now = now->left;
				else
					now = now->right;

			}
			printf("%.6lf\n",res+eps);


		}


	}
	
	
	return 0;
}