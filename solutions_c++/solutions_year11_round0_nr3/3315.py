#include<iostream>
#include<vector>
#include<cstdio>
#include<cstdlib>
using namespace std;
template <typename Iterator> inline bool next_combination(const Iterator first, Iterator k, const Iterator last)
 {    
   if ((first == last) || (first == k) || (last == k))  
     return false;  
  Iterator itr1 = first;
    Iterator itr2 = last;
    ++itr1;
    if (last == itr1)
       return false; 
        itr1 = last;
        --itr1;
        itr1 = k;
        --itr2; 
       while (first != itr1) 
       {     
          if (*--itr1 < *itr2)   
        {       
           Iterator j = k;
          while (!(*itr1 < *j)) ++j;
          std::iter_swap(itr1,j);
          ++itr1;
          ++j;
          itr2 = k; 

        std::rotate(itr1,j,last);    
      while (last != j)       
   {             ++j;       
      ++itr2;         
     }
          std::rotate(k,itr2,last); 
         return true;    
   }  
      }  
  std::rotate(first,k,last); 
   return false;
 } 
int main()
{
    freopen("C-large.in1.in","r",stdin);
    freopen("out1.txt","w",stdout);
    int T,TT=0;
    cin>>T;
    while(T--){
    TT++;
    long long sum=0,ts=0,n,k,t,xr,ma=-1,i;
    cin>>n; 
    std::vector<long long> ints; 
    for (i = 0; i < n; i++)
    {
        cin>>t;
        ints.push_back(t);
        sum+=t;
    }
    xr = ints[0];
    ma = ints[0];
    for(i=1;i<n;i++)
    {
        xr = xr ^ ints[i];
        if(ints[i]<ma)
        ma = ints[i];
    }
    if(xr!=0)
    cout<<"Case #"<<TT<<": NO\n";
    else
    cout<<"Case #"<<TT<<": "<<sum-ma<<endl;
    }
    return 0;
}
