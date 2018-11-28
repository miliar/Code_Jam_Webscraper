#include <iostream>
#include <fstream>
using namespace std;

#define INPUT "a.in"
#define OUTPUT "a.out"

#define abs(a) ((a>0)?(a):(-(a)))

int main(){

    freopen(INPUT,"r",stdin);
    freopen(OUTPUT,"w",stdout);

    int test;
    cin >> test;
    for (int task =1;task<=test;task++)
    {
        int b=1,o=1,tb=0,to=0,n,pos;
        char c;
        cin >> n;
        while (n-- > 0){
            cin >> c;
            if (c == 'B'){
                cin >> pos;
                tb = max(abs(pos-b)+tb,to)+1;
                b = pos;
//                cerr << "B" <<pos <<"|"<<tb<<endl;
            } else if (c == 'O') {
                cin >> pos;
                to = max(abs(pos-o)+to,tb)+1;
                o = pos;
//                cerr << "O" <<pos <<"|"<<to<<endl;
            }
        }

        cout << "Case #" << task << ": " << max(tb,to) <<endl;
    }


}
