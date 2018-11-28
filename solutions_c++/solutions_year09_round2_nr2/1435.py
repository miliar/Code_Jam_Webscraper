// template.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <vector>
#include <bitset>
#include <set>
#include <fstream>
#include <hash_map>
#include <cassert>
#include <queue>
#include <list>
using namespace std;
using namespace stdext;

void get(const string &a,vector<string> &b)
{
   if (a.length()==1)
   {
      b.push_back(a);
      return;
   }
   vector<string> myset;
   for (int i = 0 ; i<a.length(); ++i)
   {
      myset.clear();
      string input;
      for ( int j = 0 ; j <a.length(); ++j)
      {
         if ( j!= i)
         {
            input += a[j];
         }
      }
      get(input,myset);

      for ( vector<string>::iterator it = myset.begin();
         it!=myset.end() ; ++it
         )
      {
         string cc= a[i]+*it;
         b.push_back(cc);
      }
   }
}

long long process(long long a)
{
   char buf[2048]={};
   _itoa_s(a,buf,10);
   int len = strlen(buf);
   
   vector<string> myset;
   get(buf,myset);

   unsigned long long min=-1;
   for ( vector<string>::iterator it = myset.begin();
      it!=myset.end() ; ++it
      )
   {
      if ( (*it)[0]=='0')
      {
         continue;
      }
      unsigned long long l = atoi( (*it).c_str() );
      if ( a >= l)
      {
         continue;
      }
      else 
      {
         if (min > l)
         {
            min = l;
         }
      }
   }

   if (min==-1)
   {
      string next = buf;
      next+="0";
      int nextlen = next.length();
      vector<string> nextset;
      get(next,nextset);

      
      for ( vector<string>::iterator it = nextset.begin();
         it!=nextset.end() ; ++it
         )
      {
         if ( (*it)[0]=='0' )
         {
            continue;
         }
         unsigned long long l = atoi( (*it).c_str() );
         
            if (min > l)
            {
               min = l;
            }
         
      }
   }

   return min;
}

int _tmain(int argc, _TCHAR* argv[])
{
  
   int count = 0;
   cin>>count;     
   cin.get();

   ofstream of("out.txt");
   for (int i = 0 ; i< count ; ++i)
   {      
      long long a;
      cin >> a;

           
      long long result = process(a);
      of<<"Case #"<<i+1<<": "<<result<<endl;      
      cout<<"Case #"<<i+1<<": "<<result<<endl;      
      

   }



   /*
   ofstream of("out.txt");
   int aa = 1;
   for ( vector<int>::iterator it = result.begin() ;
         it != result.end(); ++it)
   {
      of<<"Case #"<<aa<<": "<<*it<<endl;
      aa++;
   }
   */
	return 0;
}

