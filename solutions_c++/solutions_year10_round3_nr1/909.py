#include <iostream>
#include <cstdio>

using namespace std;

FILE *fin = fopen ("A-large.in","r");
FILE *fout = fopen ("A-large.out","w");

int main () {
    int T;
    fscanf (fin,"%d",&T);
    for (int run = 1;run<=T;++run) {
        int N;
        fscanf (fin,"%d",&N);   
        int a[N],b[N];
        for (int i = 0;i<N;++i) 
            fscanf (fin,"%d %d",&a[i],&b[i]);

        for (int i = 0;i<N;++i)
            for (int j = i+1;j<N;++j)
                if (a[i] > a[j]) {
                    int temp = a[i];
                    a[i] = a[j];
                    a[j] = temp;
                    temp = b[i];
                    b[i] = b[j];
                    b[j] = temp;
                }
        int res = 0;
        for (int i = 0;i< N-1;++i)
            for (int j = i+1;j<N;++j)
                if (b[i] > b[j]) res++;
        cout<<res<<endl;
        fprintf (fout, "Case #%d: %d\n",run,res);
    }
    cin>>T;
    return 0;
}
