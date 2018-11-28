#include <string>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <valarray>
#include <bitset>
#include <iostream>
#include <cctype>

using namespace std;

bool encuentra(vector <string> general,string cadena)
 {   int cont=0;
	for(int a=0;a<general.size();a++)
	{
		if(cadena==general[a])
			{
            cont ++;
            break;}
	}
 return cont;
 }
 void inserta_en(vector <string> &nuevo,vector <string> general,string cad)
 {
	if(encuentra(general,cad))
	{
		if(!encuentra(nuevo,cad))
			nuevo.push_back(cad);
	
	}
 
 
 }
 
int main()
{
    int N,i=1;
    cin>>N;
    while(N>0)
    {
       int S,Q;
       
       vector < string > general,mien;
       string pal,cad2;
       cin>>S;
	   getline(cin,pal);
       while(S>0)
       {
       getline(cin,pal);
       general.push_back(pal);
       S--;
       }  
	sort(general.begin(),general.end());
       cin>>Q;
       getline(cin,cad2);
       int cuenta=0;

	   while(Q>0)
	   {
	   getline(cin,cad2);
	   inserta_en(mien,general,cad2);
	   	sort(mien.begin(),mien.end());
	   if(mien==general)
	   {
	 
	   mien.clear();
	   //cout<<mien.size()<<endl;
	   mien.push_back(cad2);
	     cuenta++;
	   }
	   Q--;
	   }
      cout<<"Case #"<<i<<": "<<cuenta<<endl;
	  i++;
     N--;           
    }
    //system("pause");
    return 0;
   }
