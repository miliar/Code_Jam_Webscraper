// Fair Warning(gcj2010).cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;
string a[1001];
string d[1001];
int cmp(const void * a,const void *b)
{
	string s1=*(static_cast<const string *>(a));
	string s2=*(static_cast<const string *>(b));
	if(s1.length()>s2.length())
		return 1;
	else if(s1.length()<s2.length())
		return -1;
	else
	{
		for(int i=0;i<s1.length();i++)
		{
			if(s1[i]>s2[i])
				return 1;
			else if(s1[i]<s2[i])
				return -1;
		}
		return 0;
	}
}

string sub(string s1,string s2)
{
	int l1=s1.length(),l2=s2.length();
	string s;
	int b=0;
	for(int i=1;i<=l2;i++)
	{
		if(s1[l1-i]-s2[l2-i]-b<0)
		{
			s.push_back(s1[l1-i]-s2[l2-i]-b+10+'0');
			b=1;
		}
		else
		{
			s.push_back(s1[l1-i]-s2[l2-i]-b+'0');
			b=0;
		}
	}
	for(int i=l1-l2-1;i>=0;i--)
	{
		if(s1[i]-'0'-b<0)
		{
			s.push_back(10+s1[i]-b);
			b=1;
		}
		else
		{
			s.push_back(s1[i]-b);
			b=0;
		}
	}
	//delete 0
	int zp=-1;
	for(int i=s.length()-1;i>=0;i--)
	{
		if(s[i]=='0')
			zp=i;
		else
			break;
	}
	if(zp!=-1)
		s.erase(zp);
	l1=s.length();
	char t;
	for(int i=0;i<l1/2;i++)
	{
		t=s[i];
		s[i]=s[l1-i-1];
		s[l1-i-1]=t;
	}
	if(s=="")
		s="0";
	return s;
}
string getmod(string s1,string s2)
{
	string tmp=s2;
	while(1)
	{
		if(cmp(&s1,&s2)<0)
			return s1;
		else
		{
			int d;
			while(1)
			{
				d=s1.length()-s2.length();
				if(cmp(&s1,&s2)<0)
					break;
				tmp=s2;
				for(int i=0;i<d;i++)
				{
					tmp.push_back('0');
				}
				if(cmp(&tmp,&s1)>0)
				{
					tmp.erase(tmp.length()-1);
				}
				s1=sub(s1,tmp);//s1与s2在10倍以内
			}
			return s1;
		}
	}
	return "";
}
string gcd(string s1,string s2)
{
	if(s2=="0")
		return s1;
	return gcd(s2,getmod(s1,s2));
}

int main()
{
	int ts,n;
	string min,gmax,mods;
	ifstream f("d:\\gcj\\B-large.in");
	ofstream of("d:\\gcj\\A-small.out");
	if(f!=NULL)
	{
		f>>ts;
		for(int t=1;t<=ts;t++)
		{
			f>>n;
			for(int i=0;i<n;i++)
				f>>a[i];
			qsort(a,n,sizeof(a[0]),cmp);
			for(int i=0;i<n-1;i++)
				d[i]=sub(a[i+1],a[i]);

			min="10000000000000000000000000000000000000000000000000000000000";
			if(n==2)
				min=d[0];
			gmax=d[0];
			for(int i=1;i<n-1;i++)	
			{
				if(d[i]=="0")
					continue;
					gmax=gcd(d[i],gmax);
					if(cmp(&gmax,&min)<0)
						min=gmax;
			}
			mods=getmod(a[0],min);
			if(mods!="0")
			{
				mods=sub(min,mods);
			    of<<"Case #"<<t<<": "<<mods<<endl;
			}
			else
			  of<<"Case #"<<t<<": "<<"0"<<endl;
		}
	}
	return 0;
}

