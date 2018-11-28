#include <iostream>
#include <string>
#include <set>
#include <map>
using namespace std ;

int main()
{
    //freopen("in.txt", "r", stdin ) ;
    //freopen("out.txt", "w", stdout ) ;
    
    int sets ;
    
    cin >> sets ;
    for(int s=1; s<=sets; ++s ){
        int c ;
        cin >> c ;
        map<string,string> form ;
        string str ;
        
        for(int i=0; i<c; ++i ){
            cin >> str ;
            form[str.substr(0,2)] = str.substr(2) ;
            swap( str[0], str[1] ) ;
            form[str.substr(0,2)] = str.substr(2) ;
        }
        
        int d ;
        cin >> d ;
        set<string> oppo ;
        for(int i=0; i<d; ++i ){
            cin >> str ;
            oppo.insert(str) ;
            swap( str[0], str[1] ) ;
            oppo.insert(str) ;
        }
        
        int n ;
        cin >> n ;
        cin >> str ;
        string ans ;
        ans += str[0] ;
        for(int i=1; i<str.size(); ++i ){
            string temp ;
            temp += ans[ans.size()-1] ;
            temp += str[i] ;
            if( form.count(temp) ){
                ans.resize( ans.size()-1 ) ;
                ans += form[temp] ;
            }
            else{
                temp = str[i] ;
                bool OK = true ;
                for(int j=0; j<ans.size(); ++j ){
                    if( oppo.count(string(temp+ans[j])) ){
                        ans = "" ;
                        OK = false ;
                        break ; 
                    }
                }
                if( OK ){
                    ans += str[i] ;
                }
            }
        }
        
        cout << "Case #" << s << ": [" ;
        for(int i=0; i<ans.size(); ++i ){
            if( i )
                cout << ", " ;
            cout << ans[i] ;
        }
        cout << "]" << endl ;
    }
    return 0 ;
}
