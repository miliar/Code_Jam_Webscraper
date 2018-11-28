#define _NOMINMAX

#include <stdio.h>
#include <math.h>

#include <assert.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

namespace{
    std::string get_result(int n,int m,int A)
    {
        bool possible(false);
        int w,a,b,x;
        for(w=n;w>=1;--w){
            for(a=m;a>=1;--a){
                if(w*a >= A){
                    for(b=m;b>=1;--b){
                        for(x=0;x<=w;++x){
                            const int s = a*(w-x) + b*x;
                            if(s == A){
                                possible = true;
                                goto loop_end;
                            }
                        }
                    }
                }
            }
        }
loop_end:
        if(!possible){
            return "IMPOSSIBLE";
        }

        char str[1024];
        sprintf(str,"%d %d %d %d %d %d",0,a,x,0,w,b);
        return str;
    }
}

int main(int argc, char* argv[])
{
    int n_cases(0);
    cin >> n_cases;

    for(int c=0;c!=n_cases && !std::cin.eof();++c){
        int n,m,a;
        cin >> n >> m >> a;

        std::cout << "Case #"<<(c+1)<<": "<< get_result(n,m,a) <<"\n";
    }
	return 0;
}
