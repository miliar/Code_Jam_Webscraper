/* @BEGIN_OF_SOURCE_CODE */
/* Author : FameofLight */
#include<rope.h>
#include <set>

#define For(i,x) for(int i=0;i<x;i++)

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);//for input
    freopen("output.txt","w",stdout);//for output
    int t,n,q,a;
    string s;
    cin >> t;
    For(c,t)
    {
            cin >> n;
            getline(cin,s);
            For(i,n)
            {
                    getline(cin,s);
            }
            cin >> q;
            getline(cin,s);
            set<string> z;
            a=0;
            For(i,q)
            {
                    getline(cin,s);
                    z.insert(s);
                    if(z.size()==n)
                    {
                                   a++;
                                   z.clear();
                                   z.insert(s);
                    }
                   
            }
            cout << "Case #" << c+1 << ": ";
            cout << a << endl;
    }
}
                        
                        
                        

