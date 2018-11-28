#include <cstdlib>
#include <iostream>
#include <cmath>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <complex>
#include <algorithm>
#include <functional>
#include <fstream>
#include <numeric>
#include <string>
#include <valarray>
#include <queue>
#include <set>

using namespace std;

#define show(s) cout << #s << "-->" << s << endl;
#define show1(x,y,z) cout << #x << " , " << y << " , "<< z<< "-->" << x << endl;

int main()
{

    char hash[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q' };

    int n;
    scanf("%d", &n);
    string input;
    getline(cin, input);
    for (int i = 0; i < n; i++)
    {
        getline(cin, input);
        printf("Case #%d: ",i+1);
        for(int j=0; j< input.size(); j++){
            if(input[j] != ' ')
            {
                printf("%c", hash[((int)input[j]-97)]);
            }
            else
                printf("%c", input[j]);
        }
        printf("\n");
    }


    return 0;
}