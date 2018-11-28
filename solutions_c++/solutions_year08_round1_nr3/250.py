#include <iostream>
#include <cstring>
#include <cmath>

using namespace std;
//                         2     3     4     5     6     7    8     10   11     12     13    14  15     16    17    18    19    20    21    22    23    24   25     26    27   28     29
char ans[31][5]={"0","1","027","143","751","935","607","903","991","335","047","943","471","055","447","463","991","095","607","263","151","855","527","743","351","135","407","903","791","135","647"};

int main(){
    
    freopen("c.in","r",stdin);
    freopen("c.txt","w",stdout);
    
    int i,n;
    cin >> n;
    
    for( i=1;i<=n;i++ ){
        int pos;
        cin >> pos;
        printf("Case #%d: %s\n",i,ans[pos]);
    }
    
    
    return 0;
}
