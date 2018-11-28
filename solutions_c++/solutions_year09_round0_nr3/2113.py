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
#include <iomanip>
using namespace std;
using namespace stdext;

//const char *S ="jam";
const char *S ="welcome to code jam";
const int SLEN = strlen(S);

//const char *S ="welcome";
//const int SLEN = 7;
int cache[501] ={};
int clen[501] = {};

int c[20][501];

const bool DEBUG = false;

const bool enable_cache = false;

const bool all =false;

int process( char data[501], int si, int idx, int len)
{
   
   if (DEBUG)
   cout<<"process( si:"<<si<<"="<<S[si]<<", idx"<<idx<<"="<<data[idx]<<")"<<endl;
   
   if (enable_cache)
   {
      /*
      if (DEBUG)         
         cout<<"cache["<<idx<<"]:"<<cache[idx]<<", SLEN-si="<<SLEN-si<<", clen["<<idx<<"]:"<<clen[idx]<<endl;
         */
      /*
      if (( cache[idx] != -1) && (( SLEN-si )==clen[idx]))
      {
         if (DEBUG)
         {
            cout<<"hit cache["<<idx<<"], clen["<<idx<<"]:"<<clen[idx]<<endl;

         }

         return cache[idx];
         
      }
      */
   }
   
    

   int result = 0;
   int firstMeet = -1;
   for ( int i = idx ; i < len ; ++i)
   {     

      if (S[si] == data[i]) 
      {
         //if (DEBUG)
         //cout<< "find data["<<i<<"] = "<< data[i]<<endl;
         if (firstMeet == -1)
         {
            firstMeet = i;
         }

         if ( ( si + 1 ) == SLEN )
         {      
            /*
            cache[i] = 1;
            clen[i] = 1;
            */
            result +=1;
            continue;
         }
         else if ( ( i+1 ) == len )
         {
            break;
         }

         int tmp = 0;
         
         if (!all)
         {
            if ( c[si+1][i+1] !=-1 )
            {

               if (DEBUG) cout<<"Hit process( , si:"<<si+1<<", i:"<<i+1<<")"<<endl;
               tmp = c[si+1][i+1];
            }
            else
            {
               tmp = process( data, si+1, i+1, len);
            }
         }
         else
         {
            tmp = process( data, si+1, i+1, len);
         }

         

         
         
         if (DEBUG)
         {
            /*
            cout<<"< cache:";
            for (int j=0 ; j<len ;++j)
            {
               cout<<j<<":"<<cache[j]<<" ";
            }
            cout<<endl;

            cout<<"< clen:";
            for (int j=0 ; j<len ;++j)
            {
               cout<<j<<":"<<clen[j]<<" ";
            }
            cout<<endl;
*/
         }
         
         
         
         //cache[i] =tmp;
         //clen[i]= SLEN - si;
         result += tmp;
/*
         if (DEBUG)
         {
            cout <<" cache["<<i<<"] <="<<tmp<<endl;
            cout <<" clen["<<i<<"] <="<<SLEN - si<<endl;
            cout<<" result =="<<result<<endl;
         }
  */       
         
         if ( result > 10000)
         {
            result %= 10000;
         }
         

      }

   }
   /*
   if (firstMeet != -1)
   {
      if (DEBUG) cout <<"firstMeet cache["<<firstMeet<<"] <="<<result<<endl;
      cache[firstMeet] = result;
   }
   */
   if (DEBUG)
      cout<<"< process( si:"<<si<<"="<<S[si]<<", idx"<<idx<<"="<<data[idx]<<") : result"<<result<<endl;

   c[si][idx] = result;
   return result;
   
}

int _tmain(int argc, _TCHAR* argv[])
{
   
   int count = 0;
   cin>>count;
   cin.get();
   
   
   char data[501] ={};
   ofstream of("out.txt");
   for (int i = 0 ; i< count ; ++i)
   {
      //memset(cache,-1,sizeof(cache));
      //memset(clen,-1,sizeof(clen));
      memset(data,0,sizeof(data));
      memset(c,-1,sizeof(c));
      cin.getline(data,501)  ;
      
      int result = process(data,0,0,strlen(data));
      cout<<"Case #"<<i+1<<": "<<std::setw(4)<<std::setfill('0')<<result<<endl;
      of<<"Case #"<<i+1<<": "<<std::setw(4)<<std::setfill('0')<<result<<endl;
      if (DEBUG)
      {
         /*
         cout<<"cache:";
      for (int j=0 ; j<strlen(data) ;++j)
      {
         cout<<j<<":"<<cache[j]<<" ";
      }
      cout<<endl;

      cout<<"clen:";
      for (int j=0 ; j<strlen(data) ;++j)
      {
         cout<<j<<":"<<clen[j]<<" ";
      }
      cout<<endl;
      */
      }
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

