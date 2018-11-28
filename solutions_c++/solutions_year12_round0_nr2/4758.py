#include <cstdlib>
#include <iostream>
#include <cmath>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <complex>
#include <algorithm>
#include <functional>
#include <fstream>
#include <numeric>
#include <string>
#include <valarray>
#include <queue>
#include <set>

using namespace std;

#define show(s) cout << #s << "-->" << s << endl;
#define show1(x,y,z) cout << #x << " , " << y << " , "<< z<< "-->" << x << endl;

int main()
{


    int n;
    scanf("%d", &n);
    int m ,s, p;
    int trip;
    int temp = 0;
    for (int i = 0; i < n; i++)
    {
        int type[3] = {0,0,0};
        temp = 0;
        scanf("%d%d%d", &m , &s , &p);
        for(int j=0; j< m; j++){
            scanf("%d", &trip);
            if(!trip){
                temp+=((p==0)&(s==0));
                continue;
            }
            if(trip%3 == 0){

                if((trip/3)+1 < p){
                    type[0]++;
                }
                else if( (trip/3)+1 == p){
                    type[1]++;
                }
                else
                    type[2]++;
            }
            else if(trip%3 == 1){
                if((trip/3)+1 < p){
                    type[0]++;
                }
                else
                    if(trip > 1 || !s)
                        type[2]++;
            }
            else
                if((trip/3)+2 < p){
                    type[0]++;
                }
                else if( (trip/3)+2 == p){
                    type[1]++;
                }
                else
                    type[2]++;
        }
        //printf("%d %d %d\n", type[0] , type[1], type[2]);
        printf("Case #%d: ",i+1);
        printf("%d\n",type[2]+min(type[1], s)+temp);

    }


    return 0;
}