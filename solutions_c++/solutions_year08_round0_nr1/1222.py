#include <iostream>
#include <string>
#include <vector>
using namespace std;
#define INF 10000

int result[1002][102];
int que[1002];
void init(int n, int m)
{
    for( int i = 0; i <= m; ++i )
        for( int j = 0; j <= n; ++j )
            result[i][j] = -1;
    for( int i = 0; i <= m; ++i )
        que[i] = 0;
}

int search(string temp, vector<string> v)
{
    for( int i = 0; i < v.size(); ++i )
    {
        if( temp == v[i] )
            return i + 1;
    }
    return 0;
}
int getMin(int x, int y)
{
    if( x > y )
        return y;
    return x;
}
int searchMin( int sea, int k, int n )
{
    int minT = INF;
    for( int i = 1; i <= n; ++i )
    {
        int temp;
        temp = result[k][i];
        if( i != sea )
            ++temp;
        minT = getMin(temp, minT);
        if( minT == 0 )
           return minT;
    }
    return minT;
}
void output(int n, int m, vector<string> v)
{
    for( int i = 1; i <= m; ++i )
        for( int j = 1; j <= n; ++j )
        {
            cout << "i = " << i << " j = " << v[j-1] << "     result = " << result[i][j] << endl;
        }
}
int main()
{
    int ncase;
    cin >> ncase;
    int yoyo = ncase;
    while(ncase--)
    {
        int n, m;
        cin >> n;
        vector<string> v;
        cin.ignore();
        for(int i = 0; i < n; ++i)
        {
            string temp;
            //cin >> temp;
            getline(cin, temp);
            v.push_back(temp);
        }
        cin >> m;
        init(n, m);
        cin.ignore();
        for(int i = 1; i <= m; ++i )
        {
            string temp;
            //cin >> temp;
            getline(cin, temp);
            que[i] = search(temp, v);
//            cout << "i = " << i << "temp = " << temp << "       values = " << que[i] << endl;
        }
//        cout << endl << endl;

        for( int i = 0; i <= n; ++i )
            result[1][i] = 0;
        for( int i = 0; i <= m; ++i )
            result[i][ que[i] ] = INF;
/*
        cout << "After init:" << endl;
        output(n, m);
        */
        for( int i = 2; i <= m; ++i ) //m¸öque
        {
            for( int j = 1; j <= n; ++j ) //n¸ösearch
            {
                if(result[i][j] != -1 )
                    continue;
                int minT = INF;
                result[i][j] = searchMin(j, i - 1, n);
            }
        }
        /*

        cout << "After deal:"<< endl;
        output(n, m, v);
*/
//        cout << result[m][n] << endl;;

        int minT = INF;

        /*cout << "que[12] = " << que[12] << endl;
        cout << "result[12][3]" << result[12][3] << endl;
        */
        for( int i = 1; i <= n; ++i )
        {
//            cout << "minT " << minT << endl;
            minT = getMin(result[m][i], minT);
//            cout << "change:  " << i << endl;
        }
        cout << "Case #"<<yoyo - ncase<<": ";

        if(minT <0 )
           cout << 0 << endl;
        else
            cout << minT << endl;
    }

}
