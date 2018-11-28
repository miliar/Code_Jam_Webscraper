#include <vector>
#include <string>
#include <iostream>
#include <memory.h>
#include <algorithm>
#include <stack>
#include <fstream>
#include <sstream>
#include <cstdio>

using namespace std;


#define All(v) (v).begin(), (v).end()
#define ffor(i,n) for(int i=0; i<n; i++)
#define LL long long
#define LD long double
#define psh push_back
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))


struct node
{
	string feat;
	double w;
	vector<node> sub;
};

void print(node p, int d)
{
	cout << "D: " << d;
	cout << " W: "  << p.w;
	cout << " F: " << p.feat;
	cout << " subt: " << p.sub.size() << endl;
	ffor(i,p.sub.size())
		print(p.sub[i],d+1);
}

void parse(node &n, string s)
{
	//cout << s << endl;
	//node data

	int st	= s.find_first_of('(');
	int en	= s.find_first_of('(',st+1);

	int l;
	if(en == -1)
		l	= s.find_first_of(')')-1;
	else
		l	= en-1;

	string t	= s.substr(st+1,l-st);
	//cout << "top:" << t;

	stringstream str(t);

	str >> n.w;
	str >> n.feat;

	//subtrees

	
	if(en	== -1)
		return;

		st	= en;
	for(;;)
	{

		//st = location of (, find complememtary )


		//cout << "st: " << st << endl;
		int cnt	= 1;
		int j = st+1;
		for(;j < s.size(); j++)
		{
			//cout << s[j] << endl;
			if(s[j] == ')')
				cnt--;
			if(cnt == 0)
				break;
			if(s[j] == '(')
				cnt++;
		}
		
		if(cnt != 0)
			break;

		//cout << "j: " << j << endl;
		node p;
		parse(p,s.substr(st-1,j-st+2));
		n.sub.psh(p);

		st	= j+2;
	}

}

double anal(node &p, const vector<string> &f)
{
	double res	= p.w;
	if(p.sub.size() == 0)
		return res;
	else
	{
		ffor(i,f.size())
			if(f[i] == p.feat)
				return res*anal(p.sub[0],f);
	}
				return res*anal(p.sub[1],f);
}

int main()
{
	int c;
	cin >> c;

	for(int i = 0; i < c; i++)
	{
		node root;
		int l;
		cin >> l;

		string t,code;
		getline(cin,t);

		ffor(j,l)
		{
			getline(cin,t);
			code += t;
		}
		parse(root,code);


		int an;
		cin >> an;

	
		//print(root,0);

		cout << "Case #" << i+1 << ": " << endl;
		ffor(j,an)
		{

			vector <string> feat;
			string name;
			cin >> name;
			int ft;
			cin >> ft;

			ffor(k,ft)
			{
				string temp;
				cin >> temp;
				feat.psh(temp);
			}

		printf("%.7f\n",anal(root,feat));

		}
				
	//	print(root,0);
		

	}
}
