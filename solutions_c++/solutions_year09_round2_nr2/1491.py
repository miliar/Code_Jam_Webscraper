#include<iostream>
#include<algorithm>
using namespace std;



int main()

{
        int A[21],i,j,N,T,t,len; 
        cin>>T;
        for(t=1;t<=T;t++)
        {
                        
                scanf("%d",&N);
                for(i=0;N;i++)
                {
                       A[i]=N%10; 
                       N/=10;
                }
                len=i;
                bool flag=true;
                for(i=0;i<len-1;i++) if(A[i]) flag=false;
                cout<<"Case #"<<t<<": ";
                //cout<<len<<endl;
                for(i=0,j=len-1;i<j;i++,j--) 
                {
                        swap(A[i],A[j]);
                }
                
                if(next_permutation(A,A+len))
                {
                        for(i=0;i<len;i++) cout<<A[i];
                }
                /*else if(flag)
                {
                        for(i=len-1;i>=0;i--) cout<<A[i];            
                        cout<<"0";
                
                }
                else
                {
                        cout<<A[len-1]<<"0";
                        for(i=len-2;i;i--) cout<<A[i];            
                        cout<<A[0];
                }
                */
                else
                {
                        
                        A[len]=0;
                        for(i=0,j=len;i<j;i++,j--)  swap(A[i],A[j]);
                        next_permutation(A,A+len+1);
                        for(i=0;i<=len;i++) cout<<A[i];
                }
                cout<<endl;
                
       }
        return 0;
}
