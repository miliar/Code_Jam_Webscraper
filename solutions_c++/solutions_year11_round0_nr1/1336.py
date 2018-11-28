#include <iostream>
using namespace std;
struct aaa
{
       int x,y;
};
aaa a,b;
int z,zz,n;

int main()
{
    int i,z,zz,k,g;
    char ch;
    
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin >> z;
    for (zz=1;zz<=z;zz++)
    {
        cin >> n;
        a.x=0;a.y=1;b.x=0;b.y=1;
        for (i=1;i<=n;i++)
        {
            cin >> ch >> k;
            if (ch=='B')
            {
                        g=b.x+abs(k-b.y);
                        if (g<=a.x) g=a.x;
                        b.x=g+1;b.y=k;
                        //cout << "B " << b.x << ' ' << b.y << endl;
            }
            else
            {
                g=a.x+abs(k-a.y);
                if (g<=b.x) g=b.x;
                a.x=g+1;a.y=k;
                //cout << "A " << a.x << ' ' << a.y << endl;
            }
        }
        if (a.x>b.x) cout << "Case #" << zz << ": " << a.x << endl;
        else cout << "Case #" << zz << ": " << b.x << endl;
    }
    return 0;
}
