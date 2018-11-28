#include <iostream>
#include <vector>
#include <algorithm>
#include <list>
#include <string>
using namespace std;

bool porownaj1 (long long  i,long long j)
{
    return i < j;
}

bool porownaj2 (long long  i,long long j)
{
    return j < i;
}

int main()
{
	int n;
	cin >> n;
    
	for( int q=0; q<n; q++ )
    {
        int len;
        vector<long long> v1, v2;
        vector<long long>::iterator v1i, v2i;
       
        cin >> len; 
        long long *tab1 = new long long[len];
        long long *tab2 = new long long[len];
        
       
        for( int i=0; i<len; i++)
        { 
            cin >> tab1[i];     
        }
        
        v1.assign( tab1, tab1+len );
        
        for( int i=0; i<len; i++)
        { 
            cin >> tab2[i];     
        }
        
        v2.assign( tab2, tab2+len );
              
        sort (v1.begin(), v1.end(), porownaj1);
        sort (v2.begin(), v2.end(), porownaj2);
        
        long long sum = 0;
        for( v1i = v1.begin(), v2i = v2.begin(); v1i != v1.end(), v2i != v2.end(); ++v1i, ++v2i )
        {
            sum += (*v1i) * (*v2i);
        }
        
	    cout << "Case #" << q+1 << ": " << sum << endl;
    }
    
	return 0;
}
