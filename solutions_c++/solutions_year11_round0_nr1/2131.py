/*
 * Google code jam: Bot Trust
 * 
 * Author: Jim
 * Date: 2011-05-07 Sat.
 */

#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <string.h>

using namespace std;
  

void solve();

int main(void)
{
    int n;

    freopen("in.txt","r",stdin); 
    freopen("out.txt","w",stdout); 


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
  bool *flag = NULL;
  int *pos = NULL;
  int i;
  cin >> n;
  flag = new bool[n];
  pos = new int[n];
 
  for(i=0; i<n; i++)
  {
      char bot;
      cin >> bot;
      if (bot == 'O')
          flag[i] = 0;
      else
          flag[i] = 1;
      
      cin >> pos[i];
      //cout << pos[i] << endl;
  } 
  int a = 1;
  int b = 1;
  i = 0;
  int j = 0;
  bool f = flag[i];
  j = i+1;
  while(flag[j]==f && j < n) j++;
  int c = 0;
  while(true)
  {
         
     if(f == 0)
     {
		 if(j < n && b != pos[j])
		 {
			 if(b - pos[j] < 0)
                 b++;
			 else
				 b--;
		 }
         if(a == pos[i])
         {
             i++;
             if(i >= n)
                 break;
             f = flag[i]; 
             j = i+1;
             while(flag[j]==f && j < n) 
				 j++;
			 c++;
             continue;     
         }        
			 if(a - pos[i] < 0)
                 a++;
			 else
				 a--;

     }  
     else
     {
         if(j < n && a != pos[j])
		 {
			 if(a - pos[j] < 0)
                 a++;
			 else
				 a--;
		 }

         if(b == pos[i])
         {
             i++;
             if(i >= n)
                 break;
             f = flag[i]; 
             j = i+1;
             while(flag[j]==f && j < n) 
				 j++;
			 c++;
             continue;     
         }        
			 if(b - pos[i] < 0)
                 b++;
			 else
				 b--;
         
      
     }
     c++;  
  }
  cout << c + 1<< endl;
}


