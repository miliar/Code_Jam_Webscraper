#include<iostream>
#include<cmath>
#include<fstream>
using namespace std;


int condition(int a[])
{
    for(int i=18;i>=0;i--)
    {
            if(a[i]!=0)
            return i;
    }
    return -1;
}



int main()
{
    int n;
    
    string check,c="welcome to code jam";
    //cout<<c[18]<<endl;
    int a[19];
    for(int i=18;i>=0;i--)
    a[i]=0;
    ifstream in;
    in.open("input.txt");
    ofstream out;
    out.open("output.txt");
    
    
    in>>n;
    getline(in,check);
    for(int i=0;i<n;i++)
    {
          for(int l=18;l>=0;l--)
          a[l]=0;
            
          getline(in,check);
          int j=0,m=0,word=0,l=0,b=0;  
          //cout<<check<<endl; 
          
          
          
          if(check[0]=='w')
          while(true){
          int r=condition(a);
          /*if(i==1)
          {cout<<r<<endl;
          system("pause");}*/
          if(r!=-1 || m==0)
          {
                  if(m!=0)
                  {j=a[r]+1;l=r;a[r]=0;}
                  else {j=1;l=0;}
                  m=1;
          }
          else break;
          while(check[j]!='\0')
          {
                               
                               //cout<<"gunjan"<<endl;
                               if(check[j]==c[l] && l!=18)
                               {
                                                 a[l]=j;
                                                 
                                                 //cout<<check[j];
                                                 l++;
                               }
                               if(check[j]=='m' && l==18)
                               {word=(word+1)%10000;}//cout<<word<<endl;}//system("pause");}
                               //a[i]=
                               j++;
                                                 
          }
          
          
          }
          for(int l=18;l>=0;l--)
          a[l]=0;m=0;
          while(true){
          int r=condition(a);
          
          if(r!=-1 || m==0)
          {
                  if(m!=0)
                  {j=a[r]+1;l=r;a[r]=0;}
                  else {j=0;l=0;}
                  m=1;
          }
          else break;
          while(check[j]!='\0')
          {
                               
                               //cout<<"gunjan"<<endl;
                               if(check[j]==c[l] && l!=18)
                               {
                                                 a[l]=j;
                                                 
                                                 //cout<<check[j];
                                                 l++;
                               }
                               if(check[j]=='m' && l==18)
                               {word=(word+1)%10000;}//cout<<word<<endl;}//system("pause");}
                               //a[i]=
                               j++;
                                                 
          }
          
          
          }
          if(word>999)
          out<<"Case #"<<i+1<<": "<<word<<endl;
          else
          {
              string st="";
              if(word==0)
              st=48;
              j=0;
              while(word!=0)
              {
                            int r=word%10;
                            word=word/10;
                            r=r+48;
                            char cc=r;
                            st=cc+st;
                            j++;
              }
              if(j==3)
              st='0'+st;
              else if(j==2)
              st="00"+st;
              else
              st="000"+st;
              out<<"Case #"<<i+1<<": "<<st<<endl;
          }
            
            
    }
    
    
    
    
    in.close();
    out.close();
    system("pause");
    return 0;
}
