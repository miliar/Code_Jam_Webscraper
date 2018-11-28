#include <iostream>
#include <string>
#include <fstream>
#include <conio.h>
using namespace std;

//string valid[D], testCases[N];
int ans;

void doTestCase(int testCaseNo, string testCase, int L, string valid[], int D);
void processLevel(int l,int L, string combo, string level[], string valid[], int D, int testCaseNo);


int main()
{
    //string file;
    //cout<<"Enter input file name : ";
    //cin>>file;
    ifstream in("A-small.in");
    ofstream out("A-small.out");
    
    int L, D, N;
    in>>L>>D>>N;
    
  //  out<<"\t"<<L<<"\t"<<D<<"\t"<<N<<"\n";
    string valid[D], testCases[N];
    
    for(int i=0; i<D; i++)
    {
      in>>valid[i];
      //out<<valid[i]<<"\n";
    }
    
    for(int i=0; i<N; i++)
    {
      in>>testCases[i];
   //   cout<<testCases[i].substr(0,1);
      doTestCase(i, testCases[i], L, valid, D);
    //  getch();
      //out<<testCases[i]<<"\n";
      out<<"Case #"<<i+1<<": "<<ans<<"\n";
  
    }
    
    
    
    return 0;
    
}

void doTestCase(int testCaseNo, string testCase, int L, string valid[], int D)
{
  
  ans=0;
  
  string level[L];
  int l=0;
  for(int i=0; i<testCase.length(); i++)
  {
     
     if(testCase.substr(i,1)=="(")
     {
       int ipos=i+1;
       while(testCase.substr(i,1)!=")")   
       {
         // cout<<"\n"<<testCase.substr(i,1);
            i++;
       }
       //getch();
       int epos=i;
       level[l++] = testCase.substr(ipos,epos-ipos);
      // cout<<"\n level["<<l-1<<"] = "<<level[l-1];
       //getch();
     }
     else
     {
         level[l++]=testCase.substr(i,1);
     }
     
  } 
  
 // for(int i=0; i<l; i++)
  //{
    //cout<<"\n l = "<<l;
    //getch();
    //cout<<"\n level["<<i<<"] in testCase : "<<testCase<<"  = "<<level[i];
  //}
  //getch();
  
  processLevel(0, L, "",level, valid, D, testCaseNo);
  
  //cout<<"\n \n Case #"<<testCaseNo+1<<": "<<ans;
  //getch();
  
  return ;
}     


void processLevel(int l,int L, string combo, string level[], string valid[], int D, int testCaseNo)
{
     if(l==L-1)
     {
       for(int i=0; i<level[l].length(); i++)
       {
         //cout<<" \n l = "<<l;
         //getch();
         //cout<<"\n level[l] = "<<level[l]<<"  level[l].substr(i,1)  = "<<level[l].substr(i,1); 
         //getch();
         //cout<<"\n Permutation : "<<combo+level[l].substr(i,1);
         
         for(int j=0; j<D; j++)
         {
           if(combo+level[l].substr(i,1)==valid[j])
            ans++;
         }
       }
       
       
     }
     else
     {
         for(int i=0; i<level[l].length(); i++)
         {
           string s=combo+level[l].substr(i,1);
           //cout<<" \n l = "<<l;
         //getch();
         int check=0;
         for(int j=0; j<D; j++)
         {
           if(s==valid[j].substr(0,l+1))
           {
              check=1;
              break;
           }
         }
         if(check)
           processLevel(l+1, L, combo+level[l].substr(i,1), level, valid, D, testCaseNo);
      //   else
        //     cout<<"Disqualified";
         }
     }
     
     return;
     
}    
