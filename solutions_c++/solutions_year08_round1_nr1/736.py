#include <vector>
#include <fstream>
#include <iostream>
using namespace std;

int main()
{
    ifstream in("A-small-attempt0.in");
    ofstream out("A-small-attempt0.out");

    int T;


    in >> T;

    for(int t = 0; t < T; t++)
    {
        int n;
        vector<int> X,Y;

        in >> n;

        out << "Case #" << t << ": ";

        for(int nx = 0; nx < n; nx++)
        {
            int x;
            in >> x;
            X.push_back(x);
        }

        for(int ny = 0; ny < n; ny++)
        {
            int y;
            in >> y;
            Y.push_back(y);
        }

        sort(X.begin(),X.end());
        sort(Y.begin(),Y.end());

        int sum = 0;
        for(int x = 0, y = n -1; x < n; x++,y--)
            sum += X[x]*Y[y];

        out << sum << endl;

    }

    in.close();
    out.close();

    return 0;
}
