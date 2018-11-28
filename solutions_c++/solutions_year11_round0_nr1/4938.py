
#include<iostream>
#include<cstdio>
#include<fstream>
#include<string>
using namespace std;

 class bot{
     public:  int cur_pos;
       int que[300];
       int que_in;
            
       bot()
       {
            cur_pos=1;
            que_in=-1;
            }
       
       };


string line;
int Eval(int N,int i,string l);
int N,ttime[20];
int main()
{
 
       ifstream myfile;
       myfile.open("A-small-attempt3.in");
       getline(myfile,line);
       int T=line[0]%48;
      
      if(line[1]!=' ');
      T=10*T+line[1]%48;
      
      int eprev=0;
      int enew;
      int req; 
      
       ofstream ourfile("output.txt",ios::app);
       for(int i=1;i<=T;i++)
       {
               getline(myfile,line);
               if(line[1]!=' ')
               N=10*(line[0]%48)+line[1]%48;
        
         enew=Eval(N,i,line);
         //req=enew-eprev;
         //eprev=enew;
         ourfile<<"\n Case #"<<i<<": "<<enew;
               
         }
myfile.close();
ourfile.close();
system("pause");
return 0;
    }

int Eval(int N,int i,string l)
{
     bot o;
     bot b;
     int len=l.length();
     int ar[3],arlen=-1,ocount=0,bcount=0; 
     char order[200],orin=-1;  
                          
         for(int j=1;j<len;j++)
         {
                 if(l[j]=='O')
                 {
                  ocount++; 
                   order[++orin]='O';
                   j=j+2;
                   while(l[j]>='0'&&l[j]<='9')
                   {
                     ar[++arlen]=l[j++]%48;                         
                                              }           
                              
                          if(arlen==0)
                          o.que[++o.que_in]=ar[0];
                          else if(arlen==1)
                          o.que[++o.que_in]=ar[0]*10+ar[1];
                          else if(arlen==2)
                          o.que[++o.que_in]=100;
                          
                          arlen=-1;
                          
                              }
                            
                              if(l[j]=='B')
                 {
                   bcount++;
                   order[++orin]='B';
                   j=j+2;
                   while(l[j]>='0'&&l[j]<='9')
                   {
                     ar[++arlen]=l[j++]%48;                         
                                              }           
                              
                          if(arlen==0)
                          b.que[++b.que_in]=ar[0];
                          else if(arlen==1)
                          b.que[++b.que_in]=ar[0]*10+ar[1];
                          else if(arlen==2)
                          b.que[++b.que_in]=100;
                          
                          arlen=-1;
                          
                              }
                 
                 
                 }   
                 order[++orin]='\0';   
            
            
        //ACTUAL EXECUTON 
        static int intervals[20][10];int in=0;    
        
                
     int opos=0,bpos=0;
     for(int h=0;h<orin;h++)
     {
      int dif=0;
      
      if(order[h]=='O')
      {
        if(o.cur_pos>o.que[opos])
        {
            dif=o.cur_pos-o.que[opos];
            o.cur_pos=o.que[opos];
            opos++;
                                 }
        else if(o.cur_pos<o.que[opos])
        {
             dif=o.que[opos]-o.cur_pos;
             o.cur_pos=o.que[opos];
             opos++;             
                     }
            
        else if(o.cur_pos==o.que[opos])
            {
            opos++;
            dif=0;              
            }          
       intervals[i][in++]=dif+1;
     
       
                    
       
       if(b.que[bpos]>b.cur_pos)               
       {
            if(b.que[bpos]>b.cur_pos+intervals[i][in-1])
            b.cur_pos+=intervals[i][in-1];                                
             else
             b.cur_pos=b.que[bpos];
                                              }                
       else if(b.que[bpos]<b.cur_pos)
       {
          if(b.que[bpos]<b.cur_pos-intervals[i][in-1])
          b.cur_pos=b.cur_pos-intervals[i][in-1];
          else
          b.cur_pos=b.que[bpos];
            
            }
      
                                       }
                                       //HERE COMES B
       if(order[h]=='B')
       {
                        if(b.cur_pos>b.que[bpos])
                            {
                                 dif=b.cur_pos-b.que[bpos];
                                 
                                 b.cur_pos=b.que[bpos];
                                 bpos++;
                                 }
        else if(b.cur_pos<b.que[bpos])
        {
             dif=b.que[bpos]-b.cur_pos;
             b.cur_pos=b.que[bpos];
             bpos++;             
            }
            
            else if(b.cur_pos==b.que[bpos])
            {
            bpos++;
            dif=0;              
            }          
       intervals[i][in++]=dif+1;
      
                    
       
       if(o.que[opos]>o.cur_pos)               
       {
            if(o.que[opos]>o.cur_pos+intervals[i][in-1])
            o.cur_pos+=intervals[i][in-1];                                
             else
             o.cur_pos=o.que[opos];
                                              }                
       else if(o.que[opos]<o.cur_pos)
       {
          if(o.que[opos]<o.cur_pos-intervals[i][in-1])
          o.cur_pos=o.cur_pos-intervals[i][in-1];
          else
          o.cur_pos=o.que[opos];
            
            }
                     
                        
                        }                             
        
         
         
             }
             ttime[i]=0;
              for(int k=in;k>=0;k--)
              ttime[i]= ttime[i]+intervals[i][k];  
             
    return ttime[i];                      
     
     }
