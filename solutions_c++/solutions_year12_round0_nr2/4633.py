#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>
#include <sstream>
#include <cmath>

using namespace std;

vector<int> app(int n , int &s , int p)
{
    vector<int> k(3) ;
    int a1 , a2 , a3 , r1 ;
    if( s < 1 || n>28 || n<2 )
    {
         ss :
         a1 = n / 3 ;
         r1 = n - a1 ;
         a2 = r1 / 2 ;
         a3 = r1 - a2 ;
    }
    else
    {
        if(n%3 == 0)
        {
            a1 = n/3 ;
            a2 = a1+1 ;
            a3 = a1-1 ;
        }
        else if(n%3 == 1)
        {
            a1 = (int)n/3 - 1 ;
            a2 = a1 + 2 ;
            a3 = a2 ;
        }
        else if(n%3 == 2)
        {
            a1 = (int)n/3 ;
            a2 = a1 ;
            a3 = a2 + 2 ;
        }
        if(a1 !=p && a2 !=p && a3 !=p)
           goto ss ;
        s-- ;
    }
    k[0] = (a1) ;
    k[1] = (a2) ;
    k[2] = (a3) ;

    return k ;

}

int main()
{
    freopen("B-large.in", "r", stdin); // make cin and scanf take from file not from user
	freopen("B-large.out", "w", stdout); // make cout print to file not screen
    int n , N , S , P , res=0 , Max , num ;
    vector <int> nums ;
    cin >> n ;
    for(int t=0 ; t<n ; t++)
    {
        cin >> N >> S >> P ;
        vector< vector<int> > items ( N , vector<int> ( 3 ) );
        for(int i=0 ; i<N ; i++)
        {
            cin >> num ;
            nums.push_back(num) ;
        }
        sort( nums.begin() , nums.end() ) ;
        for(int i=0 ; i<N ; i++)
        {
            items[i] = app(nums[i] , S , P) ;

            Max = max(items[i][0] , items[i][1]) ;
            Max = max(items[i][2] , Max) ;
            if(Max >= P)
              res++;
        }

        cout << "Case #" << t+1 << ": " << res << endl ;
        res=0 ;
        nums.clear() ;
        items.clear() ;
    }

    return 0;
}
