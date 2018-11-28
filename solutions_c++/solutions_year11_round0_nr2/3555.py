#include<cstdio>
#include<cstdlib>
#include<vector>
#include<iostream>

using namespace std;

struct base_char{
       vector<char> combine;
       vector<char> combine_val;
       vector<char> oppose;
       int c_index;
       int o_index;
       };

int main()
{
    FILE* magic_inp = fopen("d:\\magic_inp.txt","r");
    FILE* magic_op = fopen("d:\\magic_op.txt","w");
    base_char Q, W, E, R, A, S, D, F;
    int test_cases;
    vector<char> inp;
    
    fscanf(magic_inp,"%d",&test_cases);
    
    int c,d,n,curr_case=1;
    char ch,ch1,ch2,ch3;
    
    while(test_cases--)
    {
         fscanf(magic_inp,"%d",&c);
         
         //intialization 
         inp.clear();
         Q.combine.clear();Q.oppose.clear();Q.c_index=0;Q.o_index=0;Q.combine_val.clear();
         W.combine.clear();W.oppose.clear();W.c_index=0;W.o_index=0;W.combine_val.clear();
         R.combine.clear();R.oppose.clear();R.c_index=0;R.o_index=0;E.combine_val.clear();
         E.combine.clear();E.oppose.clear();E.c_index=0;E.o_index=0;R.combine_val.clear();
         A.combine.clear();A.oppose.clear();A.c_index=0;A.o_index=0;A.combine_val.clear();
         S.combine.clear();S.oppose.clear();S.c_index=0;S.o_index=0;S.combine_val.clear();
         D.combine.clear();D.oppose.clear();D.c_index=0;D.o_index=0;D.combine_val.clear();
         F.combine.clear();F.oppose.clear();F.c_index=0;F.o_index=0;F.combine_val.clear();
         
         while((ch=fgetc(magic_inp))==' ')
         ;
         ungetc(ch,magic_inp);
         
         //read c strings
         for(int i=0;i<c;i++)
         {
                 fscanf(magic_inp,"%c%c%c",&ch1,&ch2,&ch3);
                 
                 while((ch=fgetc(magic_inp))==' ')
                 ;
                 ungetc(ch,magic_inp);
                 
                 switch(ch1)
                 {
                      case 'Q':
                           Q.combine.push_back(ch2);
                           Q.combine_val.push_back(ch3);
                           break;
                      case 'W':
                           W.combine.push_back(ch2);
                           W.combine_val.push_back(ch3);
                           break;
                      case 'E':
                           E.combine.push_back(ch2);
                           E.combine_val.push_back(ch3);
                           break;
                      case 'R':
                           R.combine.push_back(ch2);
                           R.combine_val.push_back(ch3);
                           break;
                      case 'A':
                           A.combine.push_back(ch2);
                           A.combine_val.push_back(ch3);
                           break;
                      case 'S':
                           S.combine.push_back(ch2);
                           S.combine_val.push_back(ch3);
                           break;
                      case 'D':
                           D.combine.push_back(ch2);
                           D.combine_val.push_back(ch3);
                           break;
                      case 'F':
                           F.combine.push_back(ch2);
                           F.combine_val.push_back(ch3);
                           break;
                 }
                 
                 switch(ch2)
                 {
                      case 'Q':
                           Q.combine.push_back(ch1);
                           Q.combine_val.push_back(ch3);
                           break;
                      case 'W':
                           W.combine.push_back(ch1);
                           W.combine_val.push_back(ch3);
                           break;
                      case 'E':
                           E.combine.push_back(ch1);
                           E.combine_val.push_back(ch3);
                           break;
                      case 'R':
                           R.combine.push_back(ch1);
                           R.combine_val.push_back(ch3);
                           break;
                      case 'A':
                           A.combine.push_back(ch1);
                           A.combine_val.push_back(ch3);
                           break;
                      case 'S':
                           S.combine.push_back(ch1);
                           S.combine_val.push_back(ch3);
                           break;
                      case 'D':
                           D.combine.push_back(ch1);
                           D.combine_val.push_back(ch3);
                           break;
                      case 'F':
                           F.combine.push_back(ch1);
                           F.combine_val.push_back(ch3);
                           break;
                 }
                 
         }
         //read c string ended
         
         while((ch=fgetc(magic_inp))==' ')
         ;
         ungetc(ch,magic_inp);
         
         fscanf(magic_inp,"%d",&d);
         
         while((ch=fgetc(magic_inp))==' ')
         ;
         ungetc(ch,magic_inp);
         
         //READ D STRINGS 
         for(int i=0;i<d;i++)
         {
                 fscanf(magic_inp,"%c%c",&ch1,&ch2);
                 
                 while((ch=fgetc(magic_inp))==' ')
                 ;
                 ungetc(ch,magic_inp);
                 
                 switch(ch1)
                 {
                      case 'Q':
                           Q.oppose.push_back(ch2);
                           Q.o_index++;
                           break;
                      case 'W':
                           W.oppose.push_back(ch2);
                           W.o_index++;
                           break;
                      case 'E':
                           E.oppose.push_back(ch2);
                           E.o_index++;
                           break;
                      case 'R':
                           R.oppose.push_back(ch2);
                           R.o_index++;
                           break;
                      case 'A':
                           A.oppose.push_back(ch2);
                           A.o_index++;
                           break;
                      case 'S':
                           S.oppose.push_back(ch2);
                           S.o_index++;
                           break;
                      case 'D':
                           D.oppose.push_back(ch2);
                           D.o_index++;
                           break;
                      case 'F':
                           F.oppose.push_back(ch2);
                           F.o_index++;
                           break;
                 }
                 
                 switch(ch2)
                 {
                      case 'Q':
                           Q.oppose.push_back(ch1);
                           Q.o_index++;
                           break;
                      case 'W':
                           W.oppose.push_back(ch1);
                           W.o_index++;
                           break;
                      case 'E':
                           E.oppose.push_back(ch1);
                           E.o_index++;
                           break;
                      case 'R':
                           R.oppose.push_back(ch1);
                           R.o_index++;
                           break;
                      case 'A':
                           A.oppose.push_back(ch1);
                           A.o_index++;
                           break;
                      case 'S':
                           S.oppose.push_back(ch1);
                           S.o_index++;
                           break;
                      case 'D':
                           D.oppose.push_back(ch1);
                           D.o_index++;
                           break;
                      case 'F':
                           F.oppose.push_back(ch1);
                           F.o_index++;
                           break;
                 }
                 
         }
         //READ D STRINGS ENDED
         
         while((ch=fgetc(magic_inp))==' ')
         ;
         ungetc(ch,magic_inp);
         
         fscanf(magic_inp,"%d",&n);
         
         //READ INPUT STRING
         while((ch=fgetc(magic_inp))==' ')
         ;
         ungetc(ch,magic_inp);
         
         fscanf(magic_inp,"%c",&ch);
         inp.push_back(ch);
         
         
         while((ch1=getc(magic_inp))!='\n' && ch1!=EOF)
         {
               char prev=-1;
               if(!inp.empty())
               {
                               prev = inp.back();
               }
               
               vector<char>::iterator it;
               bool flag = false;
               if(prev!=-1)
               {
               switch(prev)
                 {
                      case 'Q':
                           it = find(Q.combine.begin(),Q.combine.end(),ch1);
                           if(it!=Q.combine.end())
                           {
                               inp.pop_back();
                               inp.push_back(Q.combine_val[it-Q.combine.begin()]);
                               flag = true;
                           }
                           break;
                      case 'W':
                           it = find(W.combine.begin(),W.combine.end(),ch1);
                           if(it!=W.combine.end())
                           {
                               inp.pop_back();
                               inp.push_back(W.combine_val[it-W.combine.begin()]);
                               flag = true;
                           }
                           break;
                      case 'E':
                           it = find(E.combine.begin(),E.combine.end(),ch1);
                           if(it!=E.combine.end())
                           {
                               inp.pop_back();
                               inp.push_back(E.combine_val[it-E.combine.begin()]);
                               flag = true;
                           }
                           break;
                      case 'R':
                           it = find(R.combine.begin(),R.combine.end(),ch1);
                           if(it!=R.combine.end())
                           {
                               inp.pop_back();
                               inp.push_back(R.combine_val[it-R.combine.begin()]);
                               flag = true;
                           }
                           break;
                      case 'A':
                           it = find(A.combine.begin(),A.combine.end(),ch1);
                           if(it!=A.combine.end())
                           {
                               inp.pop_back();
                               inp.push_back(A.combine_val[it-A.combine.begin()]);
                               flag = true;
                           }
                           break;
                      case 'S':
                           it = find(S.combine.begin(),S.combine.end(),ch1);
                           if(it!=S.combine.end())
                           {
                               inp.pop_back();
                               inp.push_back(S.combine_val[it-S.combine.begin()]);
                               flag = true;
                           }
                           break;
                      case 'D':
                           it = find(D.combine.begin(),D.combine.end(),ch1);
                           if(it!=D.combine.end())
                           {
                               inp.pop_back();
                               inp.push_back(D.combine_val[it-D.combine.begin()]);
                               flag = true;
                           }
                           break;
                      case 'F':
                           it = find(F.combine.begin(),F.combine.end(),ch1);
                           if(it!=F.combine.end())
                           {
                               inp.pop_back();
                               inp.push_back(F.combine_val[it-F.combine.begin()]);
                               flag = true;
                           }
                           break;
                 }//switch(prev) ended
               }//if(prev!=-1) ended
         
               bool flag2=false;
               
               if(flag!=true && d!=0)
               {
                    switch(ch1)
                    {
                      case 'Q':
                           for(int h=0;h < Q.o_index ;h++)
                           {
                                   it = find(inp.begin(),inp.end(),Q.oppose[h]);
                                   
                                   if(it!=inp.end())
                                   {
                                   inp.clear();
                                   flag2 = true;
                                   break;
                                   }
                           }
                           break;
                      case 'W':
                           for(int h=0;h < W.o_index ;h++)
                           {
                                   it = find(inp.begin(),inp.end(),W.oppose[h]);
                                   
                                   if(it!=inp.end())
                                   {
                                   inp.clear();
                                   flag2 = true;
                                   break;
                                   }
                           }
                           break;
                      
                      case 'E':
                           for(int h=0;h < E.o_index ;h++)
                           {
                                   it = find(inp.begin(),inp.end(),E.oppose[h]);
                                   
                                   if(it!=inp.end())
                                   {
                                   inp.clear();
                                   flag2 = true;
                                   break;
                                   }
                           }
                           break;
                      
                      case 'R':
                           for(int h=0;h < R.o_index ;h++)
                           {
                                   it = find(inp.begin(),inp.end(),R.oppose[h]);
                                   
                                   if(it!=inp.end())
                                   {
                                   inp.clear();
                                   flag2 = true;
                                   break;
                                   }
                           }
                           break;
                      
                      case 'A':
                           for(int h=0;h < A.o_index ;h++)
                           {
                                   it = find(inp.begin(),inp.end(),A.oppose[h]);
                                   
                                   if(it!=inp.end())
                                   {
                                   inp.clear();
                                   flag2 = true;
                                   break;
                                   }
                           }
                           break;
                      
                      case 'S':
                           for(int h=0;h < S.o_index ;h++)
                           {
                                   it = find(inp.begin(),inp.end(),S.oppose[h]);
                                   
                                   if(it!=inp.end())
                                   {
                                   inp.clear();
                                   flag2 = true;
                                   break;
                                   }
                           }
                           break;
                      
                      case 'D':
                           for(int h=0;h < D.o_index ;h++)
                           {
                                   it = find(inp.begin(),inp.end(),D.oppose[h]);
                                   
                                   if(it!=inp.end())
                                   {
                                   inp.clear();
                                   flag2 = true;
                                   break;
                                   }
                           }
                           break;
                      
                      case 'F':
                           for(int h=0;h < F.o_index ;h++)
                           {
                                   it = find(inp.begin(),inp.end(),F.oppose[h]);
                                   
                                   if(it!=inp.end())
                                   {
                                   inp.clear();
                                   flag2 = true;
                                   break;
                                   }
                           }
                           break;
                 }//SWITCH(CH1) ENDED
               }//IF (FLAG!=TRUE) ENDED
               if(flag!=true && flag2!=true)
               inp.push_back(ch1);
         }
         //READ INPUT STRING ENDED
         fprintf(magic_op,"Case #%d: ",curr_case++);
         fprintf(magic_op,"[");
         fflush(magic_op);
         for(int k=0;k<inp.size();k++)
         {
                 fprintf(magic_op,"%c",inp[k]);
                 if(k!=(inp.size()-1))
                 fprintf(magic_op,", ");
         }
         fprintf(magic_op,"]\n");
         fflush(magic_op);
         
    }//WHILE(TEST_CASES--) ENDED
    fflush(magic_op);
}//INT MAIN() ENDED
