
#define _CRT_SECURE_NO_DEPRECATE
#include <iostream> 
#include <string>
#include <vector>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <math.h>
#include <stack>
#include <deque>
#include <numeric>
#define all(x) x.begin(),x.end()
#define mpair make_pair
using namespace std;
typedef long long ll;
typedef long double ld;
const ld epsylon = 1e-9;
struct node{
	ld weight;
	string feature;
	vector<node> subs;
	node(){
		feature = "";
	}
};
node getTree(const string& given,int from ,int to)
{
	int lbr = -1,rbr;
	for(int i=from;i<=to;i++)
	{
		if(given[i]== '(')
		{
			lbr = i;
			break;
		}
	}
	node res;
	if(lbr== -1)
	{
		istringstream in(given.substr(from,to-from+1));
		in>>res.weight;
		return res;
	}
	istringstream in(given.substr(from,lbr - from));
	in>>res.weight>>res.feature;
	int opened = 1;
	for(int i=lbr +1;i<to;i++)
	{
		if(given[i] == '(')
		{
			opened ++;
		}
		else if(given[i] == ')')
		{
			opened--;
			if(opened == 0)
			{
				rbr = i;
				break;
			}
		}
	}
	res.subs.push_back(getTree(given,lbr+1,rbr-1));
	for(int i=rbr+1;i<to;i++)
	{
		if(given[i] =='(')
		{
			lbr = i;
			break;
		}
	}
	opened = 1;
	for(int i=lbr +1;i<to;i++)
	{
		if(given[i] == '(')
		{
			opened ++;
		}
		else if(given[i] == ')')
		{
			opened--;
			if(opened == 0)
			{
				rbr = i;
				break;
			}
		}
	}
	res.subs.push_back(getTree(given,lbr+1,rbr-1));
	return res;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int nt;
	cin>>nt;
	for(int it=1;it<=nt;it++)
	{
		string given;
		int n;
		string temp;
		cin>>n;
		getline(cin,temp);
		for(int i=0;i<n;i++)
		{
			getline(cin,temp);
			given = given + " " + temp; 
		}
		int lbr =0 ;
		while(given[lbr]!= '(') lbr++;
		int rbr = (int)given.size() -1;
		while(given[rbr] != ')' ) rbr --;
		node tree = getTree(given,lbr+1,rbr-1);
		int m;
		cin>>m;
		getline(cin,temp);
		cout<<"Case #"<<it<<":"<<endl;
		for(int i=0;i<m;i++)
		{
			getline(cin,temp);
			istringstream in(temp);
			string name;
			in>>temp;
			int k;
			in>>k;
			set<string> fs;
			for(int i=0;i<k;i++)
			{
				in>>temp;
				fs.insert(temp);
			}
			node *cur  = &tree;
			ld res = 1.0;
			while(cur->subs.size() > 0)
			{
				res = res* cur->weight;
				if(fs.find(cur->feature) != fs.end())
				{
					cur = &cur->subs[0];
				}
				else
				{
					cur = &cur->subs[1];
				}
			}
			res*= cur->weight;
			printf("%.8llf\n",res);
		}
	}
	return 0;
}
