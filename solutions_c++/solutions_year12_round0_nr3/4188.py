#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>

using namespace std;

void shift_str(char* str, int k){
    char temp[strlen(str) + 1];
    temp[strlen(str)] = '\0';
    
    for (int i = 0; i < strlen(str); ++i)
    {
        temp[i] = str[(i+k) % (strlen(str))];
    }

    strcpy(str, temp);
}

int main(int argc, char *argv[])
{
    int t;
    cin >> t;

    for (int i = 0; i < t; ++i)
    {
        int a,b;
        cin >> a >> b;

        int result = 0;
        for (int j = a; j < b; ++j)
        {
            char str[8];
            sprintf(str, "%d", j);

            for (int k = 1; k < strlen(str); ++k)
            {
                shift_str(str, 1);

                if(atoi(str) > j && atoi(str) <= b){
                    result++;
                }
            }
        }
        cout<<"Case #"<<i+1<<": "<<result<<endl;        
    }
    return 0;
}
