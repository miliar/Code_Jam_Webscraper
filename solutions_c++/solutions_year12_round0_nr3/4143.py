#include <iostream>
#include <vector>
#include <math.h>

using namespace std;


int main(int argc, char** argv) {
    //freopen("input.txt", "rt", stdin);
    freopen("C-small-attempt0.in", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int T, y, p, q;
    unsigned int A, B;
    
    scanf("%d\n", &T);
    
    for(int ii=0; ii<T; ii++){

            printf("Case #%d: ", ii+1);

            scanf("%d", &A);
            scanf("%d", &B);    
            
            if(B<10){
                printf("%d\n", 0);
            }else{
            
                y = 0;
            
                for(int tt=A; tt<=B; tt++){

                    int n = tt;
                    int result;
                    int i = 0;
                    q=0;
                    p=0;
                    vector<int> ss;
                    ss.clear();

                    int digits = (int)ceil(log10(n));

                    while (n > 0) {
                        int digit = n % 10;
                        ss.push_back(digit);
                        n /= 10;
                        i++;
                    }
                    
                    for(int zz=0; zz<digits; zz++){
                        result = 0;
                        rotate(ss.begin(), ss.begin()+1, ss.end());
                        for(int qq=0; qq<ss.size(); qq++){
                            result += (int)pow(10,qq)*ss.at(qq);;
                        }

                        if(tt<result && result<=B){
                            if( p==tt && q==result ){
                                //nothing
                            }else{
                                y++;
                                p=tt;
                                q=result;
                            }
                           
                        }
                    }
                }
                printf("%d\n", y);
            }
    }
    return 0;
}

