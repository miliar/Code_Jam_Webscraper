#include<iostream>
 #include<fstream>
 #include<vector>
using namespace std;


int N=0;
//int o_arr[200]={0};
//int b_arr[200]={0};
//int seq_arr[200]={0};

int b_count=0,o_count=0;
int o_pointer=0 ,b_pointer=0,seq_pointer=0;          //store indexes


int T=0;
void emptyAllArray();
vector<int> seq_arr;
vector<int> b_arr;
vector<int> o_arr;
int main()
{
    
    
   ifstream inputFile("A-large.in");
   ofstream outFile("A-large.out");
   inputFile>>T;
   
   for(int J=0;J<T;J++)     //iterate T times
    {       
    N=0;
    inputFile>>N;
    
    for(int i=0;i<N;i++)
    {
     char char_val=0;
    inputFile>>char_val;
    
    int int_val=0;
    inputFile>>int_val;
    
    if(char_val=='O')
       {
        o_arr.push_back(int_val);       
        seq_arr.push_back(1);
        
       }
        
        else if(char_val=='B')
        {
        b_arr.push_back(int_val);       
        seq_arr.push_back(2);
        }
    
    
    }//single step For Loop 
    
    
    cout<<endl<<"orange:";
         for(int i=0;i<o_arr.size();i++)
         {
            cout<<o_arr[i]<<":";
            
                 
         }
         
         cout<<endl<<"blue:";
         for(int i=0;i<b_arr.size();i++)
         {
            cout<<b_arr[i]<<":";
            
                 
         }
         
         cout<<endl<<"sequence:";
         for(int i=0;i<seq_arr.size();i++)
         {
            cout<<seq_arr[i]<<":";
            
                 
         }
    
         cout<<endl;
         
         
         
         
         //================================================
         
        o_pointer=0;b_pointer=0;seq_pointer=0;
          int o_cur=1, b_cur=1;
         int o_next=0, b_next=0;
         o_next=o_arr[o_pointer];
         b_next=b_arr[b_pointer];
         
          int calcd_time=0;
    while(seq_pointer<seq_arr.size())
         {
          int pushed_flag=0;
          
          // cout<<endl<<"--"<<seq_pointer<<endl;
           
           //cout<<"o:"<<o_cur<<"o_next-"<<o_next<<endl;
           //cout<<"b:"<<b_cur<<"b_next-"<<b_next<<endl;
           
          
          
           if(o_cur!=o_next&&o_pointer<o_arr.size())
           {
               
               if(o_cur>o_next)
                    o_cur--;
               else if(o_cur<o_next)
                    o_cur++;
                                       
                  
              
           }   
           else if(seq_arr[seq_pointer]==1)
           {
              
              pushed_flag=1;
                o_pointer++;
                o_next=o_arr[o_pointer];
                
                            
                
           }          
           
           if(b_cur!=b_next&&b_pointer<b_arr.size())
           {
               if(b_cur>b_next)
                   b_cur--;
               else if(b_cur<b_next)
                    b_cur++;
                         
              
           }   
           else if(seq_arr[seq_pointer]==2)
           {
                pushed_flag=2;
                
                b_pointer++;
                b_next=b_arr[b_pointer];
                
           }          
                             
              calcd_time++;
              if(pushed_flag>0)seq_pointer++;
          //cout<<calcd_time;
          
          
          }
          
       //=====================================================   
          
          
          cout<<"Case #"<<J+1<< ": "<<calcd_time<<endl;
         outFile<<"Case #"<<J+1<< ": "<<calcd_time<<endl;
          
          
          
          
          
          
      
    
    
    //========================================================
    o_arr.clear();b_arr.clear();seq_arr.clear();
    }// main for Loop
    
    
    
  //================================================  
  inputFile.close();
  outFile.close();  
 system("pause");   
}
