#include<iostream>
#include<algorithm>
#include<conio.h>
#include<vector>
using namespace std;
typedef long long LL;
int getVal(vector<int> digits,int start,int len) {
    int N=0;
    for(int i=0;i<len;i++) {
        N = N*10 + digits[i+start];
    }
    return N;
}
int main() {
    int T;
    cin>>T;
    int nCase = 1;
    for(int i=0;i<T;i++) {
        int A,B;
        cin>>A>>B;
        int x=B;
        while(x>9) {
            x=x/10;
        }
        int nReversals = 0;
        vector<int> ms;
        for(int n=A;n<B;n++) {
            vector<int> digits;
            int k=n;
            while(k!=0) {
                digits.push_back(k%10);
                k=k/10;
            }
            reverse(digits.begin(),digits.end());
            int y = digits.size();
            for(k=0;k<y;k++) {
                digits.push_back(digits[k]);
            }
            for(k=1;k<y;k++)
            {
                if(digits[k]>=digits[0] && digits[k]<=x) {
                    int m = getVal(digits,k,y);
                    if(m>n && m<=B) {
                        int add=1;
                        for(int p=0;p<ms.size();p++) {
                            if(m==ms[p])
                                add=0;
                        }
                        if(add==1) {
                            ms.push_back(m);
                            nReversals++;
                        }
                    }
                }
           }
           ms.clear();
        }
        cout<<"Case #"<<i+1<<": "<<nReversals<<endl;
    }
}
