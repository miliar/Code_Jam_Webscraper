#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<stack>
#include<queue>
#include<iomanip>
//#include<fstream>

#define iter(n) for( int i = 0 ; i < n ; i++ )

#define MAX 510

using namespace std;

//typedef vector<int> vint;
//typedef vector<float> vfloat;
//typedef vector<double> vdouble;
//typedef vector<char> vchar;
//typedef vector< pair<int , int> > vpair;

int main()
{
//ifstream cin("C-small.in");
//ofstream cout("C-small.out");

char str[MAX];
const char *pattern = "welcome to code jam";

int tests;
const int pattern_len = 19;

cin >> tests;
cin.get();
for(int t = 0 ; t < tests ; t++)
{
        cin.getline(str,501);
        // cout << str;
        int len = strlen(str);
        int res[19][MAX];
        for(int i = 0 ; i < 19 ; i++)
                res[i][0] = 0;
        
        for(int j = 0 ; j < len ; j++)
                if(pattern[0] == str[j])
                    res[0][j+1] = res[0][j] + 1;
                else
                    res[0][j+1] = res[0][j]; 
                
        for(int i = 1 ; i < 19 ; i++)
                for(int j = 0 ; j < len ; j++)
                        {
                         if(pattern[i] == str[j])
                              {
                               res[i][j+1] = (res[i][j] + res[i-1][j])%1000;
                              }
                         else
                              {
                               res[i][j+1] = res[i][j];
                              }         
                        }
        cout <<  "Case #" << t + 1 << ": " << setfill('0') << setw(4) << res[18][len] << endl;
}


// in.close();
//  system("pause");
return 0;
}
