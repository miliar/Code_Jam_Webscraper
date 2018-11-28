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
#define MAX_LENGTH 110
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
//typedef int64_t lint;
//typedef unsigned int ulint;
int arr[MAX_LENGTH][MAX_LENGTH];
double brr[MAX_LENGTH],crr[MAX_LENGTH],err[MAX_LENGTH];
char drr[MAX_LENGTH];
int main()
{
    freopen("aaa.in","r",stdin);
	freopen("out_aaa.txt","w",stdout);
	int ind,i,j,k,N,T,result,cnt,counter,temp,temp1,idx,index;
	double a,b,c,d,e,f,sum,s,cn,rpi;
	scanf("%d",&T);
	for(ind=1;ind<=T;ind++)
	{
        memset(arr,NULL,sizeof(arr));
        memset(brr,NULL,sizeof(brr));
        memset(crr,NULL,sizeof(crr));
        memset(err,NULL,sizeof(err));
		scanf("%d\n",&N);
		for(i=0;i<N;i++)
		{
		    memset(drr,NULL,sizeof(drr));
		    gets(drr);
		    //printf("%s\n",drr);
		    for(j=0;j<N;j++)
            {
                if(drr[j]=='0'){arr[i][j]=0;}
                else if(drr[j]=='1'){arr[i][j]=1;}
                else{arr[i][j]=-1;}
                //printf("%d ",arr[i][j]);
            }
            //printf("\n");
		}
		for(i=0;i<N;i++)
		{
		    sum=0;cnt=0;
		    for(j=0;j<N;j++)
            {
                if(arr[i][j]!=-1){sum+=arr[i][j];cnt+=1;}
            }
            sum/=cnt;
            brr[i]=sum;
            //printf("%lf ",brr[i]);
		}
		for(i=0;i<N;i++)
		{
		    sum=0;cnt=0;
		    for(j=0;j<N;j++)
            {
                if(j!=i)
                {
                    if(arr[i][j]!=-1)
                    {
                        s=0;cn=0;
                        for(k=0;k<N;k++)
                        {
                            //if(arr[i][j]==-1){break;}
                            if(k!=i){if(arr[j][k]!=-1){s+=arr[j][k];cn+=1;}}
                        }
                        s/=cn;
                        sum+=s;
                        cnt+=1;
                        //printf("%lf ",s);
                    }
                }
            }
            //printf("%lf ",sum);
            sum/=cnt;
            crr[i]=sum;
            //printf("%lf ",sum);
		}
		for(i=0;i<N;i++)
		{
		    sum=0;cnt=0;
		    for(j=0;j<N;j++)
            {
                if(arr[i][j]!=-1)
                {
                    if(i!=j){sum+=crr[j];cnt+=1;}
                }
            }
            sum/=cnt;
            err[i]=sum;
            //printf("%lf ",sum);
		}
		printf("Case #%d:\n",ind);
		for(i=0;i<N;i++)
		{
		    rpi=0.25*brr[i]+0.50*crr[i]+0.25*err[i];
		    printf("%.12lf\n",rpi);
		}
	}
	return 0;
}
