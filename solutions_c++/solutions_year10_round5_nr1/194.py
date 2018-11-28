#include <fstream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <cstdio>
#include <string>
#include <iostream>
#include <queue>
#include <cmath>
#include <set>
#include <memory.h>

#define dat cin
#define sol cout
#define ll long long

using namespace std;

int a,b,d,x,y;

void gcdext(int a,int b, int *d, int *x, int *y)
{
  int s;
  if (b == 0)
  {
    *d = a; *x = 1; *y = 0;
    return;
  }
  gcdext(b,a % b,d,x,y);
  s = *y;
  *y = *x - (a / b) * (*y);
  *x = s;
}

ll gcd(ll a,ll b) {return (b==0) ? a : gcd(b,a%b);}

bool prime[1000001]={0};

int main()
{
//	freopen("input.txt","r",stdin);
//	freopen("output.txt","w",stdout);
	ifstream dat("input.txt");
	ofstream sol("output.txt");
	int T;
	dat >> T;
	prime[0]=prime[1]=true;
	for(ll i=2;i<=1000000;i++)
		if (!prime[i])
			for(ll j=i*i;j<=1000000;j+=i)
				prime[j]=true;
	int kol=0;
	for(int i=0;i<=1000000;i++)
		if (!prime[i]) kol++;
//	sol << kol << endl;
	int f=10000,step;
	for(int t=1;t<=T;t++)
	{
		int D,K,nums[11]={0};
		dat >> D >> K;
		for(int i=0;i<K;i++)
			dat >> nums[i];
		step=1;
		for(int i=1;i<=D;i++)
			step*=10;
		set <int> next;
		if (K>1)
		{
			for(int i=2;i<=step;i++)
			{
				bool ff=false;
				for(int j=0;j<K;j++)
					if (nums[j]>=i)
					{
						ff=true;
						continue;
					}
				if (prime[i]||ff) continue;
				for(int a=0;a<i;a++)
				{
					int sk=nums[1]-(a*nums[0])%i;
					if (sk<0) sk+=i;
					bool poss=true;
					for(int j=1;j<K;j++)
					{
						if (nums[j]!=(nums[j-1]*a+sk)%i)
						{
							poss=false;
							break;
						}
					}
					if (poss) next.insert((nums[K-1]*a+sk)%i);
				}
			}
		}
		sol << "Case #" << t <<": ";
		if (next.size()==1) sol << *next.begin() << endl;
		else sol << "I don't know.\n";
	}
	return 0;
}

