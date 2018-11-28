#define mset(a) memset(a,0,sizeof(a))

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;
int mat[200][200];
double wp1[200],wp2[200],owp[200],oowp[200];
int main()
{
	int t;
cin >>t;
for(int tt=1;tt<=t;tt++)
{
	mset(mat);
	mset(wp1);mset(wp2);mset(owp);mset(oowp);
	cout<<"Case #"<<tt<<":"<<endl;
	int n;string s;
	cin>>n;
	for(int i=0;i<n;i++)
	{
		cin>>s;
		int a=0,b=0;
		for(int j=0;j<n;j++)
		{
			if(s[j]=='1'){mat[i][j]=1;a++;b++;}
			if(s[j]=='0'){mat[i][j]=-1;b++;}
		}
		wp1[i]=a;
		wp2[i]=b;
	}
	for(int i=0;i<n;i++)
	{
		owp[i]=0.0;
		for(int j=0;j<n;j++)
			if(mat[i][j]==-1)
			{
				
				owp[i]+=(double)(wp1[j]-1)/(wp2[j]-1);
			}
			else if(mat[i][j]==1)
			{
				owp[i]+=(double)(wp1[j])/(wp2[j]-1);
			}
		owp[i]=owp[i]/wp2[i];
		//cout<<owp[i]<<"asd"<<endl;
	}	
	for(int i=0;i<n;i++)
	{
		oowp[i]=0.0;int p=0;
		for(int j=0;j<n;j++)
			if(mat[i][j]!=0)
			{
				oowp[i]+=owp[j];
				p++;
			}
		oowp[i]/=p;
	}
	for(int i=0;i<n;i++)
		cout<<wp1[i]/wp2[i]*0.25+owp[i]*0.5+oowp[i]*0.25<<endl;
	//cout <<wp1[i]/wp2[i]<<" "<<owp[i]<<" "<<oowp[i]<<endl;
}
return 0;
}
