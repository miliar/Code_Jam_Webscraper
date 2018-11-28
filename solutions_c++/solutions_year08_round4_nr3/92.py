// BEGIN CUT HERE
#include "stdafx.h"
// END CUT HERE
#include <map>
#include <set>
#include <sstream>
#include <iostream>
#include <list>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <queue>

using namespace std; 


vector<string> parse(string input, string search = " ",bool write_empty = false){
  vector<string> result;
  if (search.size() == 0){
    result.push_back(input);
    return result;
  }
  string temp = "";
  for(int i =0; i<input.length(); ++i){
    if(find(search.begin(),search.end(),input[i])!=search.end()){
      if (temp.size()!=0 || write_empty)
        result.push_back(temp);
      temp = "";
    } else {
      temp+=input[i];
    }
  }
  if(temp!="")
  result.push_back(temp);
  return result;
} 
#define sz 2001
 		int mod1 = 1000;
		int mod2 = 1000000;        

		void scanint(string &s, int& n){
			sscanf(s.c_str(),"%d",&n);
		}



    int main()
        {
			freopen("f:\\input.in", "r", stdin);
			freopen("f:\\output.txt", "w+", stdout);
		string s;
		cin>>s;
		int nn;
		sscanf(s.c_str(),"%d",&nn);


       for(int it=0;it<nn;++it)
       {
               printf ("Case #%d: ", it+1);

               int n;
               cin >> n;

               vector<int> x(n), y(n), z(n);
               vector<long double> p(n);

               for(int i=0;i<n;++i){
					cin >>s;
					int tmp;
					scanint(s,tmp);
					x[i] = tmp;
					cin >>s;
					scanint(s,tmp);
					y[i]=tmp;
					cin>>s;
					scanint(s,tmp);
					z[i]=tmp;
					cin >> p[i];
               }

               long double d1 = 0;
               long double d2 = 1e9;

			   for(int cc=0; cc<=300; ++cc)
               {
					long double d = (d1+d2)/2.;
					long double c11,c12,c21,c22,c31,c32,c41,c42;
					c11= -1e11; c12 = 1e11; c21 = -1e11; c22 = 1e11; c31 = -1e11; c32 = 1e11; c41 = -1e11; c42 = 1e11;

					for(int i=0;i<n;++i) {
						c11 = max(c11, -d*p[i] +x[i]+y[i]+z[i]);
						c21 = max(c21,-d*p[i] + x[i]+y[i]-z[i]);
						c31 = max(c31,-d*p[i] + x[i]-y[i]+z[i]);
						c41 = max(c41,-d*p[i] + x[i]-y[i]-z[i]);

						c12 = min(c12, d*p[i] +x[i]+y[i]+z[i]);
						c22 = min(c22,d*p[i] +x[i]+y[i]-z[i]);
						c32 = min(c32, d*p[i] + x[i]-y[i]+z[i]);
						c42 = min(c42, d*p[i] +x[i]-y[i]-z[i]);
					}

					if (!(c11<=c12 && c21<=c22 && c31<=c32 && c41<=c42))
						d1 = d;
					else
						d2 = d;
				}
			   double res = (d1+d2)/2.;
			   char buf[20];
			   sprintf(buf,"%.6lf", res);
			   cout<<string(buf)<<endl;
			}

        } 
    // C:\Documents and Settings\Dmitry\My Documents\Visual Studio 2005\Projects\problem\problem\problem.cpp
