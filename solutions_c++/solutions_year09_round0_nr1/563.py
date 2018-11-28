
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
struct pattern{
	vector<vector<bool> > pos;
	pattern(int n,const string& pat){
		pos.resize(n);
		for(int i=0;i<n;i++)
			pos[i].resize(26,false);
		int idx = 0;
		for(int i=0;i<pat.size();i++)
		{
			if(pat[i] != '(')
			{
				pos[idx][pat[i] - 'a'] = true;
				idx++;
			}
			else
			{
				i++;
				while(pat[i] != ')')
				{
					pos[idx][pat[i] - 'a'] = true;
					i++;
				}
				idx++;
			}
		}
	}
	bool match(const string & word)
	{
		for(int i=0;i<word.size();i++)
		{
			if(pos[i][word[i]-'a'] == false)
				return false;
		}
		return true;
	}
};
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int n,k,nt;
	cin>>n>>k>>nt;
	vector<string> words(k);
	for(int i=0;i<k;i++)
		cin>>words[i];
	for(int it=1;it<=nt;it++)
	{
		string patt;
		cin>>patt;
		pattern P(n,patt);
		int num = 0;
		for(int i=0;i<words.size();i++)
			if(P.match(words[i]))
				num++;
		cout<<"Case #"<<it<<": "<<num<<endl;
	}
	return 0;
}
