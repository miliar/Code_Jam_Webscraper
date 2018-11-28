#include <iostream>

using namespace std;

int main(){
    int n;
    cin >> n;
    int ok;
    int maybe;
    for(int j=0;j<n;j++){
        int n2;
        cin >> n2;
        ok = 0;
        maybe = 0;

        int s;
        cin >> s;

        int max;
        cin >> max;

        for(int i=0;i<n2;i++){
            int num;
            cin >> num;
            if(num>= 3*max-2)
                ok++;
            else if(num>= 3*max-4 && max>=2 )
                maybe++;
        }
        int ret = ok+ min(maybe,s);
        //cout << ok<<maybe << s;
        cout << "Case #" << j+1 << ": " << ret << endl;
    }
}


