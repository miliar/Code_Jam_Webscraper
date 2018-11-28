#include <iostream>
#include <string>

using namespace std;


int problemB(){
    int ncases, ccase = 0;
    cin >> ncases;
    while (ccase++ < ncases){
        int r, k, n;
        cin >> r >> k >> n;
        int groups[n];
        for (int i=0; i<n; i++){
            cin >> groups[i];
        }
        int curr = 0;
        float amount = 0;
        for (int i=0; i<r; i++){
            int total = groups[curr];
            int initial = curr;
            while (total <= k){
                curr++;
                if (curr == n)
                    curr = 0;
                if (curr == initial)
                    break;
                if (total + groups[curr] <= k){
                    total += groups[curr];
                }else
                    break;
            }
            amount += total;
        }
        cout << "Case #" << ccase << ": " << amount << endl;
    }


    return 0;
}

int main()
{
   return problemB();
}
