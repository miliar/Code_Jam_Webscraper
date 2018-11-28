#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

int compare (const void * a, const void * b)
{
  return ( *(long*)b - *(long*)a );
}


int main()
{
    int n;
    cin>>n;
    int p,k,l,i;
    long *v;
    long s;
    for(int t = 0; t < n; t++)
    { 
        cin>>p;
        cin>>k;
        cin>>l;  
        s = 0;
        v = new long[l];
        for(i =0;i<l;i++)
              cin>>v[i];  
        qsort (v ,l, sizeof(long), compare);
        int j = 0;
        int r = 1;
        for(i = 0;i<l;i++)
        {
              if(j == k)
              {
                   r++;
                   j = 0;
              }
                   
              s+=r*v[i];
              j++;
        }
        cout<<"Case #"<< (t+1)<<": "<<s<<"\n";
        delete v;
    }
    return 0;
}
