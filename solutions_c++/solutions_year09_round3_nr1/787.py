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

hash_map<char,int> valuemap;

long long process(const string& a)
{
   hash_map<char,int> map;
   vector<int> myvalues;
   int v = 2,maxv=1;
   string s;

   bool usezero = false;
   for (int i = 0 ; i < a.length() ; ++i)
   {
      if (i == 0)
      {
         map.insert( make_pair(a[i],1));
         myvalues.push_back(1);
         continue;
         
      }
      else
      {
         int x = v;
         bool isfind= false;
         hash_map<char,int>::iterator find_it = map.find(a[i]);
         if (find_it!=map.end())
         {
            x = find_it->second;
            isfind = true;
               
         }
         else
         {
            if (!usezero)
            {
               map.insert( make_pair(a[i],0));
               myvalues.push_back(0);
               usezero = true;
               continue;
            }
         }

         myvalues.push_back(x);

         if (!isfind)
         {
            if (maxv<v)
            {
               maxv = v;
            }
            map.insert( make_pair(a[i],v++));
         }         
      } 

   }

   int base = maxv+1;
   int pos = myvalues.size()-1;

   long long sum = 0;

   for ( vector<int>::iterator it = myvalues.begin() ;
      it!=myvalues.end(); ++it)
   {
      long long v = 1;

      if (pos != 0 )      
      {
         for (int j =0 ; j<pos ; ++j)
         {
            v = v * base;
         }
      }
      
      sum += (*it) * v;
      //cout << "pos:"<< pos <<", base value :"<<v<<endl;
      //cout << "value"<<(*it)<<", sum:"<<sum;
      --pos;
   }


   return sum;
}

int _tmain(int argc, _TCHAR* argv[])
{
  
   for (int i = 0 ; i<10; ++i)
   {
      valuemap.insert( make_pair( (char)48+i, i ));
   }

   int x = 10;
   for (int i = 97 ; i<123 ;++i)
   {
      valuemap.insert( make_pair( (char)i,x++) );
   }

   int count = 0;
   cin>>count;     
   cin.get();

   ofstream of("out.txt");
   for (int i = 0 ; i< count ; ++i)
   {      
      //long long a;
      string s;
      cin >> s;

           
      long long result = process(s);
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

