#pragma warning(disable:4786)
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<cmath>
#include<stack>
#include<ctime>

using namespace std;

#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b)  ((a) < (b) ? (a) : (b))


char str[100000];
string s,r;

int main()
{
	int i,j,k,tests,cs=0;

	//freopen("C:\\.in","r",stdin);
	freopen("C:\\Dsmall.txt","w",stdout);

	scanf("%d",&tests);

	while(tests--)
	{
		int arr[20];

		scanf("%d",&k);
		scanf("%s",str);

		s=r=str;

		int L=strlen(str);

		for(i=0;i<k;i++)
			arr[i]=i;

		int best=1000000;

		do{
			int cnt=0;
			for(i=0;i<L;i+=k)
			{
				string t=s.substr(i,k);
				for(j=0;j<t.length();j++)
					r[i+j]=t[arr[j]];
			}
			for(cnt=i=1;i<L;i++)
				if(r[i]!=r[i-1]) cnt++;
			if(cnt<best) best=cnt;
		}while(next_permutation(arr,arr+k));

	
		printf("Case #%d: %d\n",++cs,best);
		
	}
	return 0;
}