#include<iostream>
#include<vector>
#include<fstream>
using namespace std;


          vector<long long> array(3);
          vector<long long> t_array(3);
          
long long calc(long long i, long long j)
{
           if(j%i==0)
               return i;
           else
               return calc((j%i),i);
}

int main()
{
    
    long long C,i,j,temp,add,gcd;
    int N;
    ifstream fin;
    ofstream fout;
    fin.open("A-small.in");
    fout.open("A.out");
    fin>>C;
    for(i=0;i<C;i++)
    {
          fin>>N;

          for(j=0;j<N;j++)
                          fin>>array[j];
          sort(array.begin(),array.begin()+N);
          temp=array[0];
          //cout<<"\n "<<i+1<<" "<<temp;
          for(j=1;j<N;j++)
          {
                          
                    t_array[j]=array[j]-temp;  
          } 
               
          if(N==2)
          {
                  gcd=t_array[1];
            //      cout<<"\n"<<gcd<<endl;
          }else
          {
                  if(t_array[1]!=0) 
                  gcd=calc(t_array[1],t_array[2]);
                  else
                  gcd=t_array[2];
          }
          add=0;
          if(gcd!=0)
          if((array[0]%gcd)!=0)
          add=gcd-(array[0]%gcd);
          //cout<<"\n "<<i+1<<" "<<gcd<<endl;
          
          fout<<"Case #"<<i+1<<": "<<add<<"\n";
          
    }
    fin.close();
    fout.close();
    cout<<"Done";
   cin>>C;
   return 0;
}
