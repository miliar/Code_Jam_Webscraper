#include<iostream>
#include<fstream>
#include <iomanip>
#include<vector>

using namespace std;

int main()
{
 int T,N,temp;   
 ifstream in;
 in.open("D-large.in");
 ofstream out;
 out.open("output.txt");
 out.setf(ios::showpoint);
 in>>T;
 
         for(int i=0;i<T;i++)
         {
          in>>N;
          int arr[N];
          vector<int> vec;
          for(int j=0;j<N;j++)
          {
           in>>arr[j];
           vec.push_back(arr[j]);     
          }    
          sort(vec.begin(),vec.end());
          int temp[N];
          for(int k=0;k<N;k++)
          {
           temp[k]=vec[k];
          }
          
          double res=0.000000;
          for(int l=0;l<N;l++)
          {
           if(arr[l]==temp[l]){}
           else
           {
               res++;
           }       
          }
          out<<"Case #"<<i+1<<": "<<res<<endl;
          
         }
 
         in.close();
         out.close();
 
 
 
 system("pause");
 return 0;
}
