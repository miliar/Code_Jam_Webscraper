#include <iostream>
#include <fstream>
using namespace std;
int A,B;
int n_lenght(int a){
    int exp=1;
    while(a>0){
        a=a/10;
        exp=exp*10;
    }
    return exp/10;
}
int create_pairs(int n){
    int bn=n;
    int pairs=0;
    int exp=n_lenght(n);
    bool f=true;
    while(bn!=n||f){
        int l=n%10;
        n=n/10;
        n=n+l*exp;
        if(bn<n&&n>A&&n<=B) {pairs++;}
        f=false;
    }
    return pairs;
}
int main()
{
    int T;
    ifstream ifile;
    ifile.open("input.txt");
    ofstream ofile;
    ofile.open("output.txt");
    ifile>>T;
    for(int i=0;i<T;i++){
        ifile>>A>>B;
        int n;
        int ans=0;
        for(n=A;n<B;n++){
            ans=ans+create_pairs(n);
        }
        ofile<<"Case #"<<i+1<<": "<<ans<<endl;
    }
    return 0;
}
