#include <fstream>
#include <string>
using namespace std;

ifstream cin("A-small-attempt1.in");
ofstream cout("A-small-attempt1.out");

const char lang[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r',
                        'z','t','n','w','j','p','f','m','a','q'};

int main() {
    int n, i, j;
    string original;

    cin>>n;
    for (i=0;i<n;++i) {
        original = "";
        while (original.empty()) getline(cin, original);
        for (j=0; j<original.length(); ++j) {
            if (original[j]>='a' && original[j]<='z')
                original[j] = lang[original[j]-97];
        }
        cout<<"Case #"<<i+1<<": "<<original<<endl;
    }
    return 0;
}
