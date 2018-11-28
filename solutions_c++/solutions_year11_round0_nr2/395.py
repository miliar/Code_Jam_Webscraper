#include<iostream>
#include<cstdlib>
#include<fstream>

using namespace std;

bool eq(char x1, char x2, char y1, char y2)
{
    if ((x1==y1)&&(x2==y2))
        return true;
    if ((x1==y2)&&(x2==y1))
        return true;
    return false;
}

int main()
{
    //ifstream cin("B-large.in");
    //ofstream cout("B-large.out");
    int t,c,d,n;
    char cc[40][3], dd[30][2], a[101];
    cin>>t;
    for (int ti=0; ti<t; ti++)
    {
        cin>>c;
        for (int i=0; i<c; i++) cin>>cc[i][0]>>cc[i][1]>>cc[i][2];
        cin>>d;
        for (int i=0; i<d; i++) cin>>dd[i][0]>>dd[i][1];
        cin>>n;
        int m=-1;
        for (int i=0; i<n; i++)
        {
            m++;
            cin>>a[m];
            bool flag=true;
            while (flag)
            {
                if (m==0) 
                    break;
                flag=false;
                for (int j=0; j<c; j++)
                    if (eq(a[m], a[m-1], cc[j][0], cc[j][1]))
                    {
                        m--;
                        a[m]=cc[j][2];
                        flag=true;
                        break;
                    }
            }
            for (int j=0; j<d; j++)
            {
                if (m<=0)
                    break;
                for (int k=0; k<m; k++)
                    if (eq(a[m], a[k], dd[j][0], dd[j][1]))
                    {
                        m=-1;
                        break;
                    }
            }
        }
        cout<<"Case #"<<ti+1<<": [";
        if (m==-1)
            cout<<"]"<<endl;
        if (m>=0)
        {
            cout<<a[0];
            for (int j=1; j<=m; j++)
                cout<<", "<<a[j];
            cout<<"]"<<endl;
        }
    }
  //  for(;;);
    return 0;
}
