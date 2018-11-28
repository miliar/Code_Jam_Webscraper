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

vector<long long> ans;
long long curr_count=0;

void print_ans()
{
     int sz = ans.size();
     for(int i=1;i<=sz;i++)
     {
	  out<<"Case #"<<i<<": "<<ans[i-1]<<"\n";
     }
}



class dir{
    public:
    map<string,dir*> children;
    dir() 
    {
    children.clear();
    }
    void ins(string temp);


};

void dir::ins(string temp)
{

     vector<string> arr;
     int start = 1;
     int end; 
     do
     {
          end = temp.find_first_of("/",start);
	  arr.push_back(temp.substr(start,end-start));
          start = end+1;
     }while(end != string::npos);
		    int sz = arr.size();
		    dir* curr = this;
    for(int i=0;i<sz;i++)
    {
	    map<string,dir*>::iterator it = (curr->children.find(arr[i]));
	    if( it != curr->children.end() ) { curr = it->second; } 
	    else { dir* currnew = new dir(); curr->children[arr[i]] = currnew; curr=currnew;curr_count++; }
    }
}


int main()
{

     in.open("A-large.in");
     out.open("A-large.out");
     int T;
     in>>T;
     for(int i=0;i<T;i++) {
	  dir root;
	  long long N;
	  long long M;
	  in>>N;
	  in>>M;
	  for(int j=0;j<N;j++) {
	       string temp;
	       in>>temp;
	       root.ins(temp);
	  }
	  curr_count=0;
	  for(int k=0;k<M;k++) {
	       string temp;
	       in>>temp;
	       root.ins(temp);
	  }
	  ans.push_back(curr_count);

     }
     print_ans();
     in.close();
     out.close();
     return 0;
}

