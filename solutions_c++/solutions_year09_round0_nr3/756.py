#include <fstream>
#include <cstdlib>
#include <iomanip>
#include <string>
#include <iostream>
using namespace std;

ifstream fin("C-large.in");
ofstream fou("p3large.txt");


string input;
const char pat[]="welcome to code jam";

int f[600][21];


int work()
{
	int len = input.length();
    memset( f , 0 , sizeof(f));

    for (int i=0; i<len; i++){
        if (input[i]==pat[0]) f[i][0]=1;
    }

    for (int i=0; i<len; i++)
    for (int k=1; k<=18; k++){
        if (input[i]!=pat[k]) continue;
        int tmp=0;
    	for (int j=0; j<i; j++){
            if (input[j]==pat[k-1]) tmp = (tmp+f[j][k-1])%10000;
        }
        f[i][k]=tmp;
    }

    int ans=0;
    for (int i=0; i<len; i++)
    	ans = (ans+f[i][18])%10000;

    return ans;
}


int main()
{
	string nstr;
    getline( fin , nstr );
	int N;
	N = atoi(nstr.c_str());
    for (int i=1; i<=N; i++){
        getline( fin ,  input );
        //cout << input << endl;
        fou << "Case #" << i << ": " << setw(4) << setfill('0') << work() << endl;
    }


    system("pause");
    return 0;
}
