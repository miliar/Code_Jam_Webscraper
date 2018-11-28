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
#define MAX_LENGTH 1000
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

int arr[MAX_LENGTH],brr[MAX_LENGTH],main_values[MAX_LENGTH],masking[MAX_LENGTH],A[MAX_LENGTH],B[MAX_LENGTH];

void initialize()
{
    int i,j;
    for(i=0;i<MAX_LENGTH;i++)
    {
        arr[i]=0;
        main_values[i]=NULL;
    }
}
void calculate_binary_conversion(int N)
{
    int i,j;
    for(i=0;i<MAX_LENGTH;i++)
    {
        if(N<=0)
        {
            break;
        }
        if(N%2==0)
        {
            brr[i]=0;
        }
        else
        {
            brr[i]=1;
        }
        N=N/2;
    }
}
int call_permutation(int i,int N)
{
    int j,k,l,temp,temp1,temp2,m,n,A_counter=0,B_counter=0,sum=0;
    for(j=0;j<MAX_LENGTH;j++)
    {
        brr[j]=0;
    }
    calculate_binary_conversion(i);
    for(j=0;j<N;j++)
    {
        if(brr[j]==1)
        {
            A[A_counter]=main_values[j];
            A_counter+=1;
        }
        else
        {
            B[B_counter]=main_values[j];
            B_counter+=1;
        }
    }
    temp1=0;
    for(j=0;j<A_counter;j++)
    {
        temp1=temp1^A[j];
    }
    temp2=0;
    for(j=0;j<B_counter;j++)
    {
        temp2=temp2^B[j];
    }
    if(temp1==temp2)
    {
        if(A_counter>B_counter)
        {
            for(j=0;j<A_counter;j++)
            {
                sum+=A[j];
            }
        }
        else
        {
            for(j=0;j<B_counter;j++)
            {
                sum+=B[j];
            }
        }
    }
    return sum;
}
int main()
{
    //freopen("cc.in","r",stdin);
	//freopen("out_c.txt","w",stdout);
	int ind,i,j,N,T,result,n,m,temp,temp1,max_value;
	bool result_exits;
	scanf("%d",&T);
	for(ind=1;ind<=T;ind++)
	{
        initialize();
        scanf("%d",&N);
        for(i=0;i<N;i++)
        {
            scanf("%d",&temp);
            main_values[i]=temp;
        }
        temp=0;
		for(i=0;i<N;i++)
		{
		    /*for(j=0;j<MAX_LENGTH;j++)
            {
                brr[j]=0;
            }
            calculate_binary_conversion(main_values[i]);*/
		    temp=temp^main_values[i];
		}
		if(temp==0)
		{
		    result_exits=true;
		}
		else
		{
		    result_exits=false;
		}
		/*for(i=0;i<MAX_LENGTH;i++)
		{
		    if(arr[i]!=0)
		    {
		        result_exits=true;
		        break;
		    }
		}*/
		result=0;
		max_value=pow(2,N);
		//printf("%d==\n",max_value);
		for(i=1;i<max_value-1;i++)
		{
		    temp=call_permutation(i,N);
		    result=MAX(result,temp);
		}
        if(result_exits==false)
        {
            printf("Case #%d: NO\n",ind);
        }
        else
        {
            printf("Case #%d: %d\n",ind,result);
        }
	}
	return 0;
}
