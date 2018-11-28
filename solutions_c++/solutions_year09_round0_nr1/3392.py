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
#define vvs vector<vector<string>>
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
	int l,d,n,turn;  //n - no of test cases
						//turn - turn around time
	int na,nb;     //na - no of trains at A
						//nb - no of trains at B
	
	FILE *fp; //fp - input file
                   //fp1 - output file

	fp = fopen("A-small-attempt3.in","r+");
	fp1 = fopen("alien-small.txt","w+");
	fscanf(fp,"%d %d %d",&l,&d,&n);  //reading the no of test cases
	//fprintf(fp1,"hello"); 
	vs dict;
	char arr[10000];
	for(int i=0;i<d;i++)
	{
        //for(int j=0;j<l;j++){
		//fscanf(fp,"%c",&arr[j]);
        //}
        fscanf(fp,"%s",arr);
        dict.pb(arr);
        printf("%s\n",arr);
     }
                    
	for(int i=1;i<=n;i++)
	{
	    fprintf(fp1,"Case #%d: ",i);
	    char a;
	    //for(int j=0;j<l;j++){
		fscanf(fp,"%s",arr);
		cout<<arr<<endl;
        //}
		vs expr;
		string str="";
		int ans = 0;
		for(int j=0,count=0;count<l;){
                //fscanf(fp,"%c",&arr[j]);
              if(arr[j]>='a'&&arr[j]<='z'){
                  str += arr[j];
                  expr.pb(str);
                  cout<<str;
                  str="";
                  count++;
                  j++;
              }
              else{
                   j++;
                   //fscanf(fp,"%c",&arr[j]);
                   while(arr[j]!=')')
                   {
                        
                        str += arr[j];
                        j++;
                     //   fscanf(fp,"%c",&arr[j]);
                   }
                   count++;
                   cout<<str;
                  expr.pb(str);
                   str = "";
                   j++;
              }
              
        }
        copy(expr.begin(),expr.end(),ostream_iterator<string>(cout,"\n  "));cout<<endl;
        for(int j=0;j<d;j++){
                cout<<dict[j];
                scanf("%d",&turn);
           int match2=1;
            for(int k=0;k<l;k++){
              int  match1=0;
                for(int m=0;m<expr[k].S;m++){
                    if(expr[k][m]==dict[j][k]){
                          match1=1;
                          break;
                    }
                }
                if(match1==0){
                    match2=0;
                    break;
                }
            } 
            if(match2==1)
            ans++;
        }
		//output process
            fprintf(fp1,"%d\n",ans);
	
    
		
    }       

}

