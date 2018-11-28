
#include <iostream>
#include <vector>
#include <list>
#include <map>

using namespace std;
//~ for(int i = 0; i < n; ++i)
int gcd(int a1, int b1)
{
    int a, b;
    a = a1;
    b = b1;
    if(a1< b1)
    {
        a = b1;
        b = a1;
    }
    if(b ==0 )
    {
        return a;
    }
    return gcd(b, a % b);
    
}
int main()
{
    int t;
    cin >> t;
    for(int i = 0; i < t; ++i)
    {
        int n, l ,h;
        cin >> n >> l >> h;
        
        int * freq= new int[n];
        int acum;
        for(int j =0; j < n ;++j)
        {
            cin >> freq[j];
        }
        int res=-1;
        for(int j =h; j > l -1; --j)
        {
            int comp = true;
            for(int k = 0; comp &&  k < n; ++k)
            {
                comp = comp && ( ( (j % freq[k] )==0 ) || (( freq[k] %j )==0) ) ;
            }
            if(comp)
            {
                res = j;
            }
        }
        cout << "Case #" << i+1 << ": ";
        if(res==-1)
        {
            cout << "NO"<<endl;
        }
        else
        {
            cout << res << endl;
        }
        
        delete [] freq;
    }
    return 0;
}





// ******************************************
//~ 
//~ #include <iostream>
//~ #include <vector>
//~ #include <list>
//~ #include <map>
//~ 
//~ using namespace std;

//~ int gcd(int a1, int b1)
//~ {
    //~ int a, b;
    //~ a = a1;
    //~ b = b1;
    //~ if(a1< b1)
    //~ {
        //~ a = b1;
        //~ b = a1;
    //~ }
    //~ if(b ==0 )
    //~ {
        //~ return a;
    //~ }
    //~ return gcd(b, a % b);
    //~ 
//~ }
//~ int main()
//~ {
    //~ int t;
    //~ cin >> t;
    //~ for(int i = 0; i < t; ++i)
    //~ {
        //~ int n, l ,h;
        //~ cin >> n >> l >> h;
        //~ 
        //~ int * freq= new int[n];
        //~ int acum;
        //~ for(int j =0; j < n ;++j)
        //~ {
            //~ cin >> freq[j];
            //~ if(j ==0)
            //~ {
                //~ acum = freq[0];
            //~ }
            //~ else
            //~ {
                //~ acum = gcd(acum,freq[j]);
            //~ }
        //~ }
        //~ cout << acum << endl;
        //~ int res=-1;
        //~ for(int j =h; j > l -1; --j)
        //~ {
            //~ if((acum % j) == 0)
            //~ {
                //~ res = j;
            //~ }
        //~ }
        //~ cout << "Case #" << i+1 << ": ";
        //~ if(res==-1)
        //~ {
            //~ cout << "NO"<<endl;
        //~ }
        //~ else
        //~ {
            //~ cout << res << endl;
        //~ }
        //~ 
        //~ delete [] freq;
    //~ }
    //~ return 0;
//~ }
