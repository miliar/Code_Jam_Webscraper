#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cctype>
#include <complex>
#include <cassert>
#include <string>
#include <valarray>
#include <queue>
#include <iterator>
using namespace std;
#define pb push_back
#define B begin()
#define E end()
#define S size()
#define vs vector<string>
#define vi vector<int>
//#define vii vector<vi>
//#define vp vector<part>
//#define ld long double
//#define ll long long
const int MAXI = 2147483647;

FILE* fp1;

class part
{
    public:
    int a1; int a2;
};

int chg_time(char time[])
{
    int newtime;
    newtime = (600 * (time[0]-'0'))+(60 * (time[1]-'0'))+(10 * (time[3]-'0'))+(1*(time[4]-'0'));
    return newtime;
}    

bool compp(part a, part b)
{
     if (a.a1<b.a1)
     return 1;
     if (a.a1>b.a1)
     return 0;
	 return(a.a2>b.a2);
    
}

int func(vector<part> timings)
{
    sort(timings.B,timings.E,compp);
    int ans=0,temp=0;
    for(int e1=0;e1<timings.S;e1++)
        {
    	if(timings[e1].a2==0)temp++;else temp--;ans>?=temp;
        }
    return ans;
}

int main()
{
	int i,n,turn;  //n - no of test cases
						//turn - turn around time
	int na,nb;     //na - no of trains at A
						//nb - no of trains at B
	
	FILE *fp; //fp - input file
                   //fp1 - output file

	fp = fopen("train.txt","r");
	fp1 = fopen("trn_out.txt","w");
	fscanf(fp,"%d",&n);  //reading the no of test cases
	
	for(i=1;i<=n;i++)
	{
	    fprintf(fp1,"Case #%d: ",i);
		fscanf(fp,"%d",&turn);
		fscanf(fp,"%d",&na);
		fscanf(fp,"%d",&nb);
				
        vector<part> a,b;
	    part temp;
        char arr[100];
        
		for(int j=0;j<na;j++)
		{    
            temp.a2=0;
			fscanf(fp,"%s",arr);
			temp.a1=chg_time(arr); a.pb(temp);
			
		    temp.a2=1;
			fscanf(fp,"%s",arr);
			temp.a1=chg_time(arr)+turn; b.pb(temp);
		}

		for(int k=0;k<nb;k++)
		{
            temp.a2=0;
            fscanf(fp,"%s",arr);
	        temp.a1=chg_time(arr); b.pb(temp);
            
			temp.a2=1;
            fscanf(fp,"%s",arr);
            temp.a1=chg_time(arr)+turn; a.pb(temp);
		}
        int train_need_A = func(a);
        int train_need_B = func(b); 
        fprintf(fp1,"%d ",train_need_A);
        fprintf(fp1,"%d\n",train_need_B);
    }       

}

