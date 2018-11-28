#include<iostream>
#include<fstream>

using namespace std;

int i,j,k,case_no,size,surp,minp,mean,mod,surpno,mincheck,sum,flag,n;
int A[100]={0},B[100][3]={0};

main()
{ifstream fin;
 fin.open("input.txt");
 ofstream fout;
 fout.open("output.txt");
 fin>>case_no;
 for(i=0;i<case_no;i++)
     {surpno=0;
      sum=0;
      fin>>size>>surp>>minp;
      for(j=0;j<size;j++)
         fin>>A[j];
      for(j=0;j<size;j++)
         {flag=0;
          mean=A[j]/3;
          mod=A[j]%3;
          mincheck=mean+2;
          B[j][0]=B[j][1]=B[j][2]=mean;
          if(!mod&&mean)
             {if(surpno<surp&&minp==(mean+1))
                {B[j][1]++;B[j][2]--;surpno++;}
             } 
          if(mod==2)
             {if(surpno<surp&&minp==mincheck)
                {B[j][2]=mean+2;surpno++;}
              else
                {B[j][1]++;B[j][2]++;}
             }
          if(mod==1) 
             B[j][2]++;
         for(k=0;k<3;k++) 
            {if(B[j][k]>=minp)
                 flag=1;
            }
         if(flag)
             sum++;
        }
      fout<<"Case #"<<i+1<<": "<<sum<<endl;
      
     }
 fin.close();
 fout.close();
} 
      
      
      
      
      
      
      
      
      
