#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <numeric>

using namespace std;

#define v vector <int>
#define vs vector <string>
#define vv vector< v >
#define forz(i,n) for(int i=0;i<n;i++)
#define fl(i,s,n) for(int i=s;i<n;i++)
#define lh(i) int(i.length())
#define sz(i) (int)(i.size())
#define pb(a) push_back(a)
#define all(a) a.begin(),a.end()

map<int,int>mm;
void prime()
{
	mm[2]=1;
	mm[3]=1;

	int flg=0;
	for(int i=4;i<=10000;i++)
	{
		flg=0;
		for(int j=2;j*j<=i;j++)	
		{
			if(i%j==0)flg=1;
		}
		if(flg==0)mm[i]=1;
	}
}
int main()
{
	int t,ot=0;
	cin>>t;
	prime();
	while(t--)
	{
		
		int a,b,p;
		v arr(1001,0);
		cin>>a>>b>>p;
		int hi=1;
		int gg=1;
		int jj=1;
		for(int i=p;i<=b;i++)
		{int flg=0;
			if(mm[i]==0)continue;
			for(int j=a;j<=b;j++)
			{
				if(j%i==0)
				{
					for(int s=j;s<=b;s+=i)	
					{
						if(arr[s]!=0){hi=arr[s];flg=1;break;}
					}
					if(flg==0)hi=gg++;
					for(int s=j;s<=b;s+=i)arr[s]=hi;
					break;
				}	
			}			
		}
		map<int,int>kkk;
		int cnt=b-a+1;
		for(int i=a;i<=b;i++)kkk[arr[i]]++;
		for(int i=1;i<=1000;i++)if(kkk[i]!=0){cnt-=kkk[i];cnt++;}
	//	for(int i=a;i<=b;i++){cout<<arr[i]<<" ";}
		cout<<"Case #"<<++ot<<": "<<cnt<<endl;
	}
return 0;
}