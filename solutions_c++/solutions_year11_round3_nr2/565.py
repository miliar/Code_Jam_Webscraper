/*
 * Google code jam:Space Emergency 
 * 
 * Author: Jim
 * Date: 2011-05-07 Sun.
 */

#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <string.h>

using namespace std;


int compare (const void * a, const void * b)
{
  return ( *(int*)b - *(int*)a );
}

void solve();

int main(void)
{
    int n;

    freopen("in_2.txt","r",stdin); 
    freopen("out_2.txt","w",stdout); 


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
    int l = 0;
    long long t = 0;
    int n = 0;
    int c = 0;
    
    int i = 0;
    int org_t = 0;
    
    int *dis = NULL;
    
    int time = 0;
    
    cin >> l >> t >> n >> c;
    
    dis = new int[n];
    
    org_t = t;
    for(i=0; i<c; i++)
    {
        cin >> dis[i];         
    }
    for(i=c; i<n; i++)
    {
        dis[i] = dis[i%c];         
    } 
    
    if(l == 0)
    {
       for(i=0; i<n; i++)
       {
           time += 2*dis[i];     
       }  
       cout << time << endl;
       return;
    }
    
    for(i=0; i<n; i++)
    {
        if (t-2*dis[i] > 0)
        {
            
            t = t - 2*dis[i];
            dis[i] = 0;               
        }       
        else
        {
            dis[i] = (2*dis[i] - t ) / 2;
            t = 0;
            break;  
        }
    }
    
    if (t != 0)
    {
       cout << org_t - t << endl;
       return;
    }
             
    qsort (dis, n, sizeof(int), compare); 
    
    time = 0;
    for(i=0; i<n; i++)
    {
        if(l > 0)
        {
            time += dis[i];
            l--;     
        }
        else
        {
            time += 2*dis[i];    
        }
        //cout << dis[i] << " ";       
    } 
       
    cout << time + org_t << endl;
}


