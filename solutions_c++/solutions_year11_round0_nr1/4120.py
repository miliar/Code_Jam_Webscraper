#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <cstdlib>
#include <stack>
#include <queue>
#include <set>
#include <list>
#include <map>
#include <vector>
#include <string>
using namespace std;

int main(){

    freopen( "1.txt","r",stdin );
    freopen( "2.txt","w",stdout );
    int t,ca = 0;
    scanf("%d",&t);
    while(t--){

        int N;
        scanf("%d",&N);
        char A[11],B[11];
        int res = 0,OrangePosition = 1,BluePosition = 1,lastMoveTime = 0,currentMoveTime,lastMovedRobot = -1;
        for(int i = 0;i<N;++i){
            scanf("%s %s",A,B);
            stringstream is(B);
            int tmp;is>>tmp;
            if( A[0] == 'O' ){
                currentMoveTime = abs( OrangePosition - tmp ) + 1;
                if( lastMovedRobot == 1 ){
                    res += max( 1,currentMoveTime-lastMoveTime );
                    lastMoveTime = max( 1,currentMoveTime-lastMoveTime );
                }
                else{
                    res += currentMoveTime;
                    lastMoveTime += currentMoveTime;
                }
                lastMovedRobot = 0;
                OrangePosition = tmp;
            }
            else{

                currentMoveTime = abs( BluePosition - tmp ) + 1;
                if( lastMovedRobot == 0 ){
                    res += max( 1,currentMoveTime-lastMoveTime );
                    lastMoveTime = max( 1,currentMoveTime-lastMoveTime );
                }
                else{
                    res += currentMoveTime;
                    lastMoveTime += currentMoveTime;
                }
                lastMovedRobot = 1;
                BluePosition = tmp;

            }
        }
        printf("Case #%d: %d\n",++ca,res);

    }
    return 0;

}
