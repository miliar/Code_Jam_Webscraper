#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <cmath>
#include <vector>
#include <iostream>
#include <cctype>
#include <algorithm>
using namespace std;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;
	cin>>test;
	for (int t = 1 ; t <= test ; t++){
		cout<<"Case #"<<t<<": ";
		int n;
		cin>>n;
		string s;
		int d;
		vector<vector<pair<int,int> > > mas(2);
		for (int i=0;i<n;i++){
			cin>>s>>d;
			if (s=="O")
				mas[0].push_back(make_pair(d,i));
			else
				mas[1].push_back(make_pair(d,i));
		}
		for (int i=0;i<2;i++)
			reverse(mas[i].begin(),mas[i].end());
		int pos[2];
		pos[0]=pos[1]=1;
		int time;
		for (time=0;!mas[0].empty() || !mas[1].empty();time++){
			bool fl[2];
			fl[0]=fl[1]=false;
			int add[2];
			add[0]=add[1]=0;
			for (int j=0;j<2;j++){
				if (mas[j].empty())
					continue;
				if (mas[j].back().first!=pos[j])
					add[j]=(mas[j].back().first>pos[j]?1:-1);
				else{
					if (mas[1-j].empty() || mas[1-j].back().second>mas[j].back().second)
						fl[j]=true;
				}
			}
			for (int j=0;j<2;j++){
				if (fl[j])
					mas[j].pop_back();
				if (add[j])
					pos[j]+=add[j];
			}
		}
		cout<<time<<"\n";
	}
	return 0;
}