#include <iostream>
#include <vector>

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    
    int t;
    cin >> t;
    for (int i=1; i<=t; i++)
    {
        int n,m,k;
        bool D[30][30]={0};
        char C[30][30];
        for (int j=0; j<30; j++)
            for (int h=0; h<30; h++)
            {
                C[j][h]='%';
                D[j][h]=false;
            }
        vector <char> a;
        cin >> n;
        for (int j=0; j<n; j++)
        {
            char x,y,z;
            cin >> x>> y >> z;
            C[int(x)-'A'][int(y)-'A']=z;
            C[int(y)-'A'][int(x)-'A']=z;
        }
        cin >> m;
        for (int j=0; j<m; j++)
        {
            char x,y;
            cin >> x >> y;
            D[int(x)-'A'][int(y)-'A']=true;
            D[int(y)-'A'][int(x)-'A']=true;
        }
        cin >> k;
        for (int j=0; j<k; j++)
        {
            char x;
            cin >> x;
            a.push_back(x);
            if (a.size()>1)
            {
                if (C[int(a[a.size()-1])-'A'][int(a[a.size()-2])-'A']!='%')
                {
                    char r=C[int(a[a.size()-1])-'A'][int(a[a.size()-2])-'A'];
                    a.pop_back();a.pop_back();
                    a.push_back(r);
                }
                else
                {
                    if (C[int(a[a.size()-2])-'A'][int(a[a.size()-1])-'A']!='%')
                    {
                        char r=C[int(a[a.size()-2])-'A'][int(a[a.size()-1])-'A'];
                        a.pop_back();a.pop_back();
                        a.push_back(r);
                    }
                }
                for (int q=0; q<a.size(); q++)
                    for (int w=0; w<a.size(); w++)
                        if (D[int(a[q])-'A'][int(a[w])-'A']) 
                        {
                            a.clear();
                            break;
                        }
            }
        }
        cout << "Case #" << i << ": [";
        if (a.size()>0)
        {
            for (int i=0; i<a.size()-1; i++) cout << a[i] << ", ";
            cout << a[a.size()-1] << "]" << endl;
        }
        else cout << "]" << endl;
    }
    return 0;
}
