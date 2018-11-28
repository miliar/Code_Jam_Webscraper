#include<iostream>
#include<cmath>
#include<set>
using namespace std;

int T, A, B, caso, res, length, lengthNum, mult, num, i, j;

int recPairs()
{
    set<pair<int, int> > res;

    for (i = A; i <= B; i++)
    {
        length = (i == 0) ? 1 : (int)log10(i) + 1;
        mult = 1;
        for (j = 0; j < length-1; j++)
        {
            mult*=10;
        }
        num = i;
        for (j = 0; j < length; j++)
        {
            num = (num/10) + ((num%10)*mult);
            lengthNum = (num == 0) ? 1 : (int)log10(num) + 1;
            if(length == lengthNum && i < num && A <= num && num <= B)
                res.insert(pair<int, int>(i, num));
        }
    }
    return res.size();
}


int main()
{
    cin >> T;
    for (caso = 1; caso <= T; caso++)
    {
        cin >> A >> B;
        cout << "Case #" << caso << ": " << recPairs() << endl;
    }
}
