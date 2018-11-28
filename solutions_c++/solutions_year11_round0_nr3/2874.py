#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
using namespace std;

void change(bool*ptr, int len)
{
	for(int i = 0; i < len; i++)
	{
		if(*ptr)
		{
			*ptr = 0;
		}
		else 
		{
			*ptr = 1;
			break;
		}
		ptr++;
	}
}

#define SMALL
//#define LARGE
int main()
{
#ifdef SMALL
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
#endif
#ifdef LARGE
	freopen("C-large.in","r",stdin);
	//freopen("A-small.in","r",stdin);
	freopen("C-large-practice.out","w",stdout);
#endif

	int case_n;
	int top,ans,ans_1,ans_2;
	int ans_p1,ans_p2;
	int n;
	int c[1000];
	bool bo[1000];

	scanf("%d",&case_n);

	for (int i=0; i<case_n; i++)
	{
		top=0;
		ans=0;
		ans_1=0;
		ans_2=0;
		ans_p1=0;
		ans_p2=0;

		bool depok=false;

		scanf("%d",&n);
		//printf("%d",n);
		
		for (int j=0;j<n;j++)
		{
			scanf("%d",&c[j]);
			//printf("%d ",c[j]);
		}
		int pw=pow((double)2,n);
		for (int j=0;j<n;j++)
		{
			bo[j]=0;
		}
		for(int i = 0; i < pw; i++)
		{
			int tes1=0;
			int tes2=0;
			ans_p1=0;
			ans_p2=0;
			for(int k = 0; k < n; k++)
			{
				if(bo[k])
				{
					ans_p1^=c[k];
					tes1++;
					//printf("%d ",ans_p1);
				}
				else
				{
					ans_p2^=c[k];
					tes2++;
					//printf("%d ",ans_p2);
				}
			}
			if(tes1==n||tes1==0||tes2==n||tes2==0)
			{

			}
			else
			{
				if(ans_p1==ans_p2)
				{
					depok=true;
					ans_1=0;
					ans_2=0;
					for(int k = 0; k < n; k++)
					{
						if(bo[k])
						{
							ans_1+=c[k];
						}
						else ans_p2+=c[k];
					}
					ans=max(ans_1,ans_2);
					if(ans>top)top=ans;
				}
			}
			
			change(bo,n);
		}

// 			{
// 				depok=true;
// 				ans_1=0;
// 				ans_2=0;
// 				for(int m=0;m<=j;m++)
// 				{
// 					ans_1+=c[m];
// 				}
// 				for(int m=j+1;m<n;m++)
// 				{
// 					ans_2+=c[m];
// 				}
// 				ans=max(ans_1,ans_2);
// 				if(ans>top)top=ans;
// 			}
		//printf("%d\n",c[n]^c[n-1]);
		//printf("%d %d %d\n",8221^6249,6249^2651,8221^2651);
	//int n=sizeof(aa)/sizeof(aa[0]); 
 	
// 		for (int j=0;j<n;j++)
// 		{
// 			ans_p1=c[0];
// 			for(int m=1;m<=j;m++)
// 			{
// 				ans_p1=ans_p1^c[m];
// 			}
// 			ans_p2=c[j+1];
// 			for(int m=j+2;m<n;m++)
// 			{
// 				ans_p2=ans_p2^c[m];
// 			}
// 			if (ans_p2==ans_p1)
// 			{
// 				depok=true;
// 				ans_1=0;
// 				ans_2=0;
// 				for(int m=0;m<=j;m++)
// 				{
// 					ans_1+=c[m];
// 				}
// 				for(int m=j+1;m<n;m++)
// 				{
// 					ans_2+=c[m];
// 				}
// 				ans=max(ans_1,ans_2);
// 				if(ans>top)top=ans;
// 			}
// 		}

		if(depok==false)printf("Case #%d: NO\n",i+1);
		else printf("Case #%d: %d\n",i+1,top);


	}
	return 0;
}
