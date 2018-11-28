#include <iostream>
using namespace std ;

int main()
{
    //freopen("in.txt", "r", stdin ) ;
    //freopen("out.txt", "w", stdout ) ;

    int sets, num[2000] ;
    
    cin >> sets ;
    for(int s=1; s<=sets; ++s ){
        int n, all=0 ;
        bool OK = false ;
        
        cin >> n ;
        int sum = 0 ;
        for(int i=0; i<n; ++i ){
            cin >> num[i] ;
            all ^= num[i] ;
            sum += num[i] ;
        }
        
        int up = 1<<n ;
        int Max = -1 ;
        int ans ;
        for(int i=0; i<up; ++i ){
            int temp = 0 ;
			int left = 0 ;
			int tsum = 0 ;
            for(int j=0; j<n; ++j ){
                if( (i>>j)&1 ){
                    temp ^= num[j] ;
                    tsum += num[j] ;
                }
				else{
					left ^= num[j] ;
				}
            }
            if( temp == left ){
                OK = true ;
                
                tsum = max( tsum, sum-tsum ) ;
                if( tsum == sum )
                    continue ;
                Max = max( Max, tsum ) ;
            }
        }
        cout << "Case #" << s << ": " ;
        if( OK ){
            cout << Max << endl ;
        }
        else{
            cout << "NO" << endl ;
        }
    }
    return 0 ;
}
