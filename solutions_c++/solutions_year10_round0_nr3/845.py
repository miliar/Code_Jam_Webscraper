#include <iostream>
#include <cstdio>

using namespace std;

#define ll long long

FILE *fin = fopen ("C-large.in","r");
FILE *fout = fopen ("C-large.out","w");

int main () {
    int T;
    fscanf (fin, "%d", &T);

    for (int run = 1;run<=T;++run) {
        int R,K,N;
        fscanf (fin, "%d %d %d", &R,&K,&N);
        ll a[N], next[N], tong[N];
        for (int i = 0;i<N;++i)
            fscanf (fin,"%I64d", &a[i]);
        for (int i = 0;i<N;++i) {
            int j = (i+1)%N;
            ll temp = a[i];
            int count = 1;
            while (temp + a[j]<= K && count < N) {
                next[i] = j;
                temp+=a[j];                                           
                j = (j+1)%N;
                count++;
            }
            tong[i] = temp;
            next[i] = j;
        }

        int mark[N];
        memset (mark, 0, sizeof (mark));
        int li = 0, cycle_length = 0;
        ll cycle_sum = 0;
        while (mark[li] == 0 && cycle_length < R) {
            cycle_length++;
            mark[li] = 1;
            cycle_sum +=tong[li];
            li = next[li];
        }

        
        ll res = 0;
        if (cycle_length==R) res = cycle_sum;
        else {

            int i = 0, count = 0;
            while (i != li) {
                res+=tong[i];
                i = next[i];
                count++;   
            }

            cycle_sum -=res;
            cycle_length-=count;
            R-= count;
            res += cycle_sum*(R/cycle_length);
            for (int i = 0;i<R%cycle_length;++i) {
                res+=tong[li];
                li = next[li];   
            }
        }

        fprintf (fout, "Case #%d: %lld\n",run,res);
    }    

    return 0;   
}
