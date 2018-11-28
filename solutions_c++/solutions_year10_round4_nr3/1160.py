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
#include <fstream>
#include <string>
#include <gmp.h>
#include <stdio.h>
#include <stdarg.h>





using namespace std;

ofstream out;
ifstream in;

vector<int> ans;
void print_ans()
{
     int sz = ans.size();
     for(int i=1;i<=sz;i++)
     {
	  string temp;
	  out<<"Case #"<<i<<": "<<ans[i-1]<<"\n";
     }
}





long long arr[101][101];
long long arr1[101][101];


int minx;
int maxx;
int miny;
int maxy;


void readandfill()
{
     int X1;
     in>>X1;
     int Y1;
     in>>Y1;
     int X2;
     in>>X2;
     int Y2;
     in>>Y2;


     for(int i=X1;i<=X2;i++){
	  for(int j=Y1;j<=Y2;j++){
	       arr[i][j] = 1;
	  }}//for


}

bool north(int i,int j)
{
     if(i>0 && arr[i-1][j] ) { return true; }
     return false;
}

bool west(int i,int j)
{
     if(j>0 && arr[i][j-1] ) { return true; }
     return false;
}


long long calc()
{
     long long ans = 0;

     while(1){
	  bool done = true;

	  for(int i = minx;i<=maxx;i++) {
	       for(int j = miny;j<=maxy;j++) {
		    if( arr[i][j] ) { done = false;}
		    arr1[i][j] = arr[i][j];
		    if( arr[i][j] == 0  && ( arr[i-1][j]) && ( arr[i][j-1])) { arr1[i][j] = 1; }
		    if( arr[i][j] == 1  && ( !arr[i-1][j]) && ( !arr[i][j-1])) { arr1[i][j] = 0; }
	       }}
	  if(done) { break; }
		    ans++;
	  for(int i = minx;i<=maxx;i++) {
	       for(int j = miny;j<=maxy;j++) {
		    arr[i][j] = arr1[i][j];

	       }}
     }//while
return ans;
}




void init()
{
     memset(arr,0,sizeof(arr));
     memset(arr1,0,sizeof(arr1));
     minx = 1;
     maxx = 100;
     miny = 1;
     maxy = 100;


}

int main()
{

     in.open("C-small-attempt0.in");
     out.open("C-small.out");
     int T;
     in>>T;
     for(int i=0;i<T;i++) {
	  init();
	  long long R;
	  in>>R;
	  for(int j=0;j<R;j++)
	  {
	       readandfill();
	  }
	  long long c = calc();
	  ans.push_back(c);

     }
     print_ans();
     in.close();
     out.close();
     return 0;
}

