#include<iostream>
#include<algorithm>
#include<string>
#include<vector>

#include<cmath>
#include<cstdio>
#include<queue>
#include<list>
#include<stack>
#include<utility>
#include<numeric>
#include<map>
#include<cctype>
#include<cstring>
#include<sstream>

using namespace std;

#define F(a,b) for(int a=0;a<b;a++)
#define FOR(a,b,c) for(int a=b;a<c;a++)
#define FORD(a,b,c) for(int a=b;a>=c;a--)

#define s scanf
#define p printf

#define ALL(x) x.begin(), x.end()

#define INF 1000000000

struct BST
{
	double f;
	string prop;
	BST *left;
	BST *right;
};


int main()
{
	int t;
	int l;
	string total;
	BST root;
	BST *node,*nodetmp;
	int n;
	string str,tmp;
	s("%d",&t);
	stack<string> S;
	stack<BST> BS;
	F(tc,t)
	{
		s("%d",&l);	
			getline(cin,str);
		F(i,l)
		{
			getline(cin,str);
			tmp="";
			F(j,(int)str.length())
			{
				if(str[j]=='(')
				{
					S.push("(");
				}
				else if(str[j]==')')
				{
					if(tmp!="")
					{
						S.push(tmp);
						tmp="";
					}
					//node=(BST *)malloc(sizeof(BST));
					node=new BST;
					if(!isdigit(S.top()[0]))
					{
						node->prop=S.top();
						S.pop();
						istringstream is(S.top());
						S.pop();
						is>>(node->f);
					}
					else
					{
						node->prop="";
						istringstream is(S.top());
						S.pop();
						is>>(node->f);
					}
					if(node->prop!="")
					{
						nodetmp=new BST;
						nodetmp->f=BS.top().f;
						nodetmp->prop=BS.top().prop;
						nodetmp->left=BS.top().left;
						nodetmp->right=BS.top().right;
						node->right=nodetmp;
						BS.pop();

						nodetmp=new BST;
						nodetmp->f=BS.top().f;
						nodetmp->prop=BS.top().prop;
						nodetmp->left=BS.top().left;
						nodetmp->right=BS.top().right;
						node->left=nodetmp;
						BS.pop();
					}
					else
					{
						node->right=NULL;
						node->left=NULL;
					}
					BS.push(*node);
					S.pop();
				}
				else if(str[j]==' ' || str[j]=='\n')
				{
					if(tmp!="")
					S.push(tmp);
					tmp="";
				}
				else
				{
					tmp+=str[j];
				}
			}
			if(tmp!="")
			S.push(tmp);
		}

		s("%d",&l);
		BST *nn;
		p("Case #%d:\n",tc+1);
		F(i,l)
		{
			cin>>tmp;
			cin>>n;
			map<string,bool> M;
			F(j,n)
			{
				cin>>tmp;
				M[tmp]=true;
			}
			double ans=1;
			nn=&BS.top();
			while(nn!=NULL)
			{
				ans*=nn->f;
				if(M[nn->prop])
					nn=nn->left;
				else
					nn=nn->right;
			}
			p("%.7lf\n",ans);
		}
	}
	return 0;
}
