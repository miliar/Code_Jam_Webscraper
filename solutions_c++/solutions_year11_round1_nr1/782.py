#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cmath>
#include <sstream>

using namespace std;

int main()
{
    int t;
    scanf("%d", &t);
    for(int i = 0; i < t; i++){
        string wynik = "Case #";
        stringstream ss;
        ss << i + 1;
        wynik += ss.str();
        wynik += ": ";
        long long int n;
        int pd;
        int pg;
        cin >> n;
        scanf("%d %d",&pd, &pg);
        if(pg == 100){
            if(pd == 100) wynik+="Possible";
            else wynik += "Broken";
        }
        else if(pg == 0){
            if(pd == 0) wynik+="Possible";
            else wynik +="Broken";
        }
        else{
        if(n >= 100) wynik+= "Possible";
        else{
            for(int j = 1; j <= n; j++){
            if((j * pd) % 100 == 0){
                wynik += "Possible";
                break;
            } else if (j == n)
                wynik += "Broken";
                }
            }
        }
        cout << wynik << "\n";
    }
    return 0;
}
