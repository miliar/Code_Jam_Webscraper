#define _CRT_SECURE_NO_DEPRECATE
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <ctime>
using namespace std;
#define pb push_back
#define ppb pop_back
#define mp make_pair
#define pi 2*acos(0.0)
#define mp make_pair
//#define x first
//#define y second
#define sqr(a) (a)*(a)
#define D(a,b) sqrt(((a).x-(b).x)*((a).x-(b).x)+((a).y-(b).y)*((a).y-(b).y))
#define pii pair<int,int>
#define pdd pair<double,double>
#define sz(c) (int)((c).size())
#define inf 1000000000
#define all(c) (c).begin(), (c).end()
#define vi vector<int>
#define vpii vector< pii >
#define vpdd vector< pdd >
#define L(s) (int)((s).end()-(s).begin())
#define ll long long
#define C(a,b) memset((a),(b),sizeof((a)))
bool u[100];
string s[100],q;
int i,n,rez,j,cnt,m,k,lst;
char ch;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>n;
	for(int cc=0;cc<n;cc++)
	{
		rez=0;
		lst=-1;
		cin>>m;
		scanf("%c",&ch);
		for(i=0;i<m;i++)
		{
			scanf("%c",&ch);
			s[i]="";
			while(ch!='\n')
			{
				s[i]+=ch;
				scanf("%c",&ch);
			}
		}
		cin>>k;
		scanf("%c",&ch);
		for(i=0;i<k;)
		{
			cnt=0;
			C(u,0);
			if (lst!=-1)
			{
				u[lst]=true;
				cnt=1;
			}
			while(i<k&&cnt<m)
			{
					scanf("%c",&ch);
					q="";
					while(ch!='\n')
					{
						q+=ch;
						scanf("%c",&ch);
					}
					j=0;
					while(j<m&&s[j]!=q)
						j++;
					if (j<m)
					{
						if (!u[j])
						{
							u[j]=true;
							cnt++;
							lst=j;
						}
					}
					i++;
			}
			if (cnt==m)
				rez++;
		}
		cout<<"Case #"<<cc+1<<": "<<rez<<endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}