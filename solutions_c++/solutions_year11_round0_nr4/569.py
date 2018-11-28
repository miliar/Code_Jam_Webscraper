#include<fstream>
using namespace std;
ifstream in("D.in");ofstream out("D.out");
bool found[1000];
int perm[1000];
int main(){
    int T,N, a, sum,tmp;
    in>>T;

    for (int t=0;t<T;t++) {
        in>>N;
        sum=0;
        for (int i=0;i<N;i++) {found[i]=false; in>>perm[i];}
        for (int j=0;j<N;j++) {
            if (!found[j]){
                a=j; tmp=1;
                found[j]=true;
                while(perm[a]-1!=j){
                    a=perm[a]-1;
                    found[a]=true;
                    tmp++;
                }
                if (tmp>1) sum+=tmp;
            }
        }
        out<<"Case #"<<t+1<<": "<<sum<<".000000\n";
    }
    return 0;
}
