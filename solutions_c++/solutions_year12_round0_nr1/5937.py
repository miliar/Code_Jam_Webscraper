#include<iostream>
#include<string>
#include<stdio.h>

using namespace std;
string arr[101];
int key[27]={121,104,101,115,111,99,118,120,100,117,105,103,108,98,107,114,122,116,110,119,106,112,102,109,97,113};

int main()
{
    int n,i,j;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    cin >> n;
    getline(cin,arr[0]);

    for(i=0;i<n;i++)
        getline(cin,arr[i]);

    for(i=0;i<n;i++)
    {
        for(j=0;j<arr[i].length();j++)
        {
            if(arr[i][j]!=' ')
                arr[i][j] = key[((int)arr[i][j])-97];
        }
        cout << "Case #" << i+1 << ": " << arr[i] << endl;
    }
    return 0;
}
