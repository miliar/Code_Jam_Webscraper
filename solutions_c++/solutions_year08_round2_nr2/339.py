#include <cstdio>
#include <vector>

using namespace std;
FILE *in, *out;

int ind[1000001];

void merge(int a, int b){
    while(ind[a] != -1) a = ind[a];
    while(ind[b] != -1) b = ind[b];
    if(a == b) return;
    ind[a] = b;
}

int main(){
    in = fopen("B.in", "r");
    out = fopen("B.out", "w");

    int p=0;
    vector<int> prime;
    for(int i=2;i<=100000;i++){
        bool ck=true;
        for(int j=0;j<p && ck;j++)
            if(!(i % prime[j]))
                ck=false;
        if(ck){
            prime.push_back(i);
            p++;
        }
    }

    int T;
    fscanf(in, "%d", &T);
    for(int t=1;t<=T;t++){
        long long A, B, P;
        fscanf(in, "%lld %lld %lld", &A, &B, &P);

        for(int i=0;i<=B-A;i++)
            ind[i] = -1;

        for(int i=0;i<p;i++){
            long long tmp=0;
            if(P <= prime[i] && prime[i] <= B-A)
                tmp = (long long)(B/prime[i]) - (long long)((A-1)/prime[i]);
            if(tmp>1){
                long long first, now = (long long)(A/prime[i]) * prime[i];
                first = now;
                if(now < A) now += prime[i];
                while(now+prime[i] <= B){
                    long long next = now+prime[i];
                    merge(now-A, next-A);
                    now = next;
                }
            }
        }

        long long result=0;
        for(int i=0;i<=B-A;i++)
            if(ind[i] == -1)
                result++;
        fprintf(out, "Case #%d: %lld\n", t, result);
    }
    fclose(in);
    fclose(out);
    return 0;
}
