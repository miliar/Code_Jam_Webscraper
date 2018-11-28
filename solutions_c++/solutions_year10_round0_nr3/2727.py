#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

long long int T, R, k, N;
vector<long long int> groups;
long long int temp;
long long int sum;

int main()
{
    ifstream sisend("C-small.in");
    ofstream valjund("C-small.out");

    sisend >> T;

    for(int u = 1; u<=T; u++)
    {
        sisend >> R >> k >> N;
        sum = 0;
        groups.erase(groups.begin(), groups.end());
        for(int i = 1; i<=N; i++)
        {
            sisend >> temp;
            groups.push_back(temp);
        }
        for(int i = 1; i<=R; i++)
        {
            temp=k;
            for(int j = 0 ; j<N; j++)
            {
                temp=temp-groups[0];
                if(temp<0)
                {
                    temp=temp+groups[0];
                    break;
                }
                groups.push_back(groups[0]);
                groups.erase(groups.begin());
            }
            sum += k - temp;
        }
        valjund << "Case #" << u << ": " << sum << endl;
    }



    return 0;
}
