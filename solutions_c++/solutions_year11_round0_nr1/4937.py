#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <vector>
#include <string>
#include <list>
#include <set>
#include <map>
using namespace std;


int main()
{
	freopen("A-small-attempt2.in", "r", stdin); freopen("output.txt", "w", stdout);
	int n,t,k,a;
	char c;
	vector<pair<char,int>> sp[102];
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>n;
			for(int k=0;k<n;k++)
			{
				cin>>c>>a;
				sp[i].push_back(make_pair(c,a));
			}
	}
for(int i=0;i<t;i++)
	{
		int kol=0;
		int na1=1,na2=1;
		int l=0,r=0;
		int tmp=-1,tmp2=-1;
		int k=0,j=0;
		int p=0;
		int fl=0,fl2=0;
		while(p<sp[i].size())
		{
			
		for(k=l;k<sp[i].size();k++)
			{
				
				if (sp[i][k].first=='O') {if(tmp==-1) tmp=abs(na1-sp[i][k].second);break;}
			}
				for(j=r;j<sp[i].size();j++)
				{
					if (sp[i][j].first=='B') {if(tmp2==-1) tmp2=abs(na2-sp[i][j].second);break;}
				}
				
				if(k>j)
				{
					if ((tmp2-fl2)>=0)kol+=(tmp2-fl2);
					na2=sp[i][j].second;
					r=j+1;
					tmp-=(tmp2-fl2)+fl;
					fl2=0;
					fl=0;
					kol+=1;
					tmp-=1;
					if(tmp<=0) {if (k<sp[i].size() && sp[i][k].first=='O' && abs(k-j)==1) {tmp=-1;p++;kol+=1;l=k+1;fl2=1;na1=sp[i][k].second;}}
					tmp2=-1;
					p++;
					continue;
				}
				if(k<j)
				{
					if ((tmp-fl)>=0) kol+=(tmp-fl);
					na1=sp[i][k].second;
					l=k+1;
					tmp2-=(tmp-fl)+fl2;
					fl=0;
					fl2=0;
					kol+=1;
					tmp2-=1;
					tmp=-1;
					if(tmp2<=0) {if (j<sp[i].size() && sp[i][j].first=='B' && abs(k-j)==1) {tmp2=-1;p++;kol+=1;r=j+1;fl=1;na2=sp[i][j].second;}}
					
					p++;
					continue;
				}
				

					
		}
		cout<<"Case #"<<i+1<<": "<<kol<<endl;

				
			
	}
	

	return 0;
}


