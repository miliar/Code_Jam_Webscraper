#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;
int main()
{
        int ca,cb;
        char str[10];
        int t;
        int i;
        cin >> t;
        int kase = 1;
        while(t--){
                int n,nn;
                cin >> n;
                int cnt = 0;
                int chancea = 0;
                int chanceb = 0;
                int chance = 0;
                ca = cb = 1;

                for(i=0;i<n;i++){
                        cin >> str >> nn;
                        if(str[0] =='B'){
                                chance = max(abs(cb-nn)-chanceb,0) + 1;
                                chancea += chance;
                                chanceb = 0;
                                cnt += chance;
                                cb = nn;
                        }else{
                                chance = max(abs(ca-nn)-chancea,0) + 1;
                                chanceb += chance;
                                chancea = 0;
                                cnt += chance;
                                ca = nn;
                        }
                }
                cout  <<"Case #"<<kase++<<": "<< cnt << endl;
        }

        return 0;
}
