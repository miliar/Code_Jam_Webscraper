#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;
int a[26]={24,7,4,18,14,2,21,23,3,20,8,6,11,1,10,17,25,19,13,22,9,15,5,12,0,16};
int main(){
    int t;
    scanf("%d\n",&t);
    string s;
    for (int k=0;k<t;k++){
        getline(cin,s);
        printf("Case #%d: ",k+1);
        for (int i=0;i<s.length();i++)
            if ((s[i]-'a'<26)&&(s[i]-'a'>=0))
                cout << char(a[s[i]-'a']+'a');
            else
                cout << s[i];
        cout << endl;
    }
    return 0;
}
