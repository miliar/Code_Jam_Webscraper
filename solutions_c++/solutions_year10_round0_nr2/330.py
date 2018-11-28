#include <iostream>
#include <gmpxx.h>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cassert>

using namespace std;
typedef mpz_class mint;

mint gcd(mint a, mint b) {
    if(a % b == 0) return b;
    return gcd(b, a % b);
}

mint gcdl(vector<mint> v) {
	if(v.size() < 2) return v[0];
	mint ret = gcd(v[0],v[1]);
    for(int i = 2; i < v.size(); ++i) {
        ret = gcd(ret,v[i]);
    }
    return ret;
}

int main() {
	int N;
    cin>>N;
    for(int i = 0; i < N; ++i) {
    	int M;
    	cin>>M;
        vector<mint> vec(M);
        for(int j = 0; j < M; ++j) {
            cin>>vec[j];
        }

        mint me = *min_element(vec.begin(),vec.end());

        vector<mint> v2;

        for(int j = 0; j < vec.size(); ++j) {
            if(vec[j] != me) {
                v2.push_back(vec[j] - me);
            }
        }

/*
        cout<<"gcd: "<<gcd(5,6)<<endl;
        mint a = 5, b = 6;
        cout<<(b%a)<<endl;

        cout<<v2.size()<<endl;

        for(int j = 0; j < v2.size(); ++j) {
            cout<<v2[j]<<" ";
        }
        cout<<endl;

*/
        mint val = gcdl(v2);
        assert(val != 0);

        if(val == 1) {
            printf("Case #%d: 0\n",(i+1));
        } else {
            if(me % val == 0) {
                printf("Case #%d: 0\n",(i+1));
            } else {
                mint ad = val - me % val;


                printf("Case #%d: ",(i+1));
                cout<<ad<<endl;
            }
        }
    }
    return 0;
}
