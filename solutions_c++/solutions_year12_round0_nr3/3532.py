#include<iostream>
#include<vector>
#include<sstream>
#include<string>
using namespace std;

int len(int a)
{
	stringstream ss;
	ss << a;
	string s;
	ss >> s;
	return s.length();
}
long long obl(string s, vector<bool> &odw, int mini, int maks,int dl)
{
	int a;
	stringstream ss(s);
	ss>>a;
	if(odw[a]==1)return 0;
	int zm = 1;
	if(len(a) != dl)zm = 0;
	if(a<mini || a > maks)zm = 0;
	odw[a] = 1;
	
	string s2 = s.substr(1).append(1,s[0]);
//	cout<<s<<" -> "<<s2<<endl;
	long long res = obl(s2,odw,mini,maks,dl)+zm;
//	cout<<a<<": "<<res<<endl;
	return res;
}
long long obl(int a, vector<bool> &odw, int mini, int maks,int zer)
{
	stringstream ss;
	ss << a;
	string s;
	ss >> s;
	return obl(s,odw,mini,maks,zer);
}
void solve(int num)
{
	int A,B;
	long long res = 0;
	cin>>A>>B;
	vector<bool>odw(10000000,0);
	for(int i=A;i<=B;i++)
	{
		if(odw[i])continue;
		long long k = obl(i,odw,A,B,len(i));
		k--;
		//cout<<i<<": "<<k<<endl;
		if(k%2==0)res+= k/2LL *(k+1LL);
		else res+= (k+1LL)/2LL * k;
	}
	cout<<"Case #"<<num<<": "<<res<<endl;	
}
int main()
{
	
	int t;
	cin>>t;
	for(int i=0;i<t;i++)solve(i+1);
	
}