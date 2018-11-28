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

struct stru
{
    char a;
    int button;
};
stru arr[MAX_LENGTH];

void initialize()
{
    int i,j;
    for(i=0;i<MAX_LENGTH;i++)
    {
        arr[i].a=NULL;
        arr[i].button=NULL;
    }
}
int main()
{
    //freopen("aaa.in","r",stdin);
	//freopen("out1.txt","w",stdout);
	int ind,i,j,N,T,result,button,current_blue,current_orange,previous_blue,previous_orange,previous_executing,temp;
	bool blue_flag;
	char s[2];
	scanf("%d",&T);
	for(ind=1;ind<=T;ind++)
	{
        initialize();
		scanf("%d",&N);
		for(i=0;i<N;i++)
		{
		    scanf("%s%d",&s,&button);
		    stru st;
		    st.a=s[0];
		    st.button=button;
		    arr[i]=st;
		    //printf("=====%c==%d===\n",st.a,st.button);
		}
		previous_blue=1;
		previous_orange=1;
		current_blue=1;
		current_orange=1;
		previous_executing=0;
		result=0;
		blue_flag=NULL;
		for(i=0;i<N;i++)
		{
		    if(arr[i].a=='O')
		    {
		        current_orange=arr[i].button;
                temp=abs(previous_orange-current_orange);
                if(temp<=previous_executing&&blue_flag==true)
                {
                    previous_executing=1;
                    result+=1;
                }
                else
                {
                    if(blue_flag==false)
                    {
                        previous_executing=previous_executing+temp+1;
                        result+=temp+1;
                    }
                    else
                    {
                        previous_executing=temp-previous_executing+1;
                        result+=previous_executing;
                    }
                }
                previous_orange=current_orange;
                blue_flag=false;
		    }
		    else
		    {
                current_blue=arr[i].button;
                temp=abs(previous_blue-current_blue);
                if(temp<=previous_executing&&blue_flag==false)
                {
                    previous_executing=1;
                    result+=1;
                }
                else
                {
                    if(blue_flag==true)
                    {
                        previous_executing=previous_executing+temp+1;
                        result+=temp+1;
                    }
                    else
                    {
                        previous_executing=temp-previous_executing+1;
                        result+=previous_executing;
                    }
                }
                previous_blue=current_blue;
                blue_flag=true;
		    }
		    //printf("current orange :%d=====result :%d=====\n",current_orange,result);
		}
		printf("Case #%d: %d\n",ind,result);
	}
	return 0;
}
