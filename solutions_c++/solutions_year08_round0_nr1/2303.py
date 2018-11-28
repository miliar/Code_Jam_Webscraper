#include<iostream>
#include <set>
#include<fstream>
using namespace std;
fstream in("A-large.in",ios::in);
#define cin in
fstream out("output.txt",ios::out);
#define cout out


int main()
{
  
    int tc,n,q,changes;
    string s;
    cin >> tc;
    for(int j=0;j<tc;j++)
    {
            cin >> n;
            getline(cin,s);
            for(int i=0;i<n;i++)
            {
                    getline(cin,s);
            }
            cin >> q;
            getline(cin,s);
            set<string> nik;
            changes=0;
            for(int i=0;i<q;i++)
            {
                    getline(cin,s);
                    nik.insert(s);
                    if(nik.size()==n)
                    {
                                   changes++;
                                   nik.clear();
                                   nik.insert(s);
                    }
                   
            }
            cout << "Case #" << j+1 << ": ";
            cout << changes << endl;
    }
}
                        
                        
                        

