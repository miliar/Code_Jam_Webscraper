#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <bitset>
#include <functional>
#include <utility>//pair
#include <iomanip>

using namespace std;

#define dbg(x) cerr<<#x<<" : "<<x<<endl;
#define inf (1<<30)
#define PB push_back
#define MP make_pair
#define mset(x, a) memset(x, (a), sizeof(x))
typedef long long LL;
const double PI = acos(-1.0);
const double eps = 1e-8;
const int INF = 0x3f3f3f3f;

int main(int argc, char *argv[])
{
	freopen("B-small-attempt4.in","r",stdin);
    freopen("B-small-attempt4.out","w",stdout);
	int n;
	cin>>n;
	for(int k=1;k<=n;k++)
	{
		int c,d,m;
		string s1,s2,s3;
		string::iterator iter;
		cin>>c;
		if(c==1)
			cin>>s1;
		cin>>d;
		if(d==1)
			cin>>s2;
		cin>>m;
		cin>>s3;
		if(c==0 && d==0)
		{
			cout<<"Case #"<<k<<":"<<" [";
			for(int j=0;j<m;j++)
			{
				if(j!=m-1)
					cout<<s3[j]<<", ";
				else
					cout<<s3[j]<<"]"<<endl;
			}
		}
		if(c==1&&d==0)
		{
			for(int i=0;i<s3.size();i++)
			{
				if( (s3[i]==s1[0]&&s3[i+1]==s1[1]) || (s3[i]==s1[1]&&s3[i+1]==s1[0]))
				{	
					s3.erase(i,2);
					s3.insert(i,s1);
					s3.erase(i,2);
					i--;
				}
			}
			cout<<"Case #"<<k<<":"<<" [";
			for(int j=0;j<s3.size();j++)
			{
				if(j!=s3.size()-1)
					cout<<s3[j]<<", ";
				else
					cout<<s3[j]<<"]"<<endl;
			}
		}
		if(c==0&&d==1)
		{
			int i,j;
			while(1)
			{
				if(s3.find(s2[0])!=string::npos && s3.find(s2[1])!=string::npos)
				{
					i=s3.find(s2[0]);
					j=s3.find(s2[1]);
					if(i>j)
						swap(i,j);
					s3.erase(0,j+1);
				}
				else
					break;
			}
			cout<<"Case #"<<k<<":"<<" [";
			for(int j=0;j<s3.size();j++)
			{
				if(j!=s3.size()-1)
					cout<<s3[j]<<", ";
				else
					cout<<s3[j]<<"]"<<endl;
			}
			if(s3.empty())
				cout<<"]"<<endl;
		}
		if(c==1&&d==1)
		{
			int i,j;
			while(1)
			{
				if(s3.find(s2[0])!=string::npos && s3.find(s2[1])!=string::npos)
				{
					i=s3.find(s2[0]);
					j=s3.find(s2[1]);
	
					if(i>j)
						swap(i,j);
			
					if( (s3[i]==s1[0]&&s3[i+1]==s1[1]) || (s3[i]==s1[1]&&s3[i+1]==s1[0]) || (s3[j]==s1[0]&&s3[j-1]==s1[1]) || (s3[j]==s1[1]&&s3[j-1]==s1[0]) ||  (s3[i-1]==s1[0]&&s3[i]==s1[1]) || (s3[i-1]==s1[1]&&s3[i]==s1[0]))
					{	
						if( (s3[i]==s1[0]&&s3[i+1]==s1[1]) || (s3[i]==s1[1]&&s3[i+1]==s1[0]) )
						{
							s3.erase(i,2);
							s3.insert(i,s1);
							s3.erase(i,2);
						}
						if((s3[j]==s1[0]&&s3[j-1]==s1[1]) || (s3[j]==s1[1]&&s3[j-1]==s1[0]) )
						{
							s3.erase(j-1,2);
							s3.insert(j-1,s1);
							s3.erase(j-1,2);
						}
						if( (s3[i-1]==s1[0]&&s3[i]==s1[1]) || (s3[i-1]==s1[1]&&s3[i]==s1[0]) )
						{	
							s3.erase(i-1,2);
							s3.insert(i-1,s1);
							s3.erase(i-1,2);
						}
					}
					else
						s3.erase(0,j+1);
				}
				else
					break;
			}
			for(int i=0;i<s3.size();i++)
			{
				if( (s3[i]==s1[0]&&s3[i+1]==s1[1]) || (s3[i]==s1[1]&&s3[i+1]==s1[0]))
				{	
					s3.erase(i,2);
					s3.insert(i,s1);
					s3.erase(i,2);
					i--;
				}
			}
			cout<<"Case #"<<k<<":"<<" [";
			for(int j=0;j<s3.size();j++)
			{
				if(j!=s3.size()-1)
					cout<<s3[j]<<", ";
				else
					cout<<s3[j]<<"]"<<endl;
			}
			if(s3.empty())
				cout<<"]"<<endl;
		}

	}

	return 0;
}

