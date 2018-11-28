#pragma comment(linker, "/STACK:16777216")
#pragma warning(disable:4786)

#include <set>
#include <map>
#include <list>
#include <cmath>
#include <stack>
#include <queue>
#include <bitset>
#include <vector>
#include <cstdio>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <fstream>
#include <iterator>
#include <iostream>
#include <algorithm>

using namespace std;

#define MAX_SIZE 99999999
#define MAX_LENGTH 103
#define INF (1<<29);

int MIN(int a,int b){return a<b?a:b;}
int MAX(int a,int b){return a>b?a:b;}
int GCD(int a,int b){while(b) b^=a^=b^=a%=b; return a;}
int LCM(int a,int b){return a*(b/GCD(a,b));}
void SWAP(int &a,int &b){a=a^b;b=a^b;a=a^b;}

const double PI = acos(-1);
const double ESP= 1e-11;

//typedef __int64 lint;
//typedef unsigned __int64 ulint;
typedef int64_t lint;
typedef unsigned int ulint;

char arr[MAX_LENGTH][MAX_LENGTH],brr[MAX_LENGTH][MAX_LENGTH];

int main()
{
    freopen("aaa.in","r",stdin);
	freopen("out_aaa.txt","w",stdout);
	int ind,i,j,N,T,result,cnt,counter,temp,temp1,idx,index,r,c;
	bool this_line_contains,res_found;
	scanf("%d",&T);
	for(ind=1;ind<=T;ind++)
	{
        memset(arr,NULL,sizeof(arr));
        memset(brr,NULL,sizeof(brr));
		scanf("%d%d",&r,&c);
		for(i=0;i<r;i++)
		{
		    scanf("%s",&arr[i]);
		}
		//for(i=0;i<r;i++)
		{
		    //printf("%s\n",arr[i]);
		}
		this_line_contains=false;
		res_found=true;
		for(i=0;i<r;i++)
		{
		    for(j=0;j<c;j++)
            {
                if(arr[i][j]=='#')
                {
                    if(arr[i][j+1]=='#'&&arr[i+1][j]=='#'&&arr[i+1][j+1]=='#')
                    {
                        arr[i][j]='/';arr[i][j+1]='\\';
                        arr[i+1][j]='\\';arr[i+1][j+1]='/';
                    }
                    else
                    {
                        res_found=false;
                    }

                }
            }
            if(res_found==false){break;}
		}
		for(i=0;i<r;i++)
		{
		    for(j=0;j<c;j++)
            {
                if(arr[i][j]=='#'){res_found=false;}
            }
		}
		if(res_found==false)
		{
		    printf("Case #%d:\nImpossible\n",ind);
		}
		else
		{
		    printf("Case #%d:\n",ind);
		    for(i=0;i<r;i++)
            {
                printf("%s\n",arr[i]);
            }
		}
	}
	return 0;
}
