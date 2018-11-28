#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
#include <queue>
#include <cstring>
#include <fstream>
using namespace std;
bool mp[41][41];
int N;
#define fir(i,j,n) for(int (i)=(j);(i)<(n);(i)++)
bool valid(int row,int prow)
{
	fir(i,prow+1,N) if (mp[row][i]) return false;
	return true;
}
void swapRow(int r1,int r2)
{
	fir(i,0,N) swap(mp[r1][i],mp[r2][i]);
}
int main()
{
	int tc;
	cin>>tc;int cs=0;
	while(tc--) {
		++cs;
		cin>>N;memset(mp,0,sizeof(mp));
		fir(i,0,N) {
			string s;cin>>s;
			fir(j,0,N) mp[i][j]=(s[j]=='1');
		}
		int ans=0;
		fir(i,0,N) {
			if (!valid(i,i))
			{
				/*
				cout<<"p "<<i<<endl;
				int j=i;
				while(!valid(j))
				{
					//fir(l,0,N) {fir(k,0,N) cout<<mp[l][k];cout<<endl;}cout<<endl;
					swapRow(j,j+1);
					//fir(l,0,N) {fir(k,0,N) cout<<mp[l][k];cout<<endl;}cout<<endl;
					j++;
					ans++;
				}
				*/
				int j=i;
				while(!valid(j,i)) j++;
				for(int k=j;k>i;k--) {++ans;swapRow(k,k-1);}
			}
			//fir(l,0,N) {fir(k,0,N) cout<<mp[l][k];cout<<endl;}cout<<endl;
		}
		cout<<"Case #"<<cs<<": "<<ans<<endl;
	}
	return 0;
}