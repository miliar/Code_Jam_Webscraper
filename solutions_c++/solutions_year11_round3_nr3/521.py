#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <sstream>
using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int k = 1; k <= t; k++){
        int n,l,h;
        scanf("%d%d%d", &n, &l, &h);
        int *notes = new int[n];
        for(int i = 0; i < n; i++){
            scanf("%d", &notes[i]);
        }
        bool final = false; int endish;
        for(int note = l; (note <= h) && !(final); note++){
            bool result = true;
            for(int i = 0; i < n; i++){
                if((note % notes[i]) && (notes[i] % note)){
                    result = false;
                    break;
                } else if(i == n - 1){
                    endish = note;
                }
            }
            if(result == true)
                final = true;
        }
        cout << "Case #"<<k<<": ";
        if(!final){
            cout <<"NO"<<endl;
        } else cout << endish << endl;
        delete[] notes;
    }
    return 0;
}
