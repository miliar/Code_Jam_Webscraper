#include <fstream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

#define ll long long

using namespace std;

ll gcd(ll a,ll b) {return (b==0) ? a : gcd(b,a%b);}
ll lcd(ll a,ll b) {return (a/gcd(a,b))*b;}

string operator - (string a,string b)
{
	reverse(a.begin(),a.end());
	reverse(b.begin(),b.end());
	string r;
	int l=max(a.size(),b.size());
	for(int i=0;i<l;i++)
	{
		long r=(i<b.size()) ? (b[i]-'0') : 0;
		a[i]-=r;
		if (a[i]<'0')
		{
			a[i]+=10;
			a[i+1]--;
		}
	}
	while(l>1&&a[--l]<='0') a.erase(a.end()-1);
	reverse(a.begin(),a.end());
	return a;
}


bool cmp(string a,string b)
{
	if (a.size()<b.size()) return true;
	if (a.size()>b.size()) return false;
	return a<b;
}

bool cmp1(string a,string b)
{
	if (a.size()<b.size()) return true;
	if (a.size()>b.size()) return false;
	return a<=b;
}

string operator %(string a,string b)
{
	while(cmp1(b,a))
	{
		string c=b;
		while(cmp1(c,a))
			c.push_back('0');
		c.erase(c.end()-1);
		a=a-c;
		/*if (cmp(a,b))
		{
			string tmp=a;
			a=b;
			b=tmp;
		}*/
	}
	return a;
}

string gcd_s(string a,string b)
{
	if (cmp(a,b))
	{
		string tmp=a;
		a=b;
		b=tmp;
	}
	while(b!="0")
	{
		string c=b;
		while(cmp1(c,a))
			c.push_back('0');
		c.erase(c.end()-1);
		a=a-c;
		if (cmp(a,b))
		{
			string tmp=a;
			a=b;
			b=tmp;
		}
	}
	return a;
}

int main()
{
	ifstream dat("input.txt");
	ofstream sol("output.txt");
	int t,n,k;
	dat >> t;
	for(int i=0;i<t;i++)
	{
		dat >> n;
		string nums[1001],g;
		for(int j=0;j<n;j++)
			dat >> nums[j];
		sort(&nums[0],&nums[n],cmp);
		g=nums[1]-nums[0];
		for(int j=2;j<n;j++)
			g=gcd_s(g,nums[j]-nums[j-1]);
		string G=nums[0]%g;
		sol << "Case #" << i+1 << ": " << g-(G=="0" ? g : G) << endl;
		/*ll nums[3]={0},g;
		for(int j=0;j<n;j++)
			dat >> nums[j];
		sort(&nums[0],&nums[n]);
		g=nums[1]-nums[0];
		if (n==3) g=gcd(g,nums[2]-nums[1]);
		sol << "Case #" << i+1 << ": " << g-(nums[0]%g==0 ? g : nums[0]%g) << endl;*/
	}
//	sol << gcd(26000000-11000000,11000000-6000000) << endl;
//	sol << gcd(26000000+4000000, gcd(11000000+4000000, 6000000+4000000)) << endl;
	return 0;
}
