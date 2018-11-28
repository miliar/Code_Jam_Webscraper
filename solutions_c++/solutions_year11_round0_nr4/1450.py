#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    //ifstream cin("D-large.in");
    //ofstream cout("output4.txt");
    int num = 0;
    int length = 0;
    int temp = 0;
    int count = 0;
    //fin >> num;
    cin >> num;
    for(int i = 0; i < num; i++)
    {
        cin >> length;
       // fin >> length;
        for(int j = 0; j < length; j++)
        {
            //fin >> temp;
            cin >> temp;
            if(temp != j+1)
            count++;
        }
        cout << "Case #" << i+1 << ": " << count << ".000000" << endl;
       // fout << "Case #" << i+1 << ": " << count << ".000000" << endl;
        count = 0;
        temp = 0;
    }
    return 0;
}
