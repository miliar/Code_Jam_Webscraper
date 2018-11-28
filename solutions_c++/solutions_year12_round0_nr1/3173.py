#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <sstream>

using namespace std;

void convertGooglereseLine(map<char,char> dict) {
    char x;
    while ((x = getchar()) != '\n') {
        cout<<dict[x];
    }
}

int main(void)
{
    /* Prepare for Problem */
    map<char,char> dict;
    
    string sampleTestCase = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv zq";
    string sampleTestCaseOutput = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up qz";
    
    for (int i=0; i<sampleTestCase.size(); i++) {
        if (!dict[sampleTestCase[i]]) {
            dict[sampleTestCase[i]] = sampleTestCaseOutput[i];
            //for handling upper case
            dict[sampleTestCase[i]-32] = sampleTestCaseOutput[i]-32;
        }
    }
    
    /* Start Solving Probelem */
    
    freopen("Input.txt", "r", stdin);
    freopen("OutputText.txt", "w", stdout);
    
    int T;
    scanf("%d",&T);getchar();

    for (int i = 1; i<=T; i++) {
        cout<<"Case #"<<i<<": ";
        convertGooglereseLine(dict);
        cout<<endl;
    }

    return 0;
}
