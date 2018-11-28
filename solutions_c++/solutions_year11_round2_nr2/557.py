// zero.lin`s google_codejam.cpp 
//


#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string.h>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstdlib>
#include <cctype>
#include <cmath>


#include "google_codejam\stdafx.h"
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vii;
typedef long long ll;

#define rep(i,n) for(int i=0;i<n;++i)
#define all(n) n.begin(),n.end()
#define sz(o) (int)(o.size())
#define mset(o,v) memset(o,v,sizeof(o))
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
#define mk(first,second) make_pair(first,second)
#define present(container, element) (container.find(element) != container.end()) 
#define cpresent(container, element) (find(all(container),element) != container.end())

const int inf=1<<28;
const double eps=1e-11;
int gcd(int a,int b){return b==0?a:gcd(b,a%b);}
int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	
	
	int testcase;
	scanf("%d",&testcase);
	
	rep(caseID,testcase)
	{
		int c,d;
		cin>>c>>d;
		vector<pair<int,int>> arr;
		for(int i=0;i<c;++i)
		{
			int p,v;
			cin>>p>>v;
			arr.push_back( pair<int,int>(p,v));
		}
		sort(all(arr));
		double mx=0;
		for(int i=0;i<c;++i)
			for(int j=i;j<c;++j){
				int n=0;
				for(int k=i;k<=j;++k)
					n+=arr[k].second;
				mx=max(mx,1.0*((n-1)*d-(arr[j].first-arr[i].first))/2);
			}
		printf("Case #%d: ",caseID+1);
		cout<<mx<<endl;
		
	}
	
	return 0;
}

