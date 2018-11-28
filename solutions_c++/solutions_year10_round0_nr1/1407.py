#include<fstream>
using namespace std;

int main(){
    ifstream in("a.in");
    ofstream out("a.out");

    int t;
    in>>t;
    for(int i=0;i<t;i++){  
            int n, k;
            in>>n;
            in>>k;
            out<<"Case #"<<(i+1)<<": ";
            if((k+1)%(1<<n)==0)
                                out<<"ON\n";
            else out<<"OFF\n";
   }
   in.close();
   out.close();
}
