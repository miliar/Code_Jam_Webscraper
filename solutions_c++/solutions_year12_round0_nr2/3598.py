#include<iostream>
using namespace std;
int main()
{
  int num_test =0;
  int no,su,p,score,v,b,counter=0;
  cin>>num_test;
  cin.ignore(1000,'\n');
  int testCaseIndex =0,proIndex=0;
   while(++testCaseIndex <= num_test)
   {
      cout<<"Case #"<<testCaseIndex<<": ";
      cin>>no>>su>>p; 
      //cout<<no<<"--"<<su<<"--"<<p;
      while(++proIndex <=no)
      {
	 cin>>score;
	 v=score%3;
	 b=score/3;
         if(v==0)
	 {
	    if(b>=p)
		++counter;
	    else if((su>0)&&(b>0)&&(b+1>=p))
		{++counter;--su;}
         }
         else if(v==1)
	 {
             if((b>=p)||(b+1>=p))
		++counter;
	     else if((su>0)&&(b+1>=p))
		{++counter;--su;}
	 }
	 else if(v==2)
	 {
	     if((b>=p)||(b+1>=p))
                ++counter;
	     else if((su>0)&&(b+2>=p))
		{++counter;--su;}
	 }   
      }
      cout<<counter<<endl;
      counter=0;
      proIndex=0;
   }
   return 0;
}

