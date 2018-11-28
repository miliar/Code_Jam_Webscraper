#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    string a="ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvzq";
    string b="ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupqz";
    vector<int> v(26,-1);
    for (int i=0;i<int(a.size()); ++i) {
        v[a[i]-'a'] = b[i]-'a';
    }
    //for (int i = 0;i < 26;++i) cout << char('a'+i) << " " << char('a'+v[i]) << endl;
    
    int t; cin >> t;
    string s;
    getline(cin,s);//enline
    for (int cas=1;cas<=t;++cas) {
        getline(cin,s);
        for (int i = 0;i<int(s.size());++i) if (s[i]!=' ') s[i]=char(v[s[i]-'a']+'a');
        cout << "Case #" << cas <<": " << s << endl;
    }
}
