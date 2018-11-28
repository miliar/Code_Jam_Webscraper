#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <stack>
#include <cmath>
#include <sstream>
#include <cstring>
using namespace std;

char teams[100][100];
double wp[100],owp[100],oowp[100],rpi[100];
int n;

void get_wp(int idx)
{
	int all=0,win=0;
	for(int i=0;i<n;i++){
		if(teams[idx][i]=='.')continue;
		if(teams[idx][i]=='1')win++;
		all++;
	}
	wp[idx]=(win/(double)all);
}

void get_owp(int idx){
	//cout<<idx<<"*******"<<endl;
	double avg=0,c=0;
	for(int i=0;i<n;i++){
		if(i==idx || teams[i][idx]=='.')continue;
		c++;
		int all=0,win=0;
		//cout<<i<<"^^^^^^^"<<endl;
		for(int j=0;j<n;j++){
			if(j==idx || teams[i][j]=='.')continue;
			if(teams[i][j]=='1')win++;
			all++;
		}
		avg+=win/(double)all;
	}
	owp[idx]=(avg/(double)c);
}

void get_oowp(int idx){
	//cout<<idx<<"&&&&&&&&&&&&&&&&&&&"<<endl;
	double sum=0;
	int all=0;
	for(int i=0;i<n;i++){
		if(i==idx || teams[idx][i]=='.')continue;
		sum+=owp[i];
		all++;
	}
	//cout<<sum<<"*******counter"<<all<<endl;
	oowp[idx]=(sum/(double)all);
}
void get_rpi(int i){
	double sum=0;
	//for(int i=0;i<n;i++){
		//if(i==idx)continue;
		sum=0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
		//cout<<sum<<"********"<<endl;
		rpi[i]=(sum);
	//}
}

int main()
{
	freopen("large.in","r",stdin);
	freopen("2.out","w",stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		cin>>n;
		string s;
		getline(cin,s);
		for(int j=0;j<n;j++){
			getline(cin,s);
			//cout<<s<<endl;
			for(int k=0;k<s.size();k++){
				teams[j][k]=s[k];
			}
			get_wp(j);
		}
		for(int j=0;j<n;j++)get_owp(j);

		for(int j=0;j<n;j++)get_oowp(j);
		//cout<<owp.size()<<endl;
		//for(int j=0;j<n;j++)cout<<oowp[j]<<endl;
		//cout<<"**********"<<endl;
		for(int j=0;j<n;j++)get_rpi(j);
		//for(int j=0;j<n;j++)cout<<rpi[j]<<endl;
		cout<<"Case #"<<i<<":\n";
		for(int j=0;j<n;j++)cout<<rpi[j]<<endl;
	}

	return 0;
}
