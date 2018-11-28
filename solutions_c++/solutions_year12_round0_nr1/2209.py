#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int main(){
    char G[26] = {'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e'
    ,'v','z','p','d','r','j','g','t','h','a','q'};
    int n;
    cin >> n;
    cin.get();
    ofstream fout;
    fout.open("output.txt");
    for (int i=0; i<n; i++){
        string s, t="";
        getline(cin, s);
        for (int j=0; j<s.length(); j++){
            if (s[j]>='a' && s[j]<='z') {
               for (int k=0; k<26; k++)
                   if (G[k] == s[j])
                      t += (char)(97+k);
            } else t += s[j];
        }
        fout << "Case #" << i+1 << ": " << t << endl;
    }
    fout.close();
    return 0;
}
