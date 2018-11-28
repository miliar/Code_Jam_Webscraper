#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <cmath>
#include <set>
#include <utility>
#include <algorithm>
#include <string>
#include <queue>
#include <map>
#include <list>
#include <stack>

using namespace std;

int main(int argc, char *argv[])
{
    ofstream fout ("a.out");
    ifstream fin ("a.in");
    int t;
    int n;
    vector <int> x;
    vector <int> y;
    int temp;
    fin >> t;
    for(int i=0; i<t; i++)
    {
        fin >> n;
        for(int j=0; j<n; j++)
        {
            fin >> temp;
            x.push_back(temp);
        }
        for(int j=0; j<n; j++)
        {
            fin >> temp;
            y.push_back(temp);
        }
        sort(y.begin(), y.end());
		sort(x.rbegin(), x.rend());
        
        long long sum=0;
        //long long min=9223372036854775807;
        //do
        //{
            for(int j=0; j<n; j++)
            {
                sum+=(x[j]*y[j]);
            }
            //if(sum<min) min=sum;
            //sum=0;
        //}while(next_permutation(y.begin(), y.end()));
        fout << "Case #" << (i+1) << ": " << sum << endl;
		x.clear();
		y.clear();
    }
    

    //system("PAUSE");
    return 0;
}
