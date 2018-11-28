#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

map <string,bool> mp;

int main()
{
//	freopen("A.in","r",stdin);freopen("A_output.txt","w",stdout);
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);

	int _kase,kase=0,total,n,m,i,j,l;
	string s1,s2;
	cin>>_kase;
	while( _kase-- )
	{
		mp.clear();
		cin>>n>>m;
		for(i=0;i<n;i++)
		{
			cin>>s1;
			s1+='/';
			l=s1.size();
			s2="/";
			for(j=1;j<l;j++)
			{
				if(s1[j]=='/')
				{
					if( !mp[s2] )
						mp[s2]=true;
				}
				s2+=s1[j];
			}
		}
		total=0;
		for(i=0;i<m;i++)
		{
			cin>>s1;
			s1+='/';
			l=s1.size();
			s2="/";
			for(j=1;j<l;j++)
			{
				if(s1[j]=='/')
				{
					if( !mp[s2] )
					{
						total++;
						//cout<<s2<<endl;
						mp[s2]=true;
					}
				}
				s2+=s1[j];
			}
		}

		printf("Case #%d: ",++kase);
		cout<<total<<endl;
	}
	return 0;
}