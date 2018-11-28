#include<iostream>
#include<fstream>
#include <algorithm>

using namespace std;


int main()
{
  ifstream in("4-large.in");
  ofstream out("answer.txt");
  out.setf(ios::showpoint);
  int test= 1;
  int N, T, X= 0, I;
  int count= 0;
  in>>T;
  while(X!=T)
             {
              in>>N;
              int arr[N], arr1[N];
              for(int i=0; i<N; i++)
                       {
                           in>>arr[i]; 
                           arr1[i]= arr[i];
                       }
              for(int i= 0; i< N; i++)
                      for(int j= 0; j<i; j++)
                              {
                               if(arr1[i]<arr1[j])
                                                  {
                                                   int temp= arr1[i];
                                                   arr1[i]= arr1[j];
                                                   arr1[j]= temp;
                                                  }
                              }
             for(int i= 0; i< N; i++)
                     if(arr[i]!= arr1[i])
                                  count++;
             
             cout<<count<<endl;
             double ans= count*1.0000000;
             out<<"Case #"<<test<<": "<<ans<<endl;
             count= 0; 
             test++;

                          
              X++;
             }
    system("pause");
    return 0;
}
