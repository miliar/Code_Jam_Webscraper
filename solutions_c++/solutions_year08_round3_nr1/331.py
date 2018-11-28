#include<stdio.h>
#include<iostream>
#include<stdlib.h>

using namespace std;

int compareint(const void *a,const void *b)
{
    return *((int *) b) - *((int *) a);
}

int main()
{
    int ncase,ccase;
    int p,k,l;
    int freq[1001];
    int x,y,z,total;
    
    cin >> ncase;
    for(ccase = 1;ccase <= ncase;ccase++)
    {
        cin >> p >> k >> l;
        for(x = 0;x < l;x++)
            cin >> freq[x];
        
        qsort(freq,l,sizeof(int),compareint);
        
        y = 1;
        z = 0;
        total = 0;
        for(x = 0;x < l;x++)
        {
            if(z == k)
            {
                z = 0;
                y++;
            }
            
            total += freq[x] * y;
            z++;
        }
        
        cout << "Case #" << ccase << ": " << total << endl;
    }
    
    while(getchar()!=EOF);
    return 0;
}
