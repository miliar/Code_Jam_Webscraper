#include<iostream>
#include<fstream>
#include<math.h>

using namespace std;

int i,j,k,case_no,a,b,sum,newn,n,size,p;
double l;

main()
{ifstream fin;
 fin.open("input.txt");
 ofstream fout;
 fout.open("output.txt");
 fin>>case_no;
 for(i=0;i<case_no;i++)
     {fin>>a>>b;
      sum=0;
      for(j=a;j<=b;j++)
        {n=j;
         newn=0;
         for(size=0;n;size++,n/=10);
         size--;
         p=size;
         n=j;
         while(p)
           {newn=n%10;
            l=pow(10,size);
            newn=newn*l;
            newn+=n/10;
            if(newn>j&&newn<=b)
              {sum++;
               if(i==3)
                 cout<<j<<":"<<newn<<endl;
              }
            p--;
            n=newn;
           }
        }
      fout<<"Case #"<<i+1<<": "<<sum<<endl;  
     }
 fin.close();
 fout.close();
 cin.get();
}

      
      
      
      
      
      
      
      
      
      
