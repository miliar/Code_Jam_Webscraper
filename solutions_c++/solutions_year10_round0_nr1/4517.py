#include <conio.h>
#include <iostream.h>
#include <fstream.h>
#include<alloc.h>


//Global variables
  int Power=1;
  int t,n,light;
  long k;

struct Snapper
{
       int State;
       int Input;
} *Current,*first,*last;

//############$$$$$$$$$$$$$$************
void viewchain()
{
     struct Snapper *temp;
     temp=first;
     for(int i=1;i<=n;i++)
     {
             cout<<temp->Input<<" "<<temp->State<<"\n";
             temp++;
     }
}

//############$$$$$$$$$$$$$$************

void Initialval()
{

     struct Snapper *temp;
     temp=first;
     for(int i=1;i<=n;i++)
     {
     temp->State=0;                //All Snappers Off Initially
     temp->Input=0;                 //All Inputs Off ----- Power not connected;
     temp++;
     }

     return;
}

void Setinputs()   //Sets new inputs according to new States and inputs
{
     Current=first;
     int i=0;
     for(i=1;i<=n;i++)                          //Until current snapper is OFF...after which none will have input as ON
     {  
             if((Current->State==1)&&(Current->Input==1))
             {
                  Current++;             //goto next snapper
                  Current->Input=1;      //next snapper input IS on
             }
             else
                 break;              //Break loop n any snapper giving output as OFF
     }
     
     for(;i<=n;i++)                  //All Following Snappers have Input as OFF
     {
             Current++;
             Current->Input=0;
     }
     return;
}

void changestate()
{
     if(Current->State==0)
         Current->State=1;
     else
         Current->State=0;
         
     return;
}


void snapped()
{
      Current=first;

     for (int i=1;i<=n;i++)
     {
         if(Current->Input==0)
         return;                   // If Input of Current snapper is OFF none of the next Snappers can have Input as On So Ignore any further change.
         else if((Current->Input)==1)
         {
              changestate();      // If input is ON Toggle State of Current Snapper
         }
         Current++;
     }
     return;
}


void Test()
{
    int i=1;
    while(i<=k)                 //For k Snaps
    {
    snapped();                 //Snapped figers
    Setinputs();               //Set new Input to each snapper

    i++;
    }
}

void checklight()
{
     if((last->Input==1)&&(last->State==1))
     light=1;
     else
     light=0;
}

int main()
{
    
  fstream Read,Write;
  Read.open("A-small-attempt0.in",fstream::in);        // input file A-small-attempt0.in
  Write.open("result.txt",fstream::out);      //Output file result.txt
  

  Read>>t;
  
  for(int c=1;c<=t;c++){
          
        Read>>n>>k;


        first=(struct Snapper *)malloc(sizeof(struct Snapper)*n); //first snapper
        last=first+(n-1);                                         //last snapper

        Initialval();//Initial State of snappers set        

        first->Input=Power; //Power to first snapper
        light=0;            //Light OFF initially

        Test();      // Test for n snappers and k snappings
        
        checklight(); //check light condition after check
        
        //Write the results
        Write<<"Case #"<<c<<": ";
        if(light==0)
              Write<<"OFF\n";
        else if (light==1)
              Write<<"ON\n";
              
        free(first);
  }
  Read.close();
  Write.close();
}
