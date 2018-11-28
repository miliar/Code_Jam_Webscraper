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

struct WayAlt
{
   WayAlt(int _h, int _w, int _priority,int _alt):
   h(_h),w(_w),priority(_priority),alt(_alt){}
   WayAlt(int _priority):priority(_priority),alt(0){}
   int h,w;
   int priority;
   int alt;



};

bool operator<(const WayAlt &L,const WayAlt &R)
{
   if ( L.alt > R.alt)
   {
      return true;
   }
   else if ( ( L.priority < R.priority ) && ( L.alt == R.alt) )
   {
      return true;
   }
   return false;
}
struct Na : public WayAlt 
{
   Na(int _h, int _w,int _alt):WayAlt(_h,_w,4,_alt){}
};
struct Wa : public WayAlt
{
   Wa(int _h, int _w,int _alt):WayAlt(_h,_w,3,_alt){}
};
struct Ea : public WayAlt
{
   Ea(int _h, int _w,int _alt):WayAlt(_h,_w,2,_alt){}
};
struct Sa : public WayAlt
{
   Sa(int _h, int _w,int _alt):WayAlt(_h,_w,1,_alt){}
};

char l[27] = { 
   'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
   't','u','v','w','x','y','z'};

int lused = 1;

int myset[30] ;

#define CRD(x,y) x+y*101

void process(int H,int W,int alt[100][100], int basin[100][100])
{
   
   for (int h = 0 ; h <H ; ++h)
   {
      
      for (int w = 0 ; w<W; ++w)
      {
         {

         cout<<"h:"<<h<<",w:"<<w<<endl;
         for ( int _h = 0 ; _h< H ; ++_h)
         {
            for ( int _w = 0 ; _w < W ; ++_w)
            {
               cout << basin[_h][_w] << " ";
            }
            cout<<endl;
            //cin.get();
         }
         cout<<endl;
         }

         priority_queue<WayAlt> q;
         if ( h-1 >= 0 ) q.push(Na(h-1,w,alt[h-1][w]));
         if ( w-1 >= 0) 
            q.push(Wa(h,w-1,alt[h][w-1]));
         if ( w+1 < W) q.push(Ea(h,w+1,alt[h][w+1]));
         if ( h+1 < H) q.push(Sa(h+1,w,alt[h+1][w]));         
         
         if ( q.size() == 0)
         {
            basin[h][w] = lused;
            myset[basin[h][w]] = lused;
            lused++;
            cout<<"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"<<endl;
            return;
         }

         if ( alt[h][w] > q.top().alt ) 
         {

            if  (( basin[q.top().h][q.top().w] != 0 ) && 
               ( basin[h][w] != 0) )
            {
               {
                  cout<<"myset: [";
                  for (int z=0 ; z<30; ++z)
                  {
                     cout<<myset[z]<<", ";
                  }
                  cout<<"]"<<endl;
               }
               

               if ( myset[basin[h][w]] > myset[basin[q.top().h][q.top().w]])
               {
                  {
                     cout<<"c'h:"<<h<<",c'w:"<<w<<", q'h:"<<q.top().h<<", q'w:"<<q.top().w <<", basin[h][w]:"<<basin[h][w]<<", myset[basin[h][w]:"<<myset[basin[h][w]]<<", basin[q.top().h][q.top().w]:"<<basin[q.top().h][q.top().w]<<", myset[basin[q.top().h][q.top().w]]:" <<myset[basin[q.top().h][q.top().w]] <<endl;
                  }
                  
                  int tmp = myset[basin[h][w]];
                  for (int i = 0 ; i< 30 ; ++i)
                  {
                     
                     if (tmp == myset[i])
                     {
                        myset[i] = myset[basin[q.top().h][q.top().w]];
                     }
                  }                                   

               }
               else if ( myset[basin[h][w]] < myset[basin[q.top().h][q.top().w]])
               {
                  //myset[basin[q.top().h][q.top().w]] = myset[basin[h][w]];
                  int tmp = myset[basin[q.top().h][q.top().w]];
                  for (int i = 0 ; i< 30 ; ++i)
                  {                     
                     if (tmp == myset[i])
                     {
                        myset[i] = myset[basin[h][w]];
                     }
                  }                
               }

               cout<<"myset: [";
               for (int z=0 ; z<30; ++z)
               {
                  cout<<myset[z]<<", ";
               }
               cout<<"]"<<endl;

            }
            else if ( basin[q.top().h][q.top().w] != 0 )
            {
               
               basin[h][w] = basin[q.top().h][q.top().w] ;
               //myset[basin[h][w]].map.insert(make_pair(CRD(h,w),0));
               
            }
            else if ( basin[h][w] != 0)
            {
               basin[q.top().h][q.top().w] = basin[h][w];
               //myset[basin[h][w]].map.insert(make_pair(CRD(q.top().h,q.top().w),0));
            }
            else 
            {
               myset[lused ] = lused;
               //myset[lused].map.insert(make_pair(CRD(h,w),0));
               //myset[lused].map.insert(make_pair(CRD(q.top().h,q.top().w),0));
               basin[h][w] = lused;
               basin[q.top().h][q.top().w] = lused;
               
               ++lused;
            }
            
            
         }
         else //if ( alt[h][w] <= q.top().alt)
         {
            if (basin[h][w] == 0)
            {
               basin[h][w] = lused;
               myset[basin[h][w]] = lused;
               lused++;               
            }            
         }
      }
   }

}

int _tmain(int argc, _TCHAR* argv[])
{

   int basin[100][100]= {};
   int alt[100][100]={};
   
   int count = 0;
   cin>>count;
   //cin.get();   
   
   ofstream of("out.txt");
   for (int i = 0 ; i< count ; ++i)
   {

      memset(myset,0,sizeof(myset));
      memset(basin,0,10000);
      int H=0,W=0;
      cin >> H >>W;
      lused = 1;
      //cin.get();

      cout<<endl;
      for ( int h = 0 ; h< H ; ++h)
      {
         for ( int w = 0 ; w < W ; ++w)
         {
            int value;
            cin >> value;
            alt[h][w]=value;
            cout << value << " ";
         }
         cout<<endl;
         //cin.get();
      }
      cout<<endl;
      
      

      process(H,W,alt,basin);
      int sort_myset[30] = {};
      memcpy(sort_myset,myset,sizeof(myset));
      sort(sort_myset,sort_myset+30);
      hash_map<int,char> chrmap;
      int v = 0;
      int idx = 0;
      for ( int i = 0 ; i< 30 ; ++i)
      {
         if ( sort_myset[i]==0)
         {
            continue;
         }

         if (v<sort_myset[i])
         {
            
            v = sort_myset[i];
            chrmap.insert( make_pair(v,'a'+idx));
            idx++;
            
            
         }
      }

      cout<<"Case #"<<i+1<<": "<<endl;
      of<<"Case #"<<i+1<<": "<<endl;
      for ( int h = 0 ; h< H ; ++h)
      {
         for ( int w = 0 ; w < W ; ++w)
         {            
            char a = chrmap.find(myset[basin[h][w]])->second;
            cout << a<<" ";
            of <<a<<" ";
         }
         cout<<endl;
         of<<endl;
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

