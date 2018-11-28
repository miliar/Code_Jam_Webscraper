#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
static void __dtor_retz(void) __attribute__ ((destructor));
static void __dtor_retz(void) { exit(0); }
#define SIZE(X) ((int)(X.size()))//NOTES:SIZE(
#define LENGTH(X) ((int)(X.length()))//NOTES:LENGTH(
#define MP(X,Y) make_pair(X,Y)//NOTES:MP(

const int maxlength=200;

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>

vector<string> explode( const string &delimiter, const string &str)
{
    vector<string> arr;

    int strleng = str.length();
    int delleng = delimiter.length();
    if (delleng==0)
        return arr;//no change

    int i=0;
    int k=0;


    while( i<strleng )
    {
        int j=0;
        while (i+j<strleng && j<delleng && str[i+j]==delimiter[j])
            j++;
        if (j==delleng)//found delimiter
        {
            arr.push_back(  str.substr(k, i-k+1) );
            i+=delleng;
            //k=i;
        }
        else
        {
            i++;
        }
    }
    arr.push_back(  str.substr(k, i-k) );
    return arr;
}

bool MyDataSortPredicate(string d1, string  d2)
{
  return d1.size() > d2.size();
}
int cnk[1000][2];
int main()
{
	freopen("A-large.in","r",stdin);freopen("largea.out","w",stdout);
	int testcase;
	///clock_t start,end;
//  double dif;
     
 	int n=0,m=0;
 		scanf("%d",&testcase);
 		
	for (int caseId=1;caseId<=testcase;caseId++)
	{    
         int nline = 0;
         int visible = 0;
         scanf ("%d",&nline);
         for (int i=0; i<nline;i++)
         {
             scanf("%d",&cnk[i][0]);
             scanf("%d",&cnk[i][1]);
             
         }
        
		 for(int i =0; i<nline ;i++)
         {
                  for(int j =i+1; j<nline ;j++)
                  {
                      
  //if(((cnk[i][0]>cnk[j][0]&&cnk[i][1]<cnk[j][0])^(cnk[i][0]<cnk[j][0]&&cnk[i][1]>cnk[j][0]))&&(!((cnk[i][0]==cnk[i][1])&&(cnk[j][0]==cnk[j][1]))))
   if((cnk[i][0]<cnk[j][0]&&cnk[i][1]>cnk[j][1])||(cnk[i][0]>cnk[j][0]&&cnk[i][1]<cnk[j][1]))
  {
                                                    visible++;
                                                    
                                                    }
  
                 }
                 }
                 cout << "Case #"<<caseId << ": "<< visible <<"\n";
    }
                  

return 0;

}

