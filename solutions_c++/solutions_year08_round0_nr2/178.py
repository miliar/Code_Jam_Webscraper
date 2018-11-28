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
vector<int> st,tm;
int stc[3],rez[3];
int n,m,i,j,k,t,cnt;
int stm[200],ftm[200],stn[200];
string h;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>cnt;
	for(int cc=0;cc<cnt;cc++)
	{
	cin>>t;
	cin>>n>>m;
	for(i=0;i<n;i++)
	{
		cin>>h;
		stm[i]=(int)(h[0]-'0')*600+int(h[1]-'0')*60+(int)(h[3]-'0')*10+(int)(h[4]-'0');
		cin>>h;
		ftm[i]=(int)(h[0]-'0')*600+int(h[1]-'0')*60+(int)(h[3]-'0')*10+(int)(h[4]-'0');
		stn[i]=1;
	}
	for(i=0;i<m;i++)
	{
		cin>>h;
		stm[n+i]=(int)(h[0]-'0')*600+int(h[1]-'0')*60+(int)(h[3]-'0')*10+(int)(h[4]-'0');
		cin>>h;
		ftm[n+i]=(int)(h[0]-'0')*600+int(h[1]-'0')*60+(int)(h[3]-'0')*10+(int)(h[4]-'0');
		stn[n+i]=2;
	}
	stc[1]=0;
	stc[2]=0;
	rez[1]=0;
	rez[2]=0;
	for(i=0;i<n+m;i++)
		for(j=i+1;j<n+m;j++)
			if (stm[i]>stm[j])
			{
				swap(stm[i],stm[j]);
				swap(ftm[i],ftm[j]);
				swap(stn[i],stn[j]);
			}
	st.clear();
	tm.clear();
	for(k=0;k<n+m;k++)
	{
		for(i=0;i<L(st);)
			if (st[i]==stn[k]&&stm[k]>=tm[i])
			{
				stc[st[i]]++;
				st.erase(st.begin()+i);
				tm.erase(tm.begin()+i);
			}
			else
				i++;
		if (stc[stn[k]]==0)
		{
			stc[stn[k]]++;
			rez[stn[k]]++;
		}
		stc[stn[k]]--;
		st.pb(3-stn[k]);
		tm.pb(ftm[k]+t);
	}
	cout<<"Case #"<<cc+1<<": "<<rez[1]<<" "<<rez[2]<<endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}