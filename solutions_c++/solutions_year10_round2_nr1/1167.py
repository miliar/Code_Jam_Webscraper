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

int main()
{
	freopen("A-large.in","r",stdin);freopen("large.out","w",stdout);
	int testcase;
	///clock_t start,end;
//  double dif;
 
 	int n=0,m=0;
 		scanf("%d",&testcase);
 		
	for (int caseId=1;caseId<=testcase;caseId++)
	{    
         int attempt =0;
    	vector<string> str1, str2;
    	string c;
    	scanf("%d",&n);
       scanf("%d",&m);
     
     	for (int j = 0; j < n; j++)
		{
			cin >> c;
			c+='/';
            str1.push_back(c);
		}
		for (int j = 0; j < m; j++)
		{
			cin >> c;
			c+='/';
			str2.push_back(c);
		}
		
     for (int j = 0; j < m; j++)
		{
			
			vector<string> v = explode("/",str2[j]);
			
			for(int i=0; i<v.size(); i++)
            {
                    if(v[i]!="/"&&find(str1.begin(), str1.end(), v[i])==str1.end())
                    {
                    str1.push_back(v[i]);
                    attempt++;
                    }
            }
		}
		  std::sort(str1.begin(), str1.end(), MyDataSortPredicate);
/*
 for (int j = 0; j < str1.size(); j++)
		{
			
			cout<< str1[j]<<"\n";
		}*/
          
          cout<< "Case #"<<caseId<<": " <<attempt <<"\n";
		
    }


return 0;

}

