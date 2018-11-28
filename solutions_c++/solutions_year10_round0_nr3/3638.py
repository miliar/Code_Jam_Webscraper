#include<iostream>
#include <fstream>
using namespace std;

int main()
{
      ofstream out("d:\\a2.txt"); 
  
  if(!out) { 
    cout << "Cannot open file.\n"; 

   } 


  ifstream in("d:\\C-small-attempt0.in"); 
  if(!in) { 
    cout << "Cannot open file.\n";  
    return 1; 
  } 
 
    long long origin,result=0,ptr=0,Index1=0,x1,test,K,size;
    long long *matrix;





    in>>x1;





    for(int p1=1;p1<=x1;p1++)


    {

            in>>test;
	in>>K;
	in>>size;
            
            matrix=(long long*)malloc(sizeof(long long)*size);




            for(int i=0;i<size;i++)
           


		 in>>matrix[i];
            
            ptr=0;            result=0;            Index1=0;
            



for(int i=0;i<test;i++)
            {



                    ptr=0;

                    origin=Index1;                    

		while(true)
                    {
                               
                               ptr+=matrix[Index1];
                               
                               if(ptr>K)                                 { ptr-=matrix[Index1];break;}
                               else

                               Index1=(++Index1)%size;
   
       if(Index1==origin)break;
                    }
                 
                    result+=ptr;
            }
            
            out<<"Case #";
out<<p1;
out<<": ";
out<<result<<endl;
    }
    
   
    return 0;
}
            
                               
                        
