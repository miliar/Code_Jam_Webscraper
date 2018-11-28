#include<fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
//vector < vector <int> > arr;
int arr[1000][1000];
int row,col;
int final[1000][1000];
ifstream inputf;
ofstream outputf;
int visited[1000][1000];
char ch_t;
char result[1000][1000];
void fun(int i,int j)
{
        int mini=999999999;
        int mini_indxi=-1;
        int mini_indxj=-1;
        visited[i][j]=1;
        if(i-1 >= 0)
        {
               if(!visited[i-1][j])
                                fun(i-1,j);
               if(arr[i-1][j]<mini)
               {
                  mini=arr[i-1][j];
                  mini_indxi=i-1;
                  mini_indxj=j;
               }
        }
        if(j-1 >= 0)
        {
               if(!visited[i][j-1])
                              fun(i,j-1);
               if(arr[i][j-1]<mini)
               {
                  mini=arr[i][j-1];
                  mini_indxi=i;
                  mini_indxj=j-1;
               }
        }
        
        if(j+1 < col)
        {
               if(!visited[i][j+1])
                              fun(i,j+1);
               if(arr[i][j+1]<mini)
               {
                  mini=arr[i][j+1];
                  mini_indxi=i;
                  mini_indxj=j+1;
               }
        }
        
        if(i+1 < row)
        {
               if(!visited[i+1][j])
                                fun(i+1,j);
               if(arr[i+1][j]<mini)
               {
                  mini=arr[i+1][j];
                  mini_indxi=i+1;
                  mini_indxj=j;
               }
        }
        
        if(mini_indxi != -1 && mini < arr[i][j])
        {
               final[i][j]=mini_indxi*1000+mini_indxj;
               //outputf << i <<"  "<<j<<"points to "<<mini_indxi<<"  "<<mini_indxj<<endl;
        }
}

char jump(int i,int j)
{
     char ret;
     visited[i][j] += 1;
     //outputf <<i <<"  "<<j<<"changes to"<<visited[i][j]<<endl;
     if(final[i][j]==-1)
     {        
           if(visited[i][j]==1)  
           {
                       result[i][j]=ch_t;  
                      ch_t++;
                      return result[i][j];
                       //outputf << i <<"  "<<j<<"  changes to "<< ret<<endl;
           }
           else
           {
               return result[i][j];
               //outputf << i<<" "<<j<<" returning " <<ret<<endl;
           }
     }

     ret=jump(final[i][j]/1000,final[i][j]%1000);
     //outputf << i<<" "<<j<<" returning " <<ret<<endl;
     return ret;
}
int main()
{
    int cn=0;
    char inputFilename[] = "B-large.in";
    char outputFilename[] = "output.list";
    inputf.open(inputFilename, ios::in);
    outputf.open(outputFilename, ios::out);
    inputf >> cn;
    
    for(int i1=1;i1<=cn;++i1)
    {
         for(int i=0;i<1000;i++)
                 for(int j=0;j<1000;j++)
                 {
                         final[i][j]= -1;
                         arr[i][j]=0;
                         visited[i][j]=0;
                         result[i][j]=0;
                 }
         ch_t='a';
         inputf >> row;
         inputf >> col;
         for(int i=0;i<row;i++)
         {
              for(int j=0;j<col;j++)
              {
                      int num;
                      inputf >> num;
                     arr[i][j]=num;
              }       
         }
         fun(0,0);
         ch_t = 'a';
         for(int i=0;i<row;i++)
                 for(int j=0;j<col;j++)
                         visited[i][j]=0;
                         
                         
         for(int i=0;i<row;i++)
                 for(int j=0;j<col;j++)
                 {
                                   result[i][j]=jump(i,j);
                                   //outputf << "("<<i <<"  "<<j<<")"<<result[i][j]<<endl;
                 }
         outputf << "Case #"<<i1<<":"<<endl;
          for(int i=0;i<row;i++)
          {
                  string st="";
                 for(int j=0;j<col;j++)
                         if(j==0)
                                 st=st+result[i][j];
                         else
                         {
                             st=st+ " ";
                              st += result[i][j];
                         }
                 outputf <<st<<endl;
          }
    }
    outputf.close();
    inputf.close();
    return 0;
}
