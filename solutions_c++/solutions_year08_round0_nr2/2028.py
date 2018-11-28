#include<iostream>
#include<fstream>
using namespace std;



void sort(string *s, int size)
{
     string min,temp;
     int pos=0,i,j;
     
     for(i=0; i < size ; i++)
     {
              pos=i;
             min = s[i];
             for(j=(i+1) ; j<size; j++)
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
                   
                   
string calturn(string a, int t)
{
      
       int time=0;
       time = (a[3]-'0')*10 + (a[4]-'0') ;
       time = time + ((a[0]-'0')*10 + (a[1]-'0'))*60 ;
       time = time + t;
       
       char *ti;
       ti=new char[5];
       sprintf(ti,"%.2d:%.2d",time/60,time%60);
       string tii =ti;
       return tii;
       
}

int  traincalc(string *d, string *a, int nd, int na,int turnaround)
{
     int i=0,j=0,notr=0;
     
     while(nd!=0)
     {
       if(na==0)
         break;
       
       if(d[i]>=calturn(a[j],turnaround) )
       {
         na--;
         nd--;
         i++;
         j++;
       }
       else
       {
           notr++;
           nd--;
           i++;
       }
       
     }
     notr+= nd;
     return notr;
}

int main()
{
    string *ad, *aa, *bd, *ba;
    fstream fin,fout;
    fin.open("B-large.in",ios::in);
    if(!fin)
    {
      cout<<"error\n";
      return 0;
    }
    fout.open("blarge.out",ios::out);
    string lin;
    
    
    int n=0, turnaround=0, btoa=0,i=0,atob=0, nta=0, ntb=0,q;
    fin>>n;
    
    for(q=0 ; q<n ; q++)
    {
    fin>>turnaround;
    
    fin>>atob;
    fin>>btoa;
    ad = new string[atob];
    aa = new string[btoa];
    bd = new string[btoa];
    ba = new string[atob];
    
    for(i=0;i<atob;i++)
    {
      fin>>ad[i];
      fin>>ba[i];
    }
    for(i=0 ; i<btoa ; i++)
    {
      fin>>bd[i];
      fin>>aa[i];
    }
    /*ad[0]= "09:00"; 
    ad[1]= "12:00";
        
    
    ba[0] = "09:01";
    ba[1] = "12:02";
    */
    sort(ad, atob);
    
    sort(aa, btoa);
    
    sort(bd, btoa);
    sort(ba, atob);
    //getchar();   
    nta = traincalc(ad, aa, atob, btoa,turnaround); 
    ntb = traincalc(bd, ba, btoa, atob,turnaround);
    cout<<"Case #"<<q+1<<": "<<nta<<" "<<ntb<<endl; 
    fout<<"Case #"<<q+1<<": "<<nta<<" "<<ntb<<endl;
    
    }
    getchar();
    getchar();
    return 1;
}
