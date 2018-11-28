
#include <iostream>
#include <vector>
#include<set>
#include <fstream>
using namespace std;

ifstream in ("in.txt");

ofstream out ("output.txt");

#define cout out
#define cin in

int main()
{
    int t,n,q;
    cin >> t;
    string s;
    
    for(int c=1;c<=t;c++)
    {
            cin >> n;
            getline(cin,s);
            for(int i=0;i<n;i++)
            getline(cin,s);
            cin >> q;
            getline(cin,s);
            set<string> z;
            int ans=0;
            for(int i=0;i<q;i++)
            {
                    getline(cin,s);
                    z.insert(s);
                    if(z.size()==n)
                    {
                                   z.clear();
                                   ans++;
                                   z.insert(s);
                    }
            }
            cout << "Case #"<<c<<": "<< ans << endl;
    }
}
            
