#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>

#define ALL(X)  X.begin(), X.end()

using namespace std;

int NA, NB, T;

int main() 
{
        int d; scanf("%d", &d); for(int no = 1; no<=d; ++no) {
                scanf("%d %d %d", &T, &NA, &NB);
                vector< int > dAB(NA), aAB(NA);
                vector< int > dBA(NB), aBA(NB);
                dAB.erase(dAB.begin(), dAB.end()); aAB.erase(aAB.begin(), aAB.end());
                dBA.erase(dBA.begin(), dBA.end()); aBA.erase(aBA.begin(), aBA.end());

                for ( int h, m, i = 0; i < NA; ++i ) {
                        
                        scanf("%d:%d", &h, &m); h = (60*h + m); dAB.push_back(h);
                        scanf("%d:%d", &h, &m); h = (60*h + m); aAB.push_back(h);
                }
                sort(ALL(dAB)); sort(ALL(aAB));

                for ( int h, m, i = 0; i < NB; ++i ) {
                        
                        scanf("%d:%d", &h, &m); h = (60*h + m); dBA.push_back(h);
                        scanf("%d:%d", &h, &m); h = (60*h + m); aBA.push_back(h);
                }
                sort(ALL(dBA)); sort(ALL(aBA));

                
                for ( int i = 0; i < aAB.size(); ++i) {
                        int a = aAB[i];
                        for ( int j = 0; j < dBA.size(); ) {
                                if ( a + T <= dBA[j] ) {
                                //printf("\tdAB.erase(%d:%d) >= %d:%d\n", dBA[j]/60, dBA[j]%60, (a+T)/60, (a+T)%60);                                                                          
                                      dBA.erase(dBA.begin() + j);                                      
                                      break;
                                }
                                else {
                                        ++j;
                                }
                        }
                }
                

                for ( int i = 0; i < aBA.size(); ++i) {
                        int b = aBA[i];
                        for ( int j = 0; j < dAB.size(); ) {
                                if ( b + T <= dAB[j] ) {  
                                      //printf("\tdAB.erase(%d:%d) >= %d:%d\n", dAB[j]/60, dAB[j]%60, (b+T)/60, (b+T)%60);                                    
                                      dAB.erase(dAB.begin() + j); 
                                       break;
                                        
                                }
                                else ++j;
                        }
                }
                                

                printf("Case #%d: %d %d\n", no, dAB.size(), dBA.size());
                
        }
        return 0;
}
