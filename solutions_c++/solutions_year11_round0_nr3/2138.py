/*
 * Google code jam: candy
 * 
 * Author: Jim
 * Date: 2011-05-07 Sat.
 */

#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <string.h>

using namespace std;
  
int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

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
    int m = 0;
    int i = 0;
    int *candy = NULL;
    cin >> m;
    candy = new int[m];
    for(i=0; i<m; i++)
    {
        cin >> candy[i];         
    }
    int sum = 0;
    for(i=0; i<m; i++)
    {
        sum ^= candy[i];         
    }
    if(sum != 0)
    {
        cout << "NO" << endl;
        return;
    }
    
    qsort(candy, m,sizeof(int), compare);
    
    sum = 0;
    for(i=1; i<m; i++)
    {
        sum += candy[i];       
    }
    cout << sum <<endl;
}


