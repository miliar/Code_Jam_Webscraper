#include <iostream>
#include <string>
#include <algorithm>
#include <fstream>

using namespace std;

string num[1001];
string sub[1001];
int k;
bool mysort(const string &s1,const string &s2)
{
	return s1.length()<s2.length() || (s1.length()==s2.length()&& s1<s2);
}

string cut(const string &s1,const string &s2)
{
	string s;
	s=s1;
	int temp;
	int l2=s2.length()-1;
	int l1=s1.length()-1;
	l1-=l2;
	for (;l2>=0;l2--)
	{
		s[l1+l2]=s[l1+l2]-s2[l2];
		temp=l1+l2;
		s[l1+l2]+='0';
		while (s[temp]<'0')
		{
			s[temp-1]--;
			s[temp]+=10;
			temp--;
		}
	}
	while  (s[0]=='0' && s.length()>1) 
		s=&s[1];
	return s;
}

string gcd(const string &s1,const string &s2)
{
	if (s1[0]<'0'||s1[0]>'9')
	{
			k=1;
			;
		}
	string s;
	bool ifok;
	int l1=s1.length();
	int l2=s2.length();
	s=s2;
	for (int x=0;x<l2-l1+1;x++)
	{
		ifok=false;
		while (!ifok)
		{
			for (int y=l1-1;y>=0;y--)
			{
				s[x+y]-=s1[y];
				if (y!=0&&s[x+y]<0) 
				{
					s[x+y-1]--;
					s[x+y]+=10;
				}
				s[x+y]+='0';
			}
			if (s[x]<'0') 
			{
				if (x>0&&s[x-1]>'0')
				{
					s[x-1]--;
					s[x]+=10;
					continue;
				}
				ifok=true;
			}
		}
		for (int y=l1-1;y>=0;y--)
		{
			s[x+y]+=s1[y]-'0';
			if (s[x+y]>'9')
			{
				s[x+y]-=10;
				s[x+y-1]++;
			}
		}
	}
	while (s[0]=='0' && s.length()>1) s=&s[1];
	if (s=="0") return s1;
	else return gcd(s,s1);
}

string gcd2(const string &s1,const string &s2)
{
	string s;
	bool ifok;
	int l1=s1.length();
	int l2=s2.length();
	s=s2;
	for (int x=0;x<l2-l1+1;x++)
	{
		ifok=false;
		while (!ifok)
		{
			for (int y=l1-1;y>=0;y--)
			{
				s[x+y]-=s1[y];
				if (y!=0&&s[x+y]<0) 
				{
					s[x+y-1]--;
					s[x+y]+=10;
				}
				s[x+y]+='0';
			}
			if (s[x]<'0') 
			{
				if (x>0&&s[x-1]>'0')
				{
					s[x-1]--;
					s[x]+=10;
					continue;
				}
				ifok=true;
			}
		}
		for (int y=l1-1;y>=0;y--)
		{
			s[x+y]+=s1[y]-'0';
			if (s[x+y]>'9')
			{
				s[x+y]-=10;
				s[x+y-1]++;
			}
		}
	}
	while (s[0]=='0' && s.length()>1) s=&s[1];
	return s;
}


int main()
{
	int n,c,tempi;
	string ans,temp;
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	fin>>c;
	for (int i=0;i<c;i++)
	{
		fin>>n;
		for (int j=0;j<n;j++)
			fin>>num[j];
		sort(num,num+n,mysort);
		for (int j=1;j<n;j++)
			sub[j-1]=cut(num[j],num[j-1]);
		sort(sub,sub+n-1,mysort);
        tempi=0;
		ans=sub[tempi];
		while (sub[tempi]=="0"&&tempi<n-2)
		{
			tempi++;
			ans=sub[tempi];
		}
		for (int j=tempi+1;j<n-1;j++)
		ans=gcd(ans,sub[j]);
		temp=ans;
		ans=gcd2(ans,num[n-1]);
		if (ans!="0")
		ans=cut(temp,ans);
		fout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	return 0;
}