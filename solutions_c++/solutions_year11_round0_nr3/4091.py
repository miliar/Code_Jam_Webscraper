#include <cstdio>
#include <vector>
#include <set>
#include <stack>
using namespace std;
int weird(int a, int b){
    int w = 0, i=1;
    while(a>0 || b>0){
        w+=i*((a%2+b%2)%2);
        a/=2;
        b/=2;
        i*=2;
    }
    return w;
}


int main(){
    int wsum = 0, sum = 0, k, a, n, wyn = -1;
    scanf("%d", &n);
    for(int p=1; p<=n; ++p){
        wyn = -1;
        sum=0, wsum=0;
        vector<int> data;
        set<pair<int, int> > z;
        stack<pair<int, int> > buf;
        data.clear();
        z.clear();
        scanf("%d", &a);
        for(int i=0; i<a; ++i){
            scanf("%d", &k);
            sum+=k;
            data.push_back(k);
        }
        wsum = data[0];
        z.insert(make_pair(data[0], data[0]));
        for(int i=1; i<a; ++i){

            wsum = weird(wsum, data[i]);
            for(set<pair<int, int> >::reverse_iterator it=z.rbegin(); it!=z.rend(); ++it){
                  buf.push(make_pair (weird(it->first, data[i]), it->second+data[i]));

            }
            z.insert(make_pair(data[i], data[i]));
            while(!buf.empty()){
                z.insert(make_pair(buf.top().first, buf.top().second));
                buf.pop();

            }
        }

        for(set<pair<int, int> >::iterator it=z.begin(); it!=z.end(); ++it){
            if(weird(wsum, it->first)==it->first && it->first)  {
                wyn = max(wyn, it->second);
                wyn = max(wyn, sum-it->second);
            }
        }

        printf("Case #%d: ", p);
        if(wyn>0)
            printf("%d\n", wyn);
        else
            printf("NO\n");
 
    }
    return 0;
}
