#include<iostream>
#include<string.h>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<deque>
#include<set>
#include<stack>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<cassert>
#define CLRM(x) memset(x,-1,sizeof(x))
#define CLR(x) memset(x,0,sizeof(x))
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define MP make_pair
#define VI vector<int> 
#define VVI vector<vector<int> >
#define PII pair<int,int>
#define SZ(x) (int)x.size()
#define LL unsigned long long
#define MIN(a,b) (a)<(b)?(a):(b)
#define MAX(a,b) (a)>(b)?(a):(b)
#define LMAX 1000000000000000000LL
#define IMAX 100000000

#define GI(x) scanf("%d", &x)

using namespace std;
int depth;
struct node
{
	double prob;
	char feat[110];
	int isfeat;
	node *left, *right;
};
node *root;

node* foo(int vis)
{
	char c;
	double d;
	if(!vis)
	{
		do
		{
			cin >> c;
		}while(c != '(');
	}
	depth += 1;
	node* tp = (node*)malloc(sizeof(node));
	cin >> d;
	//cout << "hi " << d << endl;
	do
	{
		cin >> c;
	}while(!(c == ')' || isalpha(c)));
	char cx = c;
	tp -> prob = d;
	//cout << "go " << tp -> prob << " " << c << endl;
	if(c == ')')
	{
		tp -> isfeat = 0;
		tp -> left = NULL;
		tp -> right = NULL;
	}
	else
	{
		string tx;
		tx.PB(c);
		string tp1;
				
		while(1)
		{
			cin>>c;
			if(!isalpha(c))
				break;
			tp1.PB(c);
		}
		int vis = 0;
		if(c == '(')
		vis = 1;
		//cout << tp1<<endl;
		tx += tp1;
		//tp -> feat = new string(tx);
		strcpy(tp -> feat, tx.c_str());
		//cout<<" so " << tp->feat<<endl;
		tp -> isfeat = 1;
		tp -> left = foo(vis);
		tp -> right = foo(0);
		
	}
	//cout << "notdone " << (tp->isfeat?tp->feat:"none") << endl;
	if(cx != ')')
	{
		do
		{
			cin >> c;
		}while(c != ')');
	}

	depth -= 1;
	//cout << "done " << (tp->isfeat?tp->feat:"none") << endl;
	return tp;
}	
void preprocess()
{
	depth = 0;
	root = foo(0);
}
void disp1(node* ptr)
{
	cout << ptr -> prob << endl;
	if(ptr -> isfeat)
	{
		cout << ptr -> feat << endl;
		disp1(ptr -> left);
		disp1(ptr -> right);
	}
}	
void solve()
{
	int n;
	cin >> n;
	int i, j, k;
	string animal;
	string tp11;
	for(i = 0; i < n; i++)
	{
		double proba = 1;
		vector<string> features;
		map<string, int> m;
		cin >> animal;
		int fnum;
		cin >> fnum;
		for(j = 0; j < fnum; j++)
		{
			cin >> tp11;
			features.PB(tp11);
			m[tp11] = 1;
		}
		node *ptr = root;
		while(1)
		{
			proba *= ptr -> prob;
			if(!ptr -> isfeat)
				break;
			string x(ptr -> feat);
			if(m.find(x) != m.end())
			{
				ptr = ptr->left;
			}
			else
			{
				ptr = ptr->right;
			}
		}
		printf("%0.8lf\n", proba);
	}
}
int main()
{
	int tes;
	cin >> tes;
	int i, j, k;
	for(int t = 1; t<= tes; t++)
	{
		printf("Case #%d:\n", t);
		free(root);
		preprocess();
		//cout<<"**************"<<endl;
		//disp1(root);
		solve();
	}
	return 0;
}
