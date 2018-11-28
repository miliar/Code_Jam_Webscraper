
#include <iostream>
#include <cstdio>
#include <string>
#include <map>
#include <queue>
#include <sstream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <cstring>
using namespace std;

const int INFI = 1000000000;

//FILE *in, *out;
int T;
long long n,k,b,t;

long long x[100];
long long v[100];







ifstream in("A-small.in");
ofstream out("A-small.out");
#define cout out
#define cin in





int main()
{
	//in = fopen("A-small.in","r");
    //in = fopen("A-large.in","r");
	//out = fopen("A-small.out","w");
	//out = fopen("A-large.out","w");

	//scanf("%d",&T);
	cin >> T;
	for(int cnt = 1;cnt <= T;cnt ++)
	{
//		vec.clear();
		cout << "Case #"<<cnt<<": "; 
		cin >> n >> k >> b >> t;
		for(int i = 0;i < n;i ++)
			cin >> x[i];
		for(int i = 0;i < n;i ++)
			cin >> v[i];

		int num = 0;
		if(k == 0)
		{
			cout << 0 << endl;
			continue;
		}
		
		for(int i = 0;i < n;i ++)
		{
			if(t * v[i] >= (b - x[i]))
				num ++;
		
		}
		//sort(vec.begin(),vec.end(),cmp);

		if(num < k)
		{
			cout << "IMPOSSIBLE" <<endl;
			continue;
		}

		int ans = 0;
	    for(int i = n - 1;i >= 0;i --)
		{
			if(v[i] * t >= (b - x[i]))
			{
				for(int j = i + 1;j < n;j ++)
				{
					if((b - x[j]) * v[i] > v[j] * (b - x[i]) && v[j] * t < (b - x[j]))
					{
						ans ++;
					}
				}
				k --;
				if(k == 0)
					break;
			}
		}
		cout << ans << endl;


			
			










	}


	return 0;
}
