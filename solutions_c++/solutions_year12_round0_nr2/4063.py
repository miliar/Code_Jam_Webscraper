#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;
bool myfunction (int i,int j) { return (i>j); }
int main()
{
    freopen("a.in", "rt", stdin);
    freopen("a.out", "wt", stdout);
    int T, N, S, p ,tmp;

    vector<int> myTab ;

    cin >> T ;
    for (int indice=1; indice<=T; indice++) {
        cin >> N >> S >> p;
        myTab.clear();
        for (int i=0; i<N; ++i) {
            cin >> tmp ;
            myTab.push_back(tmp);
        }
        sort(myTab.begin(), myTab.end(), myfunction) ;

        bool end = false;
        int i=0, res=0 ;
        if (p==0)
            res =N;
        else {
            while (! end ) {
                if (myTab[i]==0)
                    end =true ;
                else {
                    if (  ((myTab[i]%3 == 0 || myTab[i]%3 == 1 ) && myTab[i]/3 >=p )  || (myTab[i]%3 == 2 && myTab[i]/3 + 1 >= p )  ){
                        i++;
                        res++ ;
                    }else if (myTab[i]%3 == 0 ) {
                        if ( myTab[i]/3 == p-1 && S!=0 ) {
                            S-- ; i++ ; res++ ;
                        } else
                            end = true ;
                    }else if (myTab[i]%3 == 1 ) {
                        if ( myTab[i]/3 == p-1 ) {
                            i++ ; res++ ;
                        } else if ( myTab[i]/3 == p-2 && S!=0 ) {
                            S-- ; i++ ; res++ ;
                        }else
                            end = true ;
                    }else if (myTab[i]%3 == 2 ) {
                        if ( myTab[i]/3 +1 == p-1 && S!=0 ) {
                            S-- ; i++ ; res++ ;
                        } else
                            end = true ;
                    }else
                        end =true ;
                    if ( i == myTab.size())
                        end = true ;
                }
            }
        }
        cout << "Case #" << indice << ": " << res << endl ;
    }
    return 0;
}
