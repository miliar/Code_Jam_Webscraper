#include<iostream>
#include<string.h>
#include<fstream>
using namespace std;


int main()
{
    int n=0,ns=5, nq=10, ite;
    fstream f1,f2;
    string line;
    f1.open("A-small-attempt1.in",ios::in);
    f2.open("A-small-attempt1.out",ios::out);
    if(!f1)
    {
           cout<<"error";
           return 1;
    }
    getline(f1,line);
    n = atoi( line.c_str() );
    
    for(ite = 0 ; ite<n ; ite++)
    {
    getline(f1, line);
    ns = atoi( line.c_str());
    string *se=new string[ns];
    int ni;
    for(ni=0 ; ni<ns ; ni++)
      getline(f1, se[ni]);
      
    getline(f1, line);
    nq = atoi(line.c_str());
    
    string *q =new string[nq];
    
    for(ni=0; ni<nq ;ni++)
      getline(f1, q[ni]);
      
    /*se[0]="Yeehaw";
    se[1]="NSM";
    se[2]="Dont Ask";
    se[3]="B9";
    se[4]="Googol";

    q[0]="Yeehaw";
    q[1]="Yeehaw";
    q[2]="Googol";
    q[3]="Dont Ask";
    q[4]="Googol";
    q[5]="NSM";
    q[6]="B9";
    q[7]="NSM";
    q[8]="B9";
    q[9]="Googol";
    
*/
    int *occ =new int[ns],i,j;
    int donej=0,  nosw=0;
    
    label:
    for(i=0;i<ns; i++)
      occ[i] = -1;    //non occurence
    
    
    for(i=0 ; i<ns ; i++)
    {
            for(j=donej ; j < nq ; j++)
            {
                    if( se[i] == q[j])
                      if(occ[i] == -1)
                      {
                                occ[i] =j;
                      }
                       
            }
    }
    int max_occ=-1, chose=-1;    
    
    for( i=0 ; i<ns ;i++)
    {
         if(occ[i] == -1)
         {
                   chose=i;
                   break;
          }
    }

    //cout<<chose;
    if(chose != -1)   //base case
    {
             //cout<<"in base: "<<chose<<endl;
             f2<<"Case #"<<ite+1<<":  "<<nosw<<endl;
             cout<<"Case #"<<ite+1<<":  "<<nosw<<endl;
             goto done;
    }
    
    for(i=0 ; i< ns ; i++)
    {
            if(occ[i]>max_occ)
            {
              max_occ = occ[i];
              chose = i;
             }
    }
    //cout<<max_occ<<"  "<<chose;
    if(max_occ<nq)
    {
      
      donej=max_occ;
      nosw++;
      goto label;
    }
    //if(max_occ==nq-1)
    
    
    done:
         ;
    }        
    
    
    


    getchar();
    
}
    
