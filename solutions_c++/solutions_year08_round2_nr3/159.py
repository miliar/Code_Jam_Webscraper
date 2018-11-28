#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream> 
#include <cmath>
#include <cstring>

using namespace std;

#define pb push_back
#define mp make_pair
#define PII pair<int,int> 
#define A first
#define B second
#define PIII pair<int,PII> 

#define I(x,y) x <y> :: iterator 
#define set(a,c) memset(a,c,sizeof(a))

#define REP(i,n) for(int i=0;i<n;i++)

typedef unsigned long long LLU;
typedef long long LL;
typedef long double LD;
int k;
int a[110];
int num[5001];
int n;
int main()
{
	int KASES;
	scanf("%d",&KASES);
	for(int kases=0;kases<KASES;kases++)
	{
		printf("Case #%d:",kases+1);
		scanf("%d%d",&k,&n);
		for(int i =0;i<n;i++)
			scanf("%d",&a[i]);
		int curr=1;
		int ptr = k;
		set(num,0);
		while(curr<=k){
			for(int i=0;i<curr;i++)
			{
				if(ptr==k) ptr= 1;
					else ptr++;
				while(num[ptr]!=0){
					if(ptr==k) ptr =1;
					else ptr++;
				}
			}
			num[ptr] = curr;
			//cout<<"@ "<<ptr<<" " <<curr<<endl;
			curr++;
		}
		for(int i=0;i<n;i++)
			printf(" %d",num[a[i]]);
		printf("\n");
	}
}

