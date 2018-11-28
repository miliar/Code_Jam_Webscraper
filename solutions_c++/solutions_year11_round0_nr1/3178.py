// Correct for small inputs-----Google Code jam 1




#include<iostream>
using namespace std;

#define N 150
int t,n;
struct my_data
{
       char r;
       int b;
}data[N];



int my_abs(int value)
{
    if(value<0)
    return -1*value;
    else 
    return value;
}



long calculate()
{
    int prev_o=1,prev_b=1;
    long time=0,need=0,mov_by_othr=0;
    char type;
    if(data[0].r=='O')
    {
       type='O';
       prev_o=data[0].b;
    }
    else
    {
        type='B';
        prev_b=data[0].b;
    }
        
    int i=1;
    mov_by_othr=data[0].b;
    time+=mov_by_othr;

    while(i<n)
    {
    
        while( i<n && data[i].r==type)
        {
           if(type=='O')
           {      
                  mov_by_othr+=my_abs((data[i].b-prev_o))+1;

                  time+=my_abs((data[i].b-prev_o))+1;
                  prev_o=data[i].b;
           }
           else
           {
                  mov_by_othr+=my_abs((data[i].b-prev_b))+1;
           
                  time+=my_abs((data[i].b-prev_b))+1;
                  prev_b=data[i].b;
           }    
                 
           i++;
           
         }
        if(i<n)
        { 
        type=data[i].r;
        
        if(type=='O')
        {
         need=my_abs(data[i].b-prev_o);
         if(mov_by_othr>=need)
         {
                        time++;//for pushing the button      
                        mov_by_othr=1;
         }
         else
         {
             
              time+=(need-mov_by_othr);
              time++; // for pushing
              mov_by_othr=need-mov_by_othr+1;   
         }
         prev_o=data[i].b;
        }
        else
        {
         need=my_abs(data[i].b-prev_b);
         if(mov_by_othr>=need)
         {
                        time++;//for pushing the button      
                        mov_by_othr=1;
         }
         else
         {
             
              time+=(need-mov_by_othr);
              time++; // for pushing
              mov_by_othr=need-mov_by_othr+1;   
         }
         prev_b=data[i].b;
         }   
         i++;
         }
         
       
       }
       
       return time;
}
       
    
int main()
{
    cin>>t;
    int i;
    
    int q=1;
    while(t-->=1)
    {
                 n=0;
                 memset(data,0,sizeof(data));
                 cin>>n;
                 for(i=0;i<n;i++)
                 {
                                 cin>>data[i].r>>data[i].b;
                 }               
                 
                 cout<<"Case #"<<q<<": "<<calculate();
                 cout<<endl;
                 q++;
    }
    cin>>i;
    return 0;
}
                 
