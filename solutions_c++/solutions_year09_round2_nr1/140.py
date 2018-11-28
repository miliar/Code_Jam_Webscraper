#include <algorithm>
#include <cmath>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>

using namespace std;

#define fore(i,a) for(int i = 0; i < (a); i++)
#define fort(i,a) for(typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define x first
#define y second

typedef pair<int,int> pi;
typedef vector<int> vi;
typedef long long ll;

#define err(...)
#define err(...) fprintf(stderr, __VA_ARGS__)

int posx,posy, L, A;
char buf[111][88];
set<string> animal;
set<char> av;
char feature[11];

char get()
{
	while(av.find(buf[posx][posy]) == av.end())
	{
		if(buf[posx][posy] == 0)
		{
			posx++;
			posy = 0;
		}
		else posy++;
	}
	//printf("return %c (%d)\n", buf[posx][posy], buf[posx][posy]);
	return buf[posx][posy++];
}

struct node
{
	node * left;
	node * right;
	char name[11];
	int len;
	double num, pww;
	node()
	{
		left = NULL;
		right = NULL;
		//printf("init %d %d\n", posx, posy);
		char c;
		int h = 0;
		pww = .1;
		num = 0;
		len = 0;
		for(c = get(); c != ')' && c != '('; c = get())
		{
			if(h < 2)
			{
				if(c == '1') num = 1;
				h++;
			}
			else if(c != ' ')
			{
				//printf("h = %d\n", h);
				if(c < 'a' || c > 'z')
				{
					num = num + pww * (c - '0');
					pww /= 10.;
				}
				else
				{
					name[len++] = c;
				}
			}
		}
		name[len] = 0;
		if(c == ')') return;
		left = new node();
		get();
		right = new node();
		get();
		//printf("koniec %s\n", name);
	}
	~node()
	{
		if(left != NULL) delete left;
		if(right != NULL) delete right;
	}
	double cute()
	{
		double res = num;
		//printf("res = %lf\n", res);
		if(len == 0) return res;
		if(animal.find(name) != animal.end()) res *= left -> cute();
		else res *= right -> cute();
		return res;
	}
};

node * root;


void test()
{
	scanf("%d", &L);
	fore(i,L) scanf(" %[^\n]", buf[i]);
	posx = posy = 0;
	get();
	root = new node();
	scanf("%d", &A);
	fore(i,A)
	{
		animal.clear();
		int N;
		scanf(" %*s%d", &N);
		fore(j,N)
		{
			scanf(" %s", feature);
			animal.insert(feature);
		}
		printf("%.7lf\n", root -> cute());
	}
	delete root;
}

int main()
{
	fore(i,10) av.insert('0'+i);
	fore(i,26) av.insert('a'+i);
	av.insert('.');
	av.insert('(');
	av.insert(')');
	int T;
	scanf("%d", &T);
	for(int tt = 1; tt <= T; tt++)
	{
		printf("Case #%d:\n", tt);
		test();
	}
}
