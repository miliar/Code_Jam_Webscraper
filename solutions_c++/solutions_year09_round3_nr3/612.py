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
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
bool fg[101];
int solve(int n,vector<int>& pm)
{
	int res=0;
	for(int i1=0;i1<101;i1++) fg[i1]=true;
	for(int i=0;i<pm.size();i++)
	{
//		cout<<"pm: "<<i<<endl;
		int tmp1=pm[i];
//		cout<<"tmp1: "<<tmp1<<endl;
		for(int k1=tmp1-1;k1>=1;k1--)
		{
			if(fg[k1])
				res++;
			else
				break;
		}
		for(int k2=tmp1+1;k2<=n;k2++)
		{
			if(fg[k2])
				res++;
			else
				break;
		}
		fg[tmp1]=false;
	}
//	cout<<"sv res: "<<res<<endl;
	return res;
}

int main()
{
	//	freopen("A.in","r",stdin);
	freopen("C-small-attempt0.in","r",stdin);freopen("x3.txt","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-large.in","r",stdin);freopen("A-large.txt","w",stdout);
	int T;
	cin>>T;
	string str;
	getline(cin, str);
	int i,j;
	for(i=0;i<T;i++)
	{
		getline(cin, str);
		stringstream ss(str);
		int P,Q;
		ss>>P>>Q;
//		cout<<"P: "<<P<<" Q: "<<Q<<endl;
		vector<int> vc;
		getline(cin, str);
		int tmp;
//		cout<<"str str:"<<str<<endl;
		stringstream ss1(str);
		for(j=0;j<Q;j++)
		{
//			cout<<"j: "<<j<<endl;
			ss1>>tmp;
//			cout<<"tmp1: "<<tmp<<endl;
			vc.push_back(tmp);
//			cout<<"vc j:"<<vc[j]<<endl;
		}
//		cout<<"vc:"<<endl;

		int mm= solve(P, vc);
//		cout<<"mm:"<<mm<<endl;
	/*	do
		{
			res+ solve(P,vc);
		}while( next_permutation(vc.begin(),vc.end()) ); */
		while( next_permutation(vc.begin(),vc.end()) )
		{
			int tt=solve(P,vc);
//			cout<<"tt:"<<tt<<endl;
			if( mm > tt)
				mm = tt;
		}
		printf("Case #%d: %d\n", i+1, mm);
		
	}
	
}