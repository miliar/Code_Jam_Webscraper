#include<iostream>
#include<conio.h>
#include<cstring>
using namespace std;
int main()
{
    int l; //number of letters in the words
    int d; //number of words in the language
    int n; //number of test cases
    int iIndex,iIndex2,iIndex3;
    int aray;
    cin>>l>>d>>n;
    char letters[5000][16];
    char testcase[20][30];
    char string[600];
    int count=0;
    int flag;

    for(iIndex=0;iIndex<d;iIndex++) //taking the words in the language
    {
      cin>>letters[iIndex];
    }
    for(iIndex=0;iIndex<n;iIndex++) //taking the testcases input
    {
      cin>>string;
      count=0;
      for(iIndex2=0;string[iIndex2]!='\0';iIndex2++)
         {
            if(string[iIndex2]=='(')
            {
               aray=0;
               iIndex2++;
               while(string[iIndex2]!=')')
               {                                              
                  testcase[count][aray]=string[iIndex2];
                  iIndex2++;
                  aray++;
               }
               testcase[count][aray]='\0';
               count++;                                                                                                  
            }
            else
               {
                  testcase[count][0]=string[iIndex2];
                  testcase[count][1]='\0';
                  count++;
               }
         }
         count=0;
         for(iIndex2=0;iIndex2<d;iIndex2++)
         {
               flag=1;
               for(iIndex3=0;iIndex3<l;iIndex3++)
               {
                  if(strchr(testcase[iIndex3],(int)letters[iIndex2][iIndex3])==NULL)
                     flag=0;
               }
               if(flag)
                  count++;
         }
         cout<<"Case #"<<(iIndex+1)<<": "<<count<<endl;                      
    }

    getch();
    return 0;    
}
