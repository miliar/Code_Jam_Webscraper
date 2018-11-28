#include <iostream>
#include <string>
#include <algorithm>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main()
{
    string s("Hello");
    string t("Hello");
    char stemp[10];
    memset(stemp,0,sizeof(stemp));
    sprintf(stemp,"%d  !",132);
    for(int j=0;j<10;j++)
    cout<<stemp[j];
    cout<<endl;

    return 0;
}
