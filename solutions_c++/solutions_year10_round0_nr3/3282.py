#include<iostream>
#include<fstream>

using namespace std;

long calc(int,int,int,long *);

int main()
{
         int num;
         int r,k,n;
         long cost;
         long array[1000];
         
         fstream fin,fout;
         fin.open("input.txt",ios::in);         
         fout.open("output.txt",ios::out);         
         fin>>num;         

         for(int j=1;j<=num;j++)
         {
                    fin>>r;fin>>k;fin>>n;
                    for(int i=0;i<n;i++)
                    {
                            fin>>array[i];        
                    }
                    for(int l=0;l<n;l++)
                            cout<<array[l];cout<<endl;        
                    cost=calc(r,k,n,array);
                    
                    fout<<"Case #"<<j<<": "<<cost<<endl;
         }  
               
         fin.close();
         fout.close();cin>>num;
         return 0;
}

long calc(int r,int k,int n,long *array)
{
       int sum,cost=0,count=0,counter=0,mov_ptr;
       for(int i=0;i<r;)
       {
            mov_ptr=array[count];
            if((sum+mov_ptr)>k  ||  counter>=n)/*chacking for thre limit*/
            {
                cost=cost+sum;
                sum=0;
                counter=0;
                i++;
            }
            else
            {
                sum=sum+mov_ptr;
                counter++;
                count=(count+1)%n;
            }
       }
       return cost;
}
