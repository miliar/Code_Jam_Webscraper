#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <sstream>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <algorithm>
#include <stack>
#include <queue>
#include <list>
#include <fstream>
using namespace std;

typedef long long LL;

int PrimeFactor5(int N){

    int ret = 0;
    while( N % 5 == 0 && N){

        N/=5;++ret;
        if(ret==2)return ret;

    }
    return ret;

}

int PrimeFactor2(int N){

    int ret = 0;
    while( N % 2 == 0 && N){

        N/=2;++ret;
        if(ret==2)return ret;

    }
    return ret;

}


int main(){
    freopen("1.in","r",stdin);
    freopen("3.txt","w",stdout);
    int t,ca = 0;
    scanf("%d",&t);
    while(t--){

        LL pd,pg,N;
        cin>>N>>pd>>pg;
        int five = PrimeFactor5( pd );
        int two = PrimeFactor2( pd );

        printf("Case #%d: ",++ca);
        if( (pg == 100 && pd != 100) || (pg==0&&pd!=0)  ){
            puts("Broken");
            continue;
        }

        if( !pd ) puts("Possible");
        else if( five + two == 4 ){

            puts("Possible");

        }
        else{

            if( five == 2 ){

                int m = pow(2.0,(2-two));
                if( m > N )puts("Broken");
                else puts("Possible");

            }
            else if( two == 2 ){

                int m = pow(5.0,(2-five));
                if(m > N )puts("Broken");
                else puts("Possible");

            }
            else{

                int m = pow(5,(2.0-five)) * pow(2.0,(2-two));
                if( m > N )puts("Broken");
                else puts("Possible");

            }

        }


    }
    return 0;

}
