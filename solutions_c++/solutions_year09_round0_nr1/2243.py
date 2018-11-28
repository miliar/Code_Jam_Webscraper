#include <cstdio>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
typedef long long ll;
const int inf=(1<<30);
#define mset(a,x) memset(a,x,sizeof(a))
#define ABS(a) ((a) >= 0 ? (a) : -(a))
#define MAX(a,b) ((a)>(b)?(a):(b))
#include <stdlib.h>

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int a,b,c,i,t=1,j,p,q,flag;
	cin>>a>>b>>c;
	int count=0;
	string str[5005],str1;
	for (i=0 ;i<b ;i++ )
		cin>>str[i];
	for (i=0 ;i<c ;i++ )
	{
		cin>>str1;
		for (j=0 ;j<b ;j++ )
		{
			for(p=0,q=0,flag=0;p<a&&q<str1.size();)
			{
				if(str1[q]=='(')
				{
					flag=1;
					q++;
				}
				else if(str1[q]==')')
				{
					flag=0;
					q++;
				}
				else if(str[j][p]==str1[q]&&flag==0)
				{
					p++;
					q++;
				}
				else if(str[j][p]==str1[q]&&flag==1)
				{
					p++;
					q++;
					while (str1[q]!=')')
						q++;
				}
				else if(flag==1)
					q++;
				else 
					break;
			}
			if(p==a)
				count++;
		}
		cout<<"Case #"<<t++<<": "<<count<<endl;
		count=0;
	}
	return 0;
}

/*

*/
