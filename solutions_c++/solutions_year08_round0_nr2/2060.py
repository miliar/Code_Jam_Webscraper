#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;
int my_atoi(string str)
{
    int len;
    long int res;
    res=0;
    len=str.length()-1;
    for(int i=len; i>=0; i--)
    {
            res+=((int)(str[i]-'0'))*pow(10.0,len-i);
    }
    return(res);
}
void convert_min(string x,string y,int& timex,int& timey,int t)
{
     int pos;
     string sub1,sub2;
     
     sub1=x.substr(0,2);
     sub2=x.substr(3,2);
     timex=(my_atoi(sub1))*60 + my_atoi(sub2);
     sub1=y.substr(0,2);
     sub2=y.substr(3,2);
     timey=(my_atoi(sub1))*60 + my_atoi(sub2)+t;
}
void sort_it(int* tr,int size,int* tr1)
{
     int tmp;
     for(int i=0; i<size; i++)
        for(int j=i; j<size; j++)
        {
             if(*(tr+i)>*(tr+j))
             {
                  tmp=*(tr+i);
                  *(tr+i)=*(tr+j);
                  *(tr+j)=tmp;
             }
             if(*(tr1+i)>*(tr1+j))
             {
                  tmp=*(tr1+i);
                  *(tr1+i)=*(tr1+j);
                  *(tr1+j)=tmp;
             }
        }
}
int main(void)
{
    ifstream bin("B-large.in");
    ofstream bout("B-large.out");
    int number,na,nb,turn_time,tmp,numA,numB;
    
    bin>>number;
    for(int m=1; m<=number; m++)
    {
    bin>>turn_time>>na>>nb;
    numA=na;
    numB=nb;

    string depA[na],arr_fmA[na],depB[nb],arr_fmB[nb];
    int t_depA[na],t_arr_fmA[na],t_depB[nb],t_arr_fmB[nb];
    

    for(int i=0; i<na; i++)
    {
            bin>>depA[i]>>arr_fmA[i];
            convert_min(depA[i],arr_fmA[i],t_depA[i],t_arr_fmA[i],turn_time);
    }
    for(int i=0; i<nb; i++)
    {
            bin>>depB[i]>>arr_fmB[i];
            convert_min(depB[i],arr_fmB[i],t_depB[i],t_arr_fmB[i],turn_time);
    }
    sort_it(t_depA,na,t_arr_fmA);
    sort_it(t_depB,nb,t_arr_fmB);
    
              
 
    int i,pos=na-1;
    int j;
    for(i=nb-1; i>=0 ; i--)
    {
         for(j=pos; j>=0 ; j--)
         {
                 if( t_arr_fmB[i]<=t_depA[j] )
                 {
                     numA--;
                     pos=j-1;
                     break;
                 }
          }
      }
    pos=nb-1;  
    cout<<endl;
    for(i=na-1; i>=0 ; i--)
    {
         for(j=pos; j>=0 ; j--)
         {
                 if( t_arr_fmA[i]<=t_depB[j] )
                 {
                     numB--;
                     pos=j-1;
                     break;
                 }
          }
      }
      bout<<"Case #"<<m<<": "<<numA<<" "<<numB<<endl;
    }  
    bin.close();
    bout.close();
}
