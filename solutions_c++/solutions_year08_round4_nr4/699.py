#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <cctype>
#include <algorithm>
#include <vector>
#include <numeric>
#include <set>
#include <queue>
#include <map>
#include <list>
#include <string>
#include <iostream>
#include <stack>
#include <sstream>
using namespace std; 
#define PB push_back
#define MP make_pair
#define F first
#define S second 
#define fo(i,n) for(i=0;i<(int)(n);i++)
#define loop(i,n) for(i=0,int __n=n;i<__n;i++)
#define BE(a) a.begin(),a.end() 
#define CLS(a,b) memset(a,b,sizeof(a))
#define SZ(a) ((int)a.size())
const long double pi=acos(-1.0);
#define torad(a) (a*pi/180.0)
typedef vector<int> vi ; 
typedef vector<string> vs ; 
typedef vector<double> vd ; 
typedef pair<int,int> pii ; 
typedef long long ll ; 
typedef long double ld ; 
typedef double dl ; 
class node {public:
};
typedef vector<node> vn ; 
FILE *in=fopen("D-small-attempt1.in","r");
FILE *out=fopen("D-small-attempt1.out","w");

int cases,n;
string str;
char cstr[2000];
int len;
int main()
{
	fscanf(in,"%d",&cases);
	int i,j,ans=1<<30,z;
	int g,c,v;
	int arr[10];
	for(z=0;z<cases;z++)
	{	
		ans=1<<30;
		fscanf(in,"%d",&n);
		len=fscanf(in,"%s",cstr);
		str=cstr;
		len=str.size();
		for(i=0;i<n;i++)
			arr[i]=i;
		string tmp;
		do{
			str=cstr;
			for(i=0;i<len;i+=n)
			{
				tmp=str.substr(i,n);
				for(j=0;j<n;j++)
					str[i+j]=tmp[arr[j]];
			}
			char last='K';
			int cnt=0;
			for(i=0;i<len;i++)
			{
				if(str[i]!=last)
					cnt++;
				last=str[i];
			}
			ans=min(ans,cnt);
		}while(next_permutation(arr,arr+n));

		fprintf(out,"Case #%d: %d\n",z+1,ans);
	}
}