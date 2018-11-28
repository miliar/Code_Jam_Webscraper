#include<iostream>
#include <fstream>
#include<conio.h>
#include<stdio.h>

using namespace std;

long double cal_wp(int ** a, int nteam,int team_no,int exclude)
{
    long double numerator=0,denominator=0;
    for(int i=0;i<nteam;i++)
    {
     if ( a[team_no][i] != 99 && i != exclude )
     {
        denominator++;
        numerator = numerator + a[team_no][i];
     }
     
            
    }
 
 
    //cout<<"denominator  "<<denominator<<endl;
    //cout<<"numerator  "<<numerator<<endl;
    
    return numerator/denominator;
    
    
}


long double cal_owp(int ** a,int nteam,int team_no)
{
    long double numerator=0,denominator=0;
    
    for(int i=0;i<nteam;i++)
    {
     if ( a[team_no][i] != 99 )
     {
          denominator++;
          numerator = numerator + cal_wp(a,nteam,i,team_no);
          
     }
     } 
    return numerator/denominator;
    
}


long double cal_oowp(int ** a,int nteam,int team_no)
{
    long double numerator=0,denominator=0;
    
    for(int i=0;i<nteam;i++)
    {
     if ( a[team_no][i] != 99 )
     {
          denominator++;
          numerator = numerator + cal_owp(a,nteam,i);
          
     }
     }
    return numerator/denominator;
    
}


long double cal_rpi(double wp, double owp, double oowp)
{
       long double rpi =   (0.25 * wp) + (0.50 * owp) +(0.25 * oowp);
       return rpi;
       
}


int main()
{
    int T=0,i=0,m=0;
    ifstream ifptr;
    ofstream ofptr;   
    ifptr.open ("A-large.in");
    ofptr.open ("A-large.out");
    ifptr>>T;
    cout<<" No of test cases:  "<<T<<endl;
    

    
    for( m = 0; m < T; m++ )
    {
         cout<<"Test case "<<m+1<<"\n\n\n";
         
         int j=0,k=0,N=0,nteams=0;
         ifptr >> nteams;
         cout<<"No of teams"<<nteams<<endl;
         int **a;
         //allocate memory start
	     a = (int **)malloc(nteams * sizeof(int *));
	           if(a == NULL)
		       {
		        cout<<"out of memory\n";
                  return 0;
               }
         for(i = 0; i < nteams; i++)
		 {
		       a[i] = (int *)malloc(nteams * sizeof(int));
		       if(a[i] == NULL)
			   {
		        cout<<"out of memory\n";
			    return 0;
		       }
		}
        //allocate memory end
        char c;
        //take input from file
         for( j = 0; j < nteams ;j++ )
         {
              for( k = 0; k < nteams ;k++ )
              {
                  ifptr >> c;
                  if ( c == '.')
                     a[j][k] = 99;
                  else if (c == '0')
                      a[j][k] = 0;
                  else a[j][k] =  1;   
                           
              }

         }
         ofptr<<"Case #"<<m+1<<":\n";
         for( j = 0; j < nteams ;j++ )
         {
     
         cout<<" Calculating rpi for team no "<<j+1<<endl;
         long double wp,owp,oowp,rpi;
          wp = cal_wp(a,nteams,j,-1) ;  
          cout<<"wp  :"<<wp<<endl;
          
          
          owp = cal_owp(a,nteams,j);
          cout<<"owp  :"<<owp<<endl;
          oowp = cal_oowp(a,nteams,j);
          cout<<"oowp  :"<<oowp<<endl;
          rpi = cal_rpi(wp,owp,oowp);
          cout<<"rpi  :"<<rpi<<endl;
          ofptr<<rpi<<"\n";
           
         }
         
         /*
         
         for( j = 0; j < nteams ;j++ )
         {
              for( k = 0; k < nteams ;k++ )
              {
                  cout<< a[j][k]<<"  ";
                           
              }
              cout<<endl;

         }
         
         
         
         
         
         */
         
         
         
         
         
         
         
         
         
         
         //if (sum_xor !=  0)
           // ofptr<<"Case #"<<i+1<<": NO\n";
         //else
           // ofptr<<"Case #"<<i+1<<": "<<sum-min<<"\n";;      
         for( i = 0; i < nteams; i++)
		       free(a[i]);
        free(a);

    }
    
    
  
    
    ifptr.close();
    ofptr.close();
    
    getchar();
return 0;    
}
