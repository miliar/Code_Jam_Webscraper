#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int max (int a,int b)
{
    if (a>b)
    { return a;   }
    else {return b;}
}

int main(void)
{
    string s1 = "welcome to code jam";
    int arr[505][2];
    string s;
    getline(cin,s);
    stringstream ss(s);
    int n;
    ss >> n;
    for (int i = 0; i<n; i++)
    {
        for (int j = 0; j < 505 ; j++)
        {
            arr[j][0] = 0;
            arr[j][1] = 0;
        }
        getline(cin,s);
        int count = 0;
        for (int j = 0; j < s.length() ; j++)
        {  if (s[j]=='w') { count++;}  arr[j+1][0] = count;    }
        for (int k=1; k< s1.length(); k++)
        {
            for (int j = 0; j < s.length() ; j++)
            {
                if (s[j]==s1[k])
                {
                    arr[j+1][k%2] = (arr[j+1][(k+1)%2] + arr[j][k%2]) % 10000;
                }else
                {
                    arr[j+1][k%2] = arr[j][k%2] % 10000;
                }
            }        
        }
        int temp = arr[s.length()][(s1.length()+1)%2] + 10000;
        cout << "Case #" << i+1 << ": " << (temp/1000)%10 << (temp/100)%10 << (temp/10)%10 << temp%10 <<endl;
    }
}
