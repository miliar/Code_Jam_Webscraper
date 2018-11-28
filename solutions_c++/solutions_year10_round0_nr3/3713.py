#include<iostream>
//#include<conio.h>
using namespace std;
int n; 
int fanswer;

int func(int r,int k,int arr[])
{
    int sum=0;
    int index=0;
    int t=0;
  if(r>0)     
  {
        while(1)
        {
               sum+=arr[index++];
//               fanswer+=sum;
               if(sum>k)
               {       
                index--;        
                break;
               }
        }      
        
  // shift the array      
//        index--;
        int *temp=new int[index];
        int counter=0;
        t=index;
//         cout<<t<<endl<<endl;
        while(t>0)
        {
              temp[counter]=arr[counter];
              fanswer+=temp[counter];
//              cout<<temp[counter]<<endl;
              counter++;
              t--;                      
        }
        
        int first=0;
        while(first<(n-index))
        {
                arr[first]=arr[first+index];
                first++;              
        }

        counter=0;
        while(first<n)
        {
               arr[first++]=temp[counter++];       
        }
  }
/*  for(int i=0;i<n;i++)
   cout<<arr[i]<<"  ";
   cout<<endl;
*/   
   r--;
   if(r>0)
   func(r,k,arr);
}

int main()
{
    int N;
    int r,k;
     int z=1;    
    cin>>N;
    
while(N>0)
{    

    cin>>r>>k>>n;
    
    int *arr=new int[n];
    for(int i=0;i<n;i++)
     cin>>arr[i];
     
     {
               N--;
               func(r,k,arr);                  
               cout<<"Case #"<<z++<<": ";   
               cout<<fanswer<<endl;
               fanswer=0;
     }
}     
//cout<<fanswer;
return 0;
}
