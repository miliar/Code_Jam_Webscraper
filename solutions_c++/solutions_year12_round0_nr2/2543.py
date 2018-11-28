#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int n;
    cin >> n;
    for (int i=0;i<n;i++)
    {
        cout << "Case #" << i+1 << ": ";
        int N,s,p;
        cin >> N >> s >> p;


            int nonzero=0;
            int type_1=0,type_2=0;
            for (int j=0;j<N;j++)
            {
                int temp;
                cin >> temp;
                if (temp!=0) nonzero++;
                if (temp>=3*p-2) type_1++;
                if (temp>=3*p-4&&temp<3*p-2) type_2++;
            }
            if (p==0) cout << N << endl; else {
            if (p==1) cout << nonzero << endl; else
            {
                if (type_2>s) cout << type_1+s <<endl; else cout << type_1+type_2 <<endl;
            }
            }

    }
    return 0;
}
