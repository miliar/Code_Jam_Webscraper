#include <iostream>
#include <vector>
#include <fstream>
using namespace std;
typedef unsigned short int USHORT;


int main()
{
    ifstream cin ("small.in");
    ofstream cout ("output.txt");

//    int nn;
//    cin >> nn;
//    queue<int> a1;
//    queue<int> a2;
//
//    for (int i = 0; i < nn; i++){
//        int temp;
//        cin >> temp;
//        a1.push(temp);
//    }
//
//    a2.push(4);
//    a2.push(6);
//
//    while (!a2.empty()){
//        a1.push(a2.front());
//        a2.pop();
//    }
//
//    while (!a1.empty()){
//        cout << a1.front() << endl;
//        a1.pop();
//    }

//    cout << a1.size() << endl;
//    cout << a2.size() << endl;

    int t;
    cin >> t;
    for (int i = 0; i < t; i++){
        int r, k, n;
        cin >> r >> k >> n;

        vector<USHORT> v;
        v.clear();

        for (int j = 0; j < n; j++){
            int temp;
            cin >> temp;
            v.push_back(temp);
        }

        int totalMoney = 0;
        int marker = 0;

        for (int l = 0; l < r; l++){
            int cPop = 0;
            bool notFirst = false;
            int ctr = 0;

            for (int j = marker; j < n; j++){
                ctr++;
                if (cPop + v[j] <= k){
                    cPop += v[j];
                }
                else{
                    marker = j;
                    break;
                }

                if (j==n-1 && ctr != n){
                    j = -1;
                    continue;
                }
                if (ctr==n){
                    marker = j;
                    break;
                }
            }

            totalMoney += cPop;
        }

        cout << "Case #" << i+1 << ": " << totalMoney << endl;
    }




    return 0;
}
