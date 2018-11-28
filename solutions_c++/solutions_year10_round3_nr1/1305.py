/* Created by Anjuta version 1.2.4a */
/*	This file will not be overwritten */

#include <iostream>
#include <vector>
#include <algorithm>

#define FOR(A,B,C)   for(int A=B;A<C;A++)
#define PB push_back


using namespace std;

struct Point
{
 int x,y;
}pp;
	
int Solve(vector <Point> Inp)
{

  int Result =0;	 
 while(Inp.size()!=0)
 {
  FOR(i,1,Inp.size())
  {
    if(Inp[i].x<Inp[0].x && Inp[i].y<Inp[0].y) {}
	else if(Inp[i].x>Inp[0].x && Inp[i].y>Inp[0].y) {}
    else		
    Result=Result+1;
  
  }
  Inp.erase(Inp.begin(),Inp.begin()+1);
 }
 return Result;
} 

int main()
{
	int tc;
	cin>>tc;
	FOR(i,0,tc)
	{ 
	 vector <Point> Input;	
	 int wires;
         cin>>wires;
	 FOR(j,0,wires)	 
	 {  
           Point pp;
           cin>>pp.x>>pp.y;
          Input.PB(pp);
	 }
	 cout<<"Case #"<<i+1<<": "<<Solve(Input)<<"\n";
      }
}
    	 
      		 
 
