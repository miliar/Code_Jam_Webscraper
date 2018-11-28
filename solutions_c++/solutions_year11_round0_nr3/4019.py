#include<fstream>
#include<iostream>
using namespace std;
int main()
{
     ifstream file1;
     file1.open("C-small-attempt0.in");
     ofstream file2;
     file2.open ("C-out-small.txt");
     char testcase[100];
     int t,a=1;
     file1 >> testcase;
     sscanf (testcase,"%d",&t);	 
     while(t--)
	 {
        int i=0,j,d[20],total,sum1,sum2,sum=0,temp,no,ans=-1;
        char total1[100];     
        file1 >> total;
        sscanf(total1,"%d",&total);	         
        
        long count=1; 
	    for(int k=0;k<total;k++)
	    {
                char digit[100];     
                file1 >> digit;
                sscanf(digit,"%d",&d[k]);	         	            
	            sum+=d[k];
        }
        while(i<count)
        {             
             sum1=0,sum2=0,temp=0,no=0;                 
			 for(int k=0;k<total;k++)
			 {
				 if((i&(1<<k)) > 0 )
				 {
					 sum1^=d[k]; 
					 temp=temp+d[k];
					 no++;
                 }
				 else 
				      sum2^=d[k];
	         }

             if(no!=0 && no!=total && sum1==sum2)
			 {			 
                int temp1=max(sum-temp,temp);
                if(temp1>ans)
                   ans=temp1;
		     }             
             if(i<total)
			    count=count*2;
			 i++;
	    } 		
		if(ans==-1)
			 file2 <<"Case #"<<a++<<": NO\n";
		else
			 file2 <<"Case #"<<a++<<": "<<ans<<"\n";
    } 
    file2.close();
    system("pause"); 
}
