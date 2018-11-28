#include <iostream>s
#include <cstdio>
#include <cmath>
#include <deque>
#include <vector>

using namespace std;

////file selection 
void SetInputFile()
{ char filename[32], infile[32], outfile[32]; scanf("%s", filename);
  strcpy(infile, filename); strcpy(outfile, filename); strcat(infile, ".in"); strcat(outfile, ".out");
  freopen(infile, "r", stdin); freopen(outfile, "w", stdout);
}

long long testcase,cases=1;
long long r,k,n,value;

vector< vector<long long> >mylists;
vector< long long > popedTotal;
deque<long long> mydeque;
long long total,multiple;
long isExists(long index)
{
     long long size_1 = mylists[index].size();
     long long j =0;
     for(long long i = 0; i!=index; i++)
     {
        long long size_2 = mylists[i].size();
        if(size_1==size_2)
        {
                          
          for(j=0;j<size_2;j++)                 
            if(mylists[i][j]!=mylists[index][j])
              break;
          if(j==size_2)
           return i;
        }
     }
     
     return -1;
}

int main()
{
    SetInputFile();
    
	long long i;
    scanf("%lld",&testcase);
    cases=1;
    
        
    while(testcase--)
    {
      scanf("%lld%lld%lld",&r,&k,&n);
	  mydeque.clear();
      mylists.clear();
	  popedTotal.clear();
      
      for(i=0;i<n;i++)
      {
        scanf("%lld",&value);
        mydeque.push_back(value);
      }
      
      total=0;multiple=0;
      for(i=0;i<r;i++)
      {
		 long long count=0;
		 long long sizeLimit = mydeque.size();
		 while(true && sizeLimit--)
         {			
            value = mydeque[0];
            if(count+value<=k)
            {
			   count += value;
               mydeque.pop_front();
			   mydeque.push_back(value);			   
            }
            else
                break;
         }
		 popedTotal.push_back(count);
		 
		 vector<long long> smalllist;
		 mylists.push_back(smalllist);
		 for(long long j =0; j<mydeque.size(); j++)
			mylists[i].push_back(mydeque[j]);
			  

         value = isExists(i);
         if(value!=-1)
         {
		   value++;
           total=0;
           for(long long inner = 0;inner<value;inner++)
           {
			   total+=popedTotal[inner];
           }
           
           multiple = (r - value) / (i - value + 1);
           
		   if(multiple!=0)
		   {			   
			   for(long long inner = value;inner <= i;inner++) 
	           {			     
				  total+=popedTotal[inner] * multiple;
		       }
			}

           long long modu = (r - value) % (i - value + 1);
           
		   if(modu!=0)
		   for(long long inner = value;inner<value+modu;inner++)
           {
              total+=popedTotal[inner];
           }

		   printf("Case #%lld: %lld\n",cases++,total);
           break;

         }         
      }

	  if(i==r)
	  {
		  for(long long inner = 0;inner<mylists.size();inner++)
           {
             total+=popedTotal[inner];
           }
		  printf("Case #%lld: %lld\n",cases++,total);
	  }
      
    }
   
} 
