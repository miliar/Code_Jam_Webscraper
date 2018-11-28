#include <iostream>
using namespace std;
#include <string>

int main(void){
    int cases;
    cin >> cases;
    for(int c=0;c<cases;++c){
        char str[64];
        int num[128];
        for(int i=0;i<128;++i)
            num[i] = -1;
        cin >> str;
        int len = strlen(str);
        num[str[0]] = 1;
        int now_num = 0;
        for(int i=1;i<len;++i){
            if(num[str[i]]==-1){
                num[str[i]] = now_num;
                now_num++;
                if(now_num==1)
                    now_num = 2;
            }
        }
        int base = now_num;
        if(base==0)
            base = 2;
        int t = 1;
        int sum = 0;
        for(int i=len-1;i>=0;i--){
            sum += num[str[i]]*t;
            t*=base;
        }
        cout << "Case #" << c+1 << ": " << sum << endl;
    }
    return 0;
}
