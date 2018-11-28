#include<iostream>
#include<fstream>
using namespace std;



void sel_sort(int sz,string *s)
{
     string min,temp;
     int i,j,pos=0;
     
     for(i=0; i < sz ; i++)
     {
       min = s[i];
       pos=i;
       for(j=(i+1) ; j<sz; j++)
       {
         if(min>s[j])
         {
           min = s[j];
           pos=j;
         }
       }
       temp = s[i];
       s[i] = s[pos] ;
       s[pos] = temp;
     }
}
                   
                   
string turn_plus_time(string a, int t)
{
      
       int time=0;
       time =  ( a[4]-'0') + (a[3]-'0')*10 ;
       time+=  (( a[1]-'0') + (a[0]-'0')*10 )*60 ;
       time = time + t;
       
       char *tstr;
       tstr=new char[5];
       sprintf(tstr,"%.2d:%.2d",time/60,time%60);
       string tii = tstr;
       return tii;
       
}

int  trains(string *dept, string *arr, int nd, int na,int turnaround)
{
     int i=0,j=0,no_of_tr=0;
     
     for(; nd!=0 ;)
     {
       if(na==0)
         break;
       
       if(dept[i]<turn_plus_time(arr[j],turnaround) )
       {
         i++;
         no_of_tr++;
           nd--;                       
       }
       else
       {
         i++;j++;
         na--;nd--;
       }
     }
     no_of_tr+= nd;
     return no_of_tr;
}

int main()
{
    string *adept, *aarr, *bdept, *barr;
    int n=0, turnaround=0, atob=0,i=0,btoa=0, no_of_tr_a=0, no_of_tr_b=0,nii;

    fstream fin,fout;
    fin.open("B-large.in",ios::in);
    if(!fin)
    {
      cout<<"error\n";
      return 0;
    }
    fout.open("B-largeout.out",ios::out);
    if(!fout)
    {
      cout<<"err opening file\n";
      return 0;
    }
      
     
    fin>>n;
    
    for(nii=0 ; nii<n ; nii++)
    {
    fin>>turnaround;
    
    fin>>atob;
    fin>>btoa;
    adept = new string[atob];
    aarr  = new string[btoa];
    bdept = new string[btoa];
    barr  = new string[atob];
    
    for(i=0;i<atob;i++)
    {
      fin>>adept[i];
      fin>>barr[i];
    }
    for(i=0 ; i<btoa ; i++)
    {
      fin>>bdept[i];
      fin>>aarr[i];
    }
    /*ad[0]= "09:00"; 
    ad[1]= "12:00";
        
    
    ba[0] = "09:01";
    ba[1] = "12:02";
    */
    sel_sort(atob,adept);
    sel_sort(btoa,aarr);
    sel_sort(btoa,bdept);
    sel_sort(atob,barr);
       
    no_of_tr_a = trains(adept, aarr, atob, btoa,turnaround); 
    no_of_tr_b = trains(bdept, barr, btoa, atob,turnaround);
    cout<<"Case #"<<nii+1<<": "<<no_of_tr_a<<" "<<no_of_tr_b<<endl; 
    fout<<"Case #"<<nii+1<<": "<<no_of_tr_a<<" "<<no_of_tr_b<<endl;
    
    }
    getchar();
    return 1;
}
