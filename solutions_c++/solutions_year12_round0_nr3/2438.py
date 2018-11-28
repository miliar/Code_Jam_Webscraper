#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<set>
using namespace std;

set<pair<int,int> >h;

struct Number{
    int digit;
    int value[11];

    bool operator < (const Number e) const{
        for(int i = 0; i < digit; i++){
            if(value[i] != e.value[i]){
                return value[i] < e.value[i];
                break;
            }
        }
        return 0;
    }

    bool operator <= (const Number e) const{
        for(int i = 0; i < digit; i++){
            if(value[i] != e.value[i]){
                return value[i] < e.value[i];
                break;
            }
        }
        return 1;
    }	

    int  getValue(){
        int r=0;
        for(int i = 0; i < digit; i++)
            r=r*10+value[i];
        return r;
    }

    void add(){
        value[digit-1]++;
        for(int i = digit-1; i >=0; i--){
            if(value[i] >= 10) value[i-1]+=1, value[i]%=10;
        }
    }

    void move(){
        Number a;
        a.digit = digit;
        int i, j;
        for(i = 0; i < digit; i++) a.value[i] = value[i];
        value[0] = a.value[digit-1];
        for(i = 0, j = 1; j < digit; i++, j++) value[j] = a.value[i];
    }
};


int main(){
    int T, cnt;
    cnt = 0;
    scanf("%d", &T);
    while(T--){
        h.clear();
        int ans = 0;
        char a[11], b[11];
        scanf("%s %s", a, b);
        int d = strlen(a);
        Number A, B, K;
        A.digit = B.digit = K.digit  = d;
        for(int i = 0; i < d; i++){
            A.value[i] = a[i] - '0';
            K.value[i] = A.value[i];
            B.value[i] = b[i] - '0';
        }
        int a_num, b_num, ten;
        a_num = b_num = 0, ten = 1;
        for(int i = d-1; i >= 0; i--, ten *= 10){
            a_num += A.value[i]*ten;
            b_num += B.value[i]*ten;
        }
        //continue;
        for(int i = a_num; i <= b_num; i++, K.add()){
            Number tmp;
            tmp.digit = K.digit;
            for(int j = 0; j < d; j++) tmp.value[j] = K.value[j];
            for(int j = 0; j < d; j++){
                tmp.move();
                if(!tmp.value[0]) continue;
                //tmp.print();
                if(tmp <= B && K < tmp){ 
                    if(h.find(make_pair(K.getValue(), tmp.getValue()))==h.end()) {
//                        printf("(%d,%d)\n",K.getValue(), tmp.getValue());
                        ans++;
                        h.insert(make_pair(K.getValue(), tmp.getValue()));
                    }

                }	
            }
        }

        printf("Case #%d: %d\n", ++cnt, ans);
    }

    return 0;
}
