#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#define ll unsigned long long
#define pb push_back
using namespace std;

int find(vector<char> v, char c)
{
	for(ll i=0;i<v.size();i++)
		if (v.at(i)==c) return i;
	return -1;
}

int main()
{
	ll nc,cc,i,j,k,base,res;
	string inp;
	vector<char> vc;
	cin >> nc;
	for(cc=0;cc<nc;cc++)
	{
		cin >> inp;
		vc.clear();
		for(i=0;i<inp.length();i++)
			if(find(vc,inp[i])==-1)
				vc.pb(inp[i]);
		base = vc.size();
		
		if(base==1) { vc.pb('0'); base++; }
		
		k = vc.at(0);
		vc.at(0) = vc.at(1);
		vc.at(1) = k;
		
		//for(i=0;i<base;i++) cout << vc.at(i) << " "; cout << endl;
		
		res = 0;
		for(i=0;i<inp.size();i++)
		{
			res = res*base + find(vc,inp[i]);
		}
		
		cout << "Case #" << cc+1 << ": " << res << endl;
		inp.clear();
	}
}


