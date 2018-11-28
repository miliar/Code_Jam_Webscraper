#include <iostream>
#include <string>

using namespace std;

int main()
{
    int N;
    string s;
    const char* str = "welcome to code jam";
    int number[501][20];
    
    cin>>N;
    getline(cin,s);
    for (int i = 0; i < N; i++)
    {
        getline(cin,s);
        for (int j = 0; j < 501; j++)
        {
            number[j][0] = 1;
            for (int l = 1; l < 20; l++)
                number[j][l] = 0;
        }
                
        for (int j = 1; j < 20; j++)
        {
            for (int k = s.size() - 1; k >= 0; k--)
            {
                if (s[k] == str[19 - j])
                    number[k][j] = (number[k+1][j] + number[k+1][j-1]) % 1000;
                else
                    number[k][j] = number[k+1][j];
            }
        }
        
        /*for (int j = 0; j < 20; j++)
        {
            for (int k = 0; k < s.size() + 1; k++)
               cout<<number[k][j]<<" ";
            cout<<endl;
        }*/
        cout<<"Case #"<<i+1<<": ";
        if (number[0][19] >= 1000)
        {
                          cout<<number[0][19] / 1000;
                          number[0][19] = number[0][19] % 1000;
        }
        else
           cout<<0;
        
        if (number[0][19] >= 100)
        {
                          cout<<number[0][19] / 100;
                          number[0][19] = number[0][19] % 100;
        }
        else
           cout<<0;
           
        if (number[0][19] >= 10)
        {
                          cout<<number[0][19] / 10;
                          number[0][19] = number[0][19] % 10;
        }
        else
           cout<<0;
        cout<<number[0][19]<<endl;
    }
    return 0;
}
