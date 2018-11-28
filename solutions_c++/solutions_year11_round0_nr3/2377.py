#include <iostream>
#include<fstream>
#include<algorithm>
#include<vector>
using namespace std;

int main()
{
    ifstream f_in("D:\\inp.txt");
    ofstream f_out("D:\\out.txt");
    int t,N;
    f_in >> t;
    for(int itri = 0 ; itri < t ; itri++)
    {
        f_in >> N;
        vector<long long> arr(N);

        for(int itr = 0 ; itr < N ; itr++)
            f_in >> arr[itr];

        sort(arr.begin(),arr.end());
        long long temp1, temp2, temp3, temp4, itr;

        for(itr = 0 ; itr < N - 1 ; itr++)
        {
            temp3 = arr[itr];
            temp4 = arr[itr + 1];
            temp1 = arr[itr];
            temp2 = arr[itr + 1];

            for(int itrj = itr-1 ; itrj >= 0 ; itrj--)
            {
                temp3 += arr[itrj];
                temp1 ^= arr[itrj];
            }

            for(int itrj = itr + 2 ; itrj < N ; itrj++)
            {
                temp4 += arr[itrj];
                temp2 ^= arr[itrj];
            }

            if(temp1 == temp2)
            break;
        }

        if(itr == (N - 1))
            f_out<<"Case #"<<itri+1<<": NO"<<endl;
        else if(temp3 > temp4)
            f_out<<"Case #"<<itri+1<<": "<<temp3<<endl;
        else
            f_out<<"Case #"<<itri+1<<": "<<temp4<<endl;

    }
    return 0;
}
