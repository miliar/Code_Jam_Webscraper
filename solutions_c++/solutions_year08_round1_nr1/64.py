#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

long long fun()
{
    long long w=0LL;
    int i, n, v;
    vector<int> v1;
    vector<int> v2;
    scanf("%d",&n);
    for(i=0;i<n;i++) {
        scanf("%d",&v);
        v1.push_back(v);
    }
    for(i=0;i<n;i++) {
        scanf("%d",&v);
        v2.push_back(v);
    }
    sort(v1.begin(),v1.end());
    sort(v2.begin(),v2.end());
    vector<int>::iterator it1;
    vector<int>::iterator it2;
    for(it1=v1.begin(),it2=v2.end()-1;it1!=v1.end();it1++,it2--) {
        w += (long long)(*it1)*(*it2);
    }
    return w;
}

int main() {
    int iT, T;
    scanf("%d", &T);
    for (iT = 1; iT <= T; iT++) {
        printf("Case #%d: %lld\n",iT,fun());
    }
    return 0;
}
