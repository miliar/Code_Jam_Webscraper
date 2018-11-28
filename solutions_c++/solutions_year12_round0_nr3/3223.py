#include<iostream>
#include<fstream>
using namespace std;
ifstream fin;
ofstream fout;
int main()
{
    fin.open("input.txt");
    fout.open("q1output.txt");
    int T,A,B;
    fin>>T;
    int df=T;
    int t[1000][5]={0};
    for(int i=12;i<=1000;i++)
    {
       if(i<100)
       {
          if(((i%10)*10+i/10)>i)
          t[i][0]=(i%10)*10+(i/10);
       }
       else
       {
           int a,b,c;
           a=i%10;
           b=(i/10)%10;
           c=i/100;
           if((a*100+c*10+b)>i)
           t[i][0]=a*100+c*10+b;
           if((b*100+a*10+c)>i)
           {
              if(t[i][0]>0)
              t[i][1]=b*100+a*10+c;
              else
              t[i][0]=b*100+a*10+c;
           }
       }
    }
    while(T--)
    {
        int count=0;      
        fin>>A>>B;
        for(int i=A;i<=B;i++)
        {
           if(t[i][0]>0&&t[i][0]<=B)
           count++;
           if(t[i][1]>0&&t[i][1]<=B)
           count++;
        }
        fout<<"Case #"<<(df-T)<<": "<<count<<endl;
    }
    
    return 0;
} 
