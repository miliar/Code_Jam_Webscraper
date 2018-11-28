#include <iostream>
#include<algorithm>
#include<string>
#include<cstring>
#include<cmath>
#include<vector>
#include <cstdio>
#include<map>
#include<stack>
#include<set>
#include<queue>
#include<cctype>
#include<assert.h>
using namespace std;
#define PI acos(-1.0)
#define INT __int64
#define MAX(x,y) (x>y?x:y)
#define MIN(x,y) (x<y?x:y)
void SWAP(int&x,int&y) 
{
	x^=y,y^=x,x^=y;
}
INT sum[1005];
int c[1005];
INT circle[1005];
int arr[1005];
int main(void)
{
	FILE*in=fopen("D://in.txt","r");
	FILE*out=fopen("D://out.txt","w");
	int t; fscanf(in,"%d",&t);
	for(int i=1;i<=t;i++)
	{
		int r,k,n;
		fscanf(in,"%d%d%d",&r,&k,&n);
		fprintf(out,"Case #%d: ",i);
		memset(sum,-1,sizeof(sum));
		int j;
        INT ret=0;
		INT sumg=0;
		for(j=0;j<n;j++) 
		{
			fscanf(in,"%d",&arr[j]);
			sumg+=arr[j];
		}
		if(sumg<=k)
		{
			fprintf(out,"%I64d\n",sumg*r);
		}
		else
		{
			int first=0;
			for(j=0;j<r;j++)
			{
				int temp=0;int ff=first;
				if(sum[first]==-1)
				{
				    while(true)
					{
						if(temp+arr[first]>k) break;
						temp+=arr[first];
					//	cout<<first<<" "<<arr[first]<<" "<<temp<<endl;
						first++;
						if(first==n) first=0;
					}
					c[ff]=j;
					sum[ff]=temp;
					//cout<<"heh "<<ff<<" "<<c[ff]<<" ";
					//printf("%I64d %d\n",sum[ff],first);
					
					ret+=temp;
				}
				else
				{
				    int ff=first;
					int len=j-c[first];
					for(int kk=0;kk<len;kk++)
					{
						circle[kk]=sum[ff];
						//printf("%d %I64d\n",ff,sum[ff]);
						if(kk>0) circle[kk]+=circle[kk-1];
						int temp=0;
						while(true)
						{
							if(temp+arr[ff]>k) break;
							temp+=arr[ff];
							ff++;
							if(ff==n) ff=0;
						}
					}
					//cout<<endl<<"la la "<<len<<" "<<circle[len-1]<<endl;
					//cout<<circle[(r-j)%len-1]<<endl;
					ret+=((r-j)/len)*circle[len-1]+circle[(r-j)%len-1];
					break;
				}
			}
			fprintf(out,"%I64d\n",ret);

		}
	}
	return 0;
}