#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    //ifstream cin("C-large.in");
    //ofstream cout("output3.txt");

    int num = 0;
    int length = 0;
    int temp = 0;
    int min = 1000001;
    int total = 0;
    int sum = 0;
    cin >> num;
    for(int i = 0; i < num; i++)
    {
        cin >> length;
        for(int j = 0; j < length; j++)
        {
            cin >> temp;
            if(temp < min)
            min = temp;
            total ^= temp;
            sum += temp;
        }
        if(total != 0)
        cout << "Case #" << i+1 << ": " << "NO" << endl;
        else
        cout << "Case #" << i+1 << ": " << sum-min << endl;
        min = 1000001;
        temp = 0;
        total = 0;
        sum = 0;
    }
    return 0;
}
