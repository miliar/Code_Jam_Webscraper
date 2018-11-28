#include<iostream>
#include<fstream>
#include<math.h>
#include<stdlib.h>

using namespace std;

void mydata();
void find();
int T=0;
int N,p,S;
int google[100];
int googler[100];
char letter;
int counter=0;
int lp;
ifstream first("c:/users/chaturvedi/desktop/small.in");
int main()
{
      mydata();
}     
void mydata()
{
      cout<<"the contents of file are : ";
      while(1)
      {
      first.get(letter);
      if(letter!=10)
      T=(T*10)+((int) letter)-48;
      else
      break;
      cout<<T<<"\n";                     
      }
      while(first)
      {
      for(lp=0;lp<T;lp++)
      find();   
      }    
}

void find()
{
     int small1,small2;
     N=p=S=0;
     while(1)
      {
      first.get(letter);
      if(letter!=32)
      N=(N*10)+((int) letter)-48;
      else
      break;
      }
      while(1)
      {
      first.get(letter);
      if(letter!=32)
      S=(S*10)+((int) letter)-48;
      else
      break;
      }
      while(1)
      {
      first.get(letter);
      if(letter!=32)
      p=(p*10)+((int) letter)-48;
      else
      break;
      }
      for(int i=0;i<N;i++)
      {
      google[i]=0;
      while(1)
              {
              first.get(letter);
              if(letter!=32 && letter!=10 && first.eof()==0)
              google[i]=(google[i]*10)+((int) letter)-48;
              else
              break;
              
              }         
      }
      googler[0]=0;
      small1=(3*p)-2;
      small2=abs(small1-2);
      for(int k=0;k<N;k++)
      {
      if(google[k]>=small1)
      counter++;
      else if(google[k]>=small2&&S>0)
           {
           counter++;
           S--;
           }
      } 

      ofstream second("c:/users/chaturvedi/desktop/out.in",ios::app);
      second<<"Case #";
      second<<lp+1;
      second<<": ";
      second<<counter;
      second<<"\n";
      counter=0;
      if(first.eof()!=0)
      {
      first.close();
      second.close();
      exit(0);
      }     
}
