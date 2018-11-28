#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
    ifstream in("B-large.in");
    ofstream out("B-large.out");
    int T;
    in>>T;
    
    //cout<<"T = "<<T<<"\n";
    
    for(int i=0; i<T; i++)
    {
      
     int H, W;
      in>>H>>W;
      int len=H*W;

      //cout<<"len= "<<len<<"\n";  
      int alt[H+2][W+2];
      for(int k=0;k<W+2;k++)
      {
        alt[0][k]=20000;
        alt[H+1][k]=20000;
      }
      for(int j=0; j<H+2; j++)
      {
        alt[j][0]=20000;
        alt[j][W+1]=20000;
      }
      int sink0[len];
      int sink[len];
      
      for(int j=1; j<H+1; j++)
        for(int k=1; k<W+1; k++)
          in>>alt[j][k];
      
      //for(int j=1; j<H+1; j++)
      //{  for(int k=1; k<W+1; k++)
          //cout<<alt[j][k]<<"\t";
          
          //cout<<"\n";
      //}
      
      for(int j=1; j<H+1; j++)
        for(int k=1; k<W+1; k++)
        {
          int sink=((j-1)*(W))+k-1;
          int al = alt[j][k];
          if(al>alt[j-1][k])
           {
              //sink= ((j-1)*(W+2))+k;
              sink = sink0[((j-2)*W)+k-1] ;   
              al=alt[j-1][k];
           }
          if(al>alt[j][k-1])
          {
              //sink= (j*(W+2))+(k-1);    
             sink= sink0[((j-1)*W)+k-2];
              al=alt[j][k-1];
           }
           if(al>alt[j][k+1])
           {
              sink= ((j-1)*(W))+k;
              al=alt[j][k+1];
           }
           if(al>alt[j+1][k])
           {
             sink= ((j)*(W))+k-1;    
              al=alt[j+1][k];
           }
           //cout<<"((j-1)*W) = "<<((j-1)*W)<<"\n";
           int index = ((j-1)*W)+(k-1);
           sink0[index]=sink;
          // cout<<index<<"\n";
           for(int l=0; l<index; l++)
           {
              
              if(sink0[l]==index)
                 sink0[l]=sink0[index];
              
        //      cout<<sink0[l]<<"\t";
           }
      //     cout<<sink0[index]<<"\n";            
        }
    
    
    int valDone[30]={20000};
    int vDone = 0;
    int start = (int)('a');
    sink[0]=start;
    valDone[vDone++]=sink0[0];
    
    //cout<<"sink : "<<"\n";
    for(int l=1; l<len; l++)
    {
         if(sink0[l]==sink0[0])
           sink[l]=sink[0];
      //   cout<<sink[l]<<"\t";
    }
    //cout<<"\n";
         
    for(int m=1; m<len; m++)
    {
       int done=0;
       for(int j=0; j<30; j++)
         if(sink0[m]==valDone[j])
           done=1;
       
     //  cout<<"done = "<<done;
           
       if(!done)
       {
          valDone[vDone++] = sink0[m];
          sink[m]=++start;
          for(int k=m+1; k<len; k++)
            if(sink0[k]==sink0[m])
              sink[k]=sink[m];
              
       }
       
    }
    
    out<<"Case #"<<i+1<<":"<<"\n";
    
    for(int n=0; n<len; n++)
    {
      if((n+1)%W==0)
        out<<(char)sink[n]<<"\n";
      else
        out<<(char)sink[n]<<"\t";
    }   
  }
    
    return 0;
}

