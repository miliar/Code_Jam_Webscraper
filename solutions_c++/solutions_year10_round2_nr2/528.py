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
	  if(ans[i-1] == -1) { 
	       out<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<"\n";
	  }
	  else { 
	       out<<"Case #"<<i<<": "<<ans[i-1]<<"\n";
	  }
     }
}






vector<long long> pos;
vector<long long> speed;
vector<int> willreach;
long long N;
long long K;
long long B;
long long T;


int calc()
{
     // populate the willreach array   

     for(int i = 0 ; i < N ;i++)
     {
	  if( T*speed[i] >= B-pos[i] ) { willreach.push_back(1); }
	  else { willreach.push_back(0); }
	  //cout<<willreach[i]<<" ";
     }
     //cout<<"\n";
}


long long count()
{
     int curr_count =0;
     int chickens =0;
     for(int i=N-1;i>=0;i--)
     {
	  if(chickens >= K ) { return curr_count;} 
	  
	  if(willreach[i]) { chickens++; 
	       for(int j=i+1;j<N;j++) { if(!willreach[j]){curr_count++; } }
	  }

     }
	  if(chickens >= K ) { return curr_count;} 

     return -1;
}

void read()
{
    
    pos.clear();
    speed.clear();
    willreach.clear();
    for(int i=0;i<N;i++) {
	  long long temp;
	  in>>temp;
	  pos.push_back(temp);
     }
     for(int i=0;i<N;i++) {
	  long long temp;
	  in>>temp;
	  speed.push_back(temp);
     }


}


int main()
{

     in.open("B-large.in");
     out.open("B-large.out");
     int C;
     in>>C;
     for(int i=0;i<C;i++) {
	  in>>N;
	  in>>K;
	  in>>B;
	  in>>T;
	  read();
	  calc();
	  long long c = count();
	  ans.push_back(c);

     }
     print_ans();
     in.close();
     out.close();
     return 0;
}

