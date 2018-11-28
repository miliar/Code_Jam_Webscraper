#include <iostream>
#include <fstream>
#include <map>


using namespace std;

int main()
{
    ifstream fin("file.in");
    ofstream fout("file.out");
    string s;
    int t;
    fin >> t;
    for(int i=0; i<t; i++) {
        fin >> s;
        map<char, int> b;
        map<char, int>::iterator iter;
        b[s[0]]=1;
        int count=0;
        for(int j=1; j<s.length(); j++) {
            iter=b.find(s[j]);
            if(iter==b.end())
                b[s[j]]=count++;
            if(count==1)
                count++;
        }
        int ans=0, base=b.size(), val=0, mul=1;
        if(base==1)
            base=2;
        for(int j=s.length()-1; j>=0; j--) {
            ans+=b.find(s[j])->second*mul;
            mul*=base;
        }
        fout << "Case #" << i+1 << ": " << ans << endl;
    }
    fin.close();
    fout.close();
    return 0;
}
