#include<iostream>
#include<algorithm>
#include<fstream>
#include<vector>
#include<conio.h>
#include<stdlib.h>
#include<string>
using namespace std;
int vecTostr(vector<int> a)
{
	int sum=0;
	int ten=1;
	for(int i=0; i<(int)a.size(); i++)
	{
		sum=(sum*10)+ a[i];
	}
	return sum;
}
void  seprt(int n,vector<int> & a)
{
	while(n>0)
	{
		a.push_back(n%10);
		n=n/10;
	}
	reverse(a.begin(),a.end());
}
int cdigit(int n)
{
	int k=0;
	while(n>0)
	{
		k++;
		n=n/10;
	}
	return k;
}
bool match(vector<int> v,int n)
{
	for(int i=0; i<(int)v.size(); i++)
	{
		if(v[i]==n)
		{
			return true;
		}
	}
	return false;
}
void per(vector<int> s,vector<int> & ne,int st)
{
	int i=0;
	int a=0;
	for(i=st; i<(int)s.size(); i++)
	{
		ne[a]=s[i];
		a++;
	}
	i=0;
	for(;a<(int)s.size(); i++)
	{
		ne[a]=s[i];
		a++;
	}
}
void main()
{
	ifstream in("C-small-attempt0.in");
	ofstream out("out.txt");
	int T;
	in>>T;
	vector <int> s;
	vector<int>x;
	for(int i=0; i<T; i++)
	{
		int A,B;
		in>>A>>B;
		int total=0;
		for(int j=A ; j<B; j++)
		{
			seprt(j,s);
			int h=0;
			for(int k=0; k<(int)s.size(); k++)
			{
				vector <int>s1(s.begin(),s.end());
				per(s,s1,k);
				if(s1[0]!=0)
				{
					int sum=vecTostr(s1);
					if(sum>A && sum>j && sum<=B)
					{
						if(!match(x,sum))
						{
							total++;
							x.push_back(sum);
						}
					}
				}
			}
			x.clear();
			s.clear();
		
		}
		out<<"Case #"<<i+1<<": "<<total;
		if(i+1<T)
		{
			out<<endl;
		}
		s.clear();
	}
}