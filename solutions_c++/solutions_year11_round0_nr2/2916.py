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
typedef int64_t lint;
typedef unsigned int ulint;

int arr[MAX_LENGTH][MAX_LENGTH],brr[MAX_LENGTH][MAX_LENGTH],crr[MAX_LENGTH],drr[MAX_LENGTH];

void initialize()
{
    int i,j,k,l,m;
    for(i=0;i<MAX_LENGTH;i++)
    {
        crr[i]=0;
        drr[i]=0;
        for(j=0;j<MAX_LENGTH;j++)
        {
            brr[i][j]=0;
            arr[i][j]=0;
        }
    }
}
int main()
{
    //freopen("bbb.in","r",stdin);
	//freopen("out_bb.txt","w",stdout);
	int ind,i,j,k,N,T,result,m,u,v,w,x,y,z,consta=62,current_index;
	bool clear_flag;
	char a[110];
	scanf("%d",&T);
	for(ind=1;ind<=T;ind++)
	{
        initialize();
		scanf("%d",&u);
		for(i=0;i<u;i++)
		{
		    scanf("%s",&a);
		    arr[a[0]-consta][a[1]-consta]=a[2]-consta;
		    arr[a[1]-consta][a[0]-consta]=a[2]-consta;
		}
		scanf("%d",&v);
		for(i=0;i<v;i++)
		{
		    scanf("%s",&a);
		    brr[a[0]-consta][a[1]-consta]=1;
		    brr[a[1]-consta][a[0]-consta]=1;
            //printf("%c %c \n",a[1],a[0]);
		}
		scanf("%d",&w);
		scanf("%s",&a);
		for(i=0;i<w;i++)
		{
		    crr[i]=a[i]-consta;
		    //printf("%c ",a[i]);
		}
		current_index=0;
		for(i=0;i<w;i++)
		{
		    drr[current_index]=crr[i];
		    clear_flag=false;
		    if(current_index!=0)
		    {
		        //printf("%c \n",drr[current_index]+consta);
                if(arr[drr[current_index]][drr[current_index-1]]!=0)
                {
                    drr[current_index-1]=arr[drr[current_index]][drr[current_index-1]];
                    drr[current_index]=0;
                    current_index-=1;
                }
                for(j=0;j<current_index;j++)
                {
                    //printf("%c %c \n",drr[j]+consta,crr[i]+consta);
                    if(brr[drr[j]][drr[current_index]]==1)
                    {
                        for(k=0;k<=current_index;k++)
                        {
                            drr[k]=0;
                            current_index=0;
                            clear_flag=true;
                        }
                    }
                }
		    }
		    /*for(m=0;m<current_index;m++)
            {
                printf("%c, ",drr[m]+consta);
            }
            printf("\n");*/
            if(clear_flag==false)
            {
                current_index+=1;
            }
		}
		printf("Case #%d: [",ind);
		for(i=0;i<current_index;i++)
		{
		    printf("%c",drr[i]+consta);
		    if(i!=current_index-1)
		    {
		        printf(", ");
		    }
		}
		printf("]\n");
	}
	return 0;
}
