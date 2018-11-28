#include<iostream>
#include<fstream>

using namespace std;

long eval(int,int,int,long *);

int main()
{
         int cases;
         int r,k,n;
         long carray[1000];
         
         ifstream fin;fin.open("input.txt",ios::in);
         fstream fout;fout.open("output.txt",ios::out);         
         fin>>cases;         

         for(int j=1;j<=cases;j++)
         {
                    fin>>r;fin>>k;fin>>n;
                    for(int i=0;i<n;i++)
                            fin>>carray[i];        
                    for(int l=0;l<n;l++)
                            cout<<carray[l];cout<<endl;        

                    fout<<"Case #"<<j<<": "<<eval(r,k,n,carray)<<endl;
         }  
               
         fin.close();
         fout.close();
         return 0;
}

long eval(int r,int k,int n,long *carray)
{
       int sum,costs=0,count=0,counter=0,ptr;
       for(int i=0;i<r;)
       {
            ptr=carray[count];
            if((sum+ptr)>k  ||  counter>=n)/*chacking for thre limit*/
            {
                costs=costs+sum;
                sum=0;
                counter=0;
                i++;
            }
            else
            {
                sum=sum+ptr;
                counter++;
                count=(count+1)%n;
            }
       }
       return costs;
}
