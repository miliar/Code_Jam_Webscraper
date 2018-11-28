#include <stdio.h>
#include<stdlib.h>
#include<iostream>
#include<set>
#include<vector>
using namespace std;

int ans=-1;
int total_sum=0;
int array[1000];
int N;
void printc(int comb[], int k) {
	
	int i;
        int sum=0;
        int sum_S=0,sum_P=0;
        set<int>st;st.clear();
        for(int i=0;i<N;i++)
        {
          st.insert(i);
        }
	for (i = 0; i < k; ++i)
        {
              //printf("%d , ", comb[i] + 1 );
              sum+=array[comb[i]];
              sum_S^=array[comb[i]];
              st.erase(comb[i]);
        }
        for(set<int>::iterator it=st.begin();it!=st.end();it++)
        {
            sum_P^=array[*it];
        }
          
       if(sum_P!=0&&sum_S!=0&&sum_P==sum_S)
       {
          ans=max(ans,max(sum,total_sum-sum));
          //printf("%d %d ",sum_P,sum_S);
       }  
       //printf("%d %d ",sum_P,sum_S);
      
               
}

int next_comb(int comb[], int k, int n) {
	int i = k - 1;
	++comb[i];
	while ((i >= 0) && (comb[i] >= n - k + 1 + i)) {
		--i;
		++comb[i];
	}

	if (comb[0] > n - k) 
		return 0; 
	for (i = i + 1; i < k; ++i)
		comb[i] = comb[i - 1] + 1;

	return 1;
}

int main()
{
        FILE *p=fopen("input.in","r");
        FILE *p2=fopen("output.txt","w");
         
        int cases;
        //cin>>cases;
        fscanf(p,"%d",&cases);
        int cs=0;
        while(cases--)
        {
          
          //cin>>N;
          fscanf(p,"%d",&N);

          total_sum=0;
          ans=-1;
          for(int i=0;i<N;i++)
          {
            fscanf(p,"%d",&array[i]);
            total_sum+=array[i];
          }
          for(int i=2;i<=N;i++)
          {
	   int n = i,j; 
	   int k = n-1; 
	   int comb[100],c[100],l,b[100]; 

	
	



	  for (int i = 0; i < n; i++)
		comb[i] = i;

	
           for(int i=1;i<k;i++)
	    printc(comb, k);
	 
            while (next_comb(comb, k, n))
		printc(comb, k);
           }//for   

         if(ans==-1)
             fprintf(p2,"Case #%d: NO\n",++cs);
         else
             fprintf(p2,"Case #%d: %d\n",++cs,ans);

       }//while

   fclose(p);
   fclose(p2);

	return 0;
}

