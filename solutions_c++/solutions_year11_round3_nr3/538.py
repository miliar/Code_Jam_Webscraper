/*
 * Google code jam: perfect_harmony
 * 
 * Author: Jim
 * Date: 2011-05-07 Sun.
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

    freopen("in_3.txt","r",stdin); 
    freopen("out_3.txt","w",stdout); 


    //Add Your Code Here
    cin >> n;
    for(int i=0; i<n; i++)
    {
        cout <<"Case #"<<i+1<<": ";
        solve();
    }


    fclose(stdin);
    fclose(stdout);

    return EXIT_SUCCESS;
}

void solve()
{
    int n = 0;
    int low = 0;
    int high = 0;
    
    int *freq = NULL;
    
    int i = 0;
    int j = 0;
    
    cin >> n >> low >> high;
    
    freq = new int[n];
    
    for(i=0; i<n; i++)
    {
        cin >> freq[i];             
    }
  
  /*  
    for(i=0; i<n; i++)
    {
        cout << freq[i] << endl;            
    }  
    */
     
    for(i=low; i<=high; i++)
    {
      for(j=0; j<n; j++)
      { 
       if( (i%freq[j] == 0) || (freq[j]%i == 0))
       {
       }
       else
       {
          break;         
        }
      }
      if(j==n)
      {
          cout<<i<<endl;
          return;
       }
    }  
    
    cout << "NO" <<endl;
    
}


