#include <cstdlib>
#include <memory>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

#define DEBUG_FLAG 1
#if DEBUG_FLAG
#define dbg(...) cerr << #__VA_ARGS__ << ": " << __VA_ARGS__ << endl
#define cdbg(...) cerr << __VA_ARGS__ << endl
#else
#define debug(r)
#define dbg(...)
#endif
int ab[2][1000][2];
void merge(int N)
{
      int ptr1,ptr2,end1,end2,ptr;
      int n1 = N;
	//merge sort
	int f1 = 0,f2;
	for(int power = 0; ( 1 << power ) < n1; power++ )
	{
	    f2 = !f1;
	    for(int j = 0; j <= ( n1 >> power ); j += 2 )
	    {//Merge
		ptr = ptr1 = j*(1<<power);
		end1 = ptr2 = (j+1)*(1<<power);
		end2 = (j+2)*(1<<power);
		if( end1 > n1 )
		    ptr2 = end1 = n1;
 
		if( n1 < end2 )
		    end2 = n1;
		while( ptr1 < end1 && ptr2 < end2 )
		{
		    if( ab[f1][ptr1][0]<ab[f1][ptr2][0])
			{ab[f2][ptr][0] = ab[f1][ptr1][0];ab[f2][ptr][1] = ab[f1][ptr1][1];ptr1++;ptr++;}
		    else
			{ab[f2][ptr][0] = ab[f1][ptr2][0];ab[f2][ptr][1] = ab[f1][ptr2][1];ptr2++;ptr++;}
		}
 
		while( ptr1 < end1 )
 
		    {ab[f2][ptr][0] = ab[f1][ptr1][0];ab[f2][ptr][1] = ab[f1][ptr1][1];ptr1++;ptr++;}
 
		while( ptr2 < end2 )
               {ab[f2][ptr][0] = ab[f1][ptr2][0];ab[f2][ptr][1] = ab[f1][ptr2][1];ptr2++;ptr++;}

	    }
	    f1 = !f1;
	}
 
	if( f1 == 1 )
	{
	    for(int k = 0; k < n1; k++ )
		{ab[0][k][0] = ab[1][k][0];ab[0][k][1] = ab[1][k][1];}
	} //merging ends
      
}
int intrsct(int N)
{
    /*int i;
    for(i=0;i<N;i++)
    cout<<ab[0][i][0]<<" "<<ab[0][i][1]<<endl;
    merge(N);
    cout<<"\n";
    for(i=0;i<N;i++)
    cout<<ab[0][i][0]<<" "<<ab[0][i][1]<<endl;
    return 0;*/
    int o=0;
    merge(N);
    for(int i=0;i<N-1;i++)
    for(int j=i+1;j<N;j++)
    if(ab[0][i][1]>ab[0][j][1])
    o++;
    return o;
}
int main() 
{
	string fname = "A-large_1C";
	freopen((fname+".in").c_str(), "r", stdin);
	freopen((fname+".out").c_str(), "w", stdout);
    int T,N;
	scanf("%d", &T);
	for (int c = 1; c <= T; ++c) 
    {
		scanf("%d",&N);
		for(int i=0;i<N;i++)
		scanf("%d %d",&ab[0][i][0],&ab[0][i][1]);
		printf("Case #%d: %d\n",c,intrsct(N));
	}
	return 0;
}
