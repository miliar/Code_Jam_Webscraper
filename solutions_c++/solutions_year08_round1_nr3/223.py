#include <iostream>
#include <fstream>
using namespace std;
string ans[]={"005","027","143","751","935","607","903","991","335","047","943",
              "471","055","447","463","991","095","607","263","151","855","527",
              "743","351","135","407","903","791","135","647"};
int i,n,x;
int main(){
    ifstream fin("C-small.in");
    ofstream fout("C-small.out");
    fin>>n;
    for(i=1;i<=n;i++){
        fin>>x;
        fout<<"Case #"<<i<<": "<<ans[x-1]<<endl;
    }    
}    
