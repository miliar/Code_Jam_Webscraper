#include<iostream>

using namespace std;

FILE *fin = freopen("C-large.in","r",stdin);
FILE *fout = freopen("probC.out","w",stdout);

int main() {
    int N, T,i,j;
    cin>>T;
    for(i=0;i<T;i++)
    {
        cin>>N;
        int x;
        cin>>x;
        int sum = x;
        int min = x;
        long long sum2 = x;
        for(j=1;j<N;j++) {
            cin>>x;
            sum ^=x;
            sum2+=x;
            if(min>x)
                min=x;
        }
        cout<<"Case #"<<(i+1)<<": ";
        if(sum)
            cout<<"NO";
        else
            cout<<sum2 - min;
        cout<<"\n";
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
