#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    fstream fout, fin;
    fin.open("input.txt");
    fout.open("output.txt");
    int T, N;
    fin>>T;
    for(int t=1; t<=T; ++t)
    {
        fin>>N;
        int a[N+2], result=0, k=0, n;
        for(int n = 1; n<=N; ++n)
            fin>>a[n];
        while(true)
        {
            for(n = 1; n<=N; ++n)
                if(a[n])break;
            if(n==N+1)
                break;
            k = a[n];
            a[n] = 0;
            if(k != n)
                result+=1;
            while(k != n)
            {
                result+=1;
                int temp = a[k];
                a[k] = 0;
                k = temp;
            }
        }
        fout<<"Case #"<<t<<": "<<result<<endl;
    }
    return 0;
}
