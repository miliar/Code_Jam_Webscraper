#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<iostream>
#include<string>
#include<sstream>
#include<ctype.h>
#include<vector>
#include<map>
#include<queue>
#include<math.h>
#include<algorithm>
#include<set>

#define pb push_back
#define PI acos(-1.0)
#define SZ(a) (int)a.size()
#define csprnt printf("Case #%d: ", cas++);
#define EPS 1e-9
#define MAX 100010
#define ll long long
#define INF (1<<30)
#define pii pair<int, int>
#define MP make_pair

using namespace std;

int arr[110];

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
    int t, cas=1;
    scanf("%d", &t);
    while(t--)
    {
    	int n, s, p, i, j;
    	scanf("%d%d%d", &n, &s, &p);
    	for(i=0;i<n;i++)
			scanf("%d", &arr[i]);
		int cnt=0, val, rem;
		for(i=0;i<n;i++)
		{
			val = arr[i]/3;
			rem = arr[i]%3;
			if(rem==2) val++;
			else if(rem==1) val++;
//			cout<<"val "<<val<<" "<<p<<endl;
			if(val>=p) cnt++;
			else if(((val+1)>=p) && ((arr[i]>2) && (arr[i]<29)))
			{
				if(s>0)
				{
					s--;
					cnt++;
				}
			}
		}
		csprnt;
		printf("%d\n", cnt);
    }
    return 0;
}

