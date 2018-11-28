/*
 * Google code jam: MagicKa
 * 
 * Author: Jim
 * Date: 2011-05-21 Sat.
 */

#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <string.h>

using namespace std;

void solve();

int main(void)
{
    int n;

    freopen("in_1.txt","r",stdin); 
    freopen("out_1.txt","w",stdout); 


    //Add Your Code Here
    cin >> n;
    for(int i=0; i<n; i++)
    {
        cout <<"Case #"<<i+1<<": "<<endl;
        solve();
    }


    fclose(stdin);
    fclose(stdout);

    return EXIT_SUCCESS;
}

void solve()
{
    int size = 0;
    cin >> size;
    int i = 0;
    int j = 0;
    int k = 0;
    double *WP = 0;
    double *OWP = 0;
    double *OOWP = 0;
    
    char **b=new char*[size];
    WP = new double[size];
    OWP = new double[size];
    OOWP = new double[size];
                                                       
    for(i=0;i<size;i++)
         b[i]=new char[size+1];
         
   for(i=0; i<size; i++)
   {
       cin >>  b[i];             
   }
   /*
   for(i=0; i<size; i++)
   {
       cout <<  b[i] << endl;             
   }   
   */
      int games = 0;
      int win = 0; 
   for(i=0; i<size; i++)
   {
      //WP
      games = 0;
      win = 0;
      for(j=0; j<size; j++)
      {
          if(b[i][j] != '.') 
          {
              games++;
              if(b[i][j] == '1')
                  win++;           
          }        
      }        
      WP[i] = win / double(games);
      //cout << i<<"(WP):"<< WP[i] <<  endl; 
   }
   for(k=0; k<size; k++)
   {
     //cal OWP
   double wp = 0.0;
   int c = 0;
   //Cal OWP for o
   for(i=0; i<size; i++)
   {
      if(k == i)
         continue;
      games = 0;
      win = 0;
      if(b[i][k] == '.')
          continue;
      for(j=0; j<size; j++)
      {
          if(b[i][j] != '.' && j != k) 
          {
              games++;
              if(b[i][j] == '1')
                  win++;           
          }        
      } 
      if(games != 0)
      {
          wp +=  win / double(games);  
          c++;     
      }           
   }
   OWP[k] = wp / c;
   //cout << k<<"(OWP):"<< OWP[k] <<  endl; 
   }
   
   for(i=0; i<size; i++)
   {
        double total = 0.0;
        int c = 0;
        for(j=0; j<size; j++)
        {
            if(b[i][j] == '.')
                continue;
            total += OWP[j];
            c++;
        }    
        
        OOWP[i] = total / c;
        //cout << i<<"(OOWP):"<< OOWP[i] <<  endl; 
   }
   
   for(i=0; i<size; i++)
   {
       cout<< 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i] << endl;         
   }
}


