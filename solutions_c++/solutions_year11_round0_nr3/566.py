#include<fstream>
using namespace std;
ifstream in("C.in");ofstream out("C.out");
int main(){
    int T,g,N,tmp,sum,low;
    in>>T;
    for(int t=0;t<T;t++){
        g=sum=0;
        low=10000001;
        in>>N;
        for (int n=0;n<N;n++) {in>>tmp; g^=tmp; sum+=tmp; if (tmp<low) low=tmp;}
        out<<"Case #"<<t+1<<": ";
        if (g) out<<"NO";
        else out<<sum-low;
        out<<"\n";
    }
    return 0;
}
