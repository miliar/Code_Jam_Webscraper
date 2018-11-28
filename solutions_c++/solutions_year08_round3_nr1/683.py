#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>

using namespace std;

//global variables here


//functions here
vector <int> bubble(vector <int> arr, long max){
int tmp;
for(long i=0;i<max;i++)
{
 for(long x=0; x<max-1-i; x++)
 {
  if(arr[x] < arr[x+1])
    {
    //r.push_back(rnd);
   tmp = arr[x];
   arr[x] = arr[x+1];
   arr[x+1] = tmp;
  }
 }
}
return  arr;
}


//main here
int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int cases;
	scanf("%d",&cases);
	for(int cs=1;cs<=cases;cs++)
	{
		// stuff here
		int ans=0;
		int p,k,l;
		cin>>p>>k>>l;
		vector <int> inp;
		for(int i=0;i<l;i++)
		{
			int zz;
			cin>>zz;
			inp.push_back(zz);
		}
		
		inp = bubble(inp, l);
		
		int cnt=1;
		int mul=1;
		for(int i=0;i<l;i++)
		{
			if(cnt > k)
				{
				cnt=1;
				mul++;
				}
			ans+=inp[i]*mul;
			cnt++;
		}
		
		
		printf("Case #%d: %d\n", cs, ans);
	}
	return 0;
}