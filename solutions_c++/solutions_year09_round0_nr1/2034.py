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
using namespace std;
using namespace stdext;
/*
struct Person
{
   int A;
   int B;
   int C;
};

struct TestCase
{
   vector<Person> people;
};



void compute( vector<TestCase> &testcases,vector<int> &result)
{
   int tcount = 0;
   for ( vector<TestCase>::iterator it = testcases.begin() ;
      it != testcases.end(); ++it)
   {
      cout<<"case "<<tcount<<", count "<<it->people.size()<<endl;
      set<int> runned;
      int myA = 0 , myB = 0 , myC = 0;
      int maxlike = 0;
      int pidx = 0;
      /*
      if (tcount != 9)
      {
         tcount++;
         continue;
      }
      */
/*
      for ( vector<Person>::iterator pit = it->people.begin() ;
         pit != it->people.end(); ++pit)
      {
         myA = pit->A; myB = pit->B; myC = pit->C;
         if (( myA+myB+myC )>10000) continue;         
         int pidx2 = 0;
         int plike = 1;
         for ( vector<Person>::iterator pit2 = it->people.begin() ;
            pit2 != it->people.end(); ++pit2)
         {
            if (pit == pit2) 
            { ++pidx2; continue; }
            //if (runned.find(pidx2) != runned.end()) { ++pidx2;continue; }

            int tmp1=0,tmp2=0,tmp3=0;
            if (myA < pit2->A)  tmp1 = pit2->A; else tmp1 = myA;
            if (myB < pit2->B)  tmp2 = pit2->B; else tmp2 = myB;
            if (myC < pit2->C)  tmp3 = pit2->C; else tmp3 = myC;

            if ( ( tmp1+tmp2+tmp3 ) > 10000 ) { ++pidx2;continue; }
            else 
            {

               ++plike;
               cout<<"-> "<<myA<<","<<myB<<","<<myC<<" |"<<plike<<endl;
               myA = tmp1; myB = tmp2; myC= tmp3;
            }
            
            ++pidx2;            
         }
         cout<<"Candidate -> A: "<<myA<<","<<myB<<","<<myC<<",Like "<<plike<<endl;
     
         int vlike =0;
         for ( vector<Person>::iterator oit = it->people.begin() ;
            oit != it->people.end(); ++oit)
         {
            if ( ( myA >= oit->A) && ( myB >= oit->B) && (myC>= oit->C) && 
               ( (myA+myB+myC) <= 10000 )
               )
            {
               ++vlike;
            }
         }
         cout<<"Verification -> A: "<<myA<<","<<myB<<","<<myC<<",Like "<<vlike<<endl;
         if ( vlike != plike)
         {
            cout<<"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"<<endl;
         }


         if (plike > maxlike) maxlike = plike;

         runned.insert(pidx);
         pidx++;
      }
      cout<<"Max like "<<maxlike<<endl;
      result.push_back(maxlike);


      tcount++;
   }
}
*/
void parse(const char* buf,size_t len,vector<hash_map<char,char>> &maps)
{
   const char *token =buf;
   bool push = false;
   hash_map<char,char> mymap;
   while ( (*token) !=0)
   {
      if ((*token)=='(')
      {
         ++token; push = true; continue;
      }
      else
      if ((*token)==')') 
      {
         if (push)
         {
            maps.push_back(mymap);
            mymap.clear();
            push = false;
         }
         else
         {
            assert(false);
         }
         ++token;
         continue;
      }
      mymap.insert( make_pair(*token,*token) );

      if ( !push )
      {
         maps.push_back(mymap);
         mymap.clear();
      }
      else
      {

      }
      ++token;
   }
}

int process (vector<string> &base, vector<hash_map<char,char>> &maps)
{
   int result = 0;
   for (vector<string>::iterator it = base.begin(); 
      it!=base.end(); ++it)
   {
      int count =0; bool allfind = true;
      if ( it->length() != maps.size() )
      {
         assert(false);
         continue;
      }
      for ( string::iterator sit = it->begin(); 
         sit!=it->end(); ++sit)
      {
         if (count < maps.size())
         {
            if (maps[count].find(*sit)==maps[count].end())
            {
               allfind = false;
               break;
            }
            ++count;
         }
         else
         {
            assert(false);
            allfind = false;
            break;
         }
      }
      if (allfind)
      {
         ++result;
      }
   }
   return result;
}

int _tmain(int argc, _TCHAR* argv[])
{
   int L =0 , D = 0 , N=0;
   cin>>L>>D>>N;
   cin.get();
   /*
   char buf[100];
   cin.get(buf,100,' ');
   L =atoi(buf);
   cin.get(buf,100,' ');
   D =atoi(buf);
   cin.get(buf,100,' ');
   N =atoi(buf);*/
   
   vector<string> base;
   for (int i = 0 ; i<D ; ++i)
   {
      char buf[17] ={};
      cin.getline(buf,16);
      base.push_back( string(buf) );
   }

   ofstream of("out.txt");
   for (int i = 0 ; i < N ; ++i)
   {
      vector<hash_map<char,char>> maps;
      char buf[1024]={};
      cin>>buf;
      parse(buf,1024,maps);
      
      cout<<"Case #"<<i+1<<": "<<process(base,maps)<<endl;
      of<<"Case #"<<i+1<<": "<<process(base,maps)<<endl;
   }



   /*
   int count = 0;
   cin>>count;
   
   vector<TestCase> testcases;
   

   for (int i = 0 ; i< count ; ++i)
   {
      TestCase testcase;
      int people_count;
      cin >> people_count;
      
      for (int j = 0 ; j < people_count ; ++j)
      {
         char buf[100];
         Person p;
         cin.get(buf,100,' ');
         p.A = atoi(buf);
         cin.get();
         cin.get(buf,100,' ');
         p.B = atoi(buf);
         cin.get();
         cin.get(buf,100);
         p.C = atoi(buf);

         testcase.people.push_back(p);
      }            
      testcases.push_back(testcase);
   }

   vector<int> result;
   compute(testcases,result);

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

