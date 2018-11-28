#include<iostream>
#include<string>
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    int c,d,n;
    int length;
    int i,j,k,l,m;
    string combine[40];
    string conflict[28];
    string magic;
    char c1, c2;
    cin>>t;
    bool b,con;
    for (i = 1; i <= t; i++)
    {
        cin>>c;
        for (j = 0; j < c; j++)
            cin>>combine[j];
        cin>>d;
        for (j = 0; j < d; j++)
        {
            cin>>conflict[j];
        }
        cin>>length;
        cin>>magic;
        b = false;
        for (j = 1; j < length; j++)
        {
            if (b)
            {
                  b = false;
            }
            b = false;
            c1 = magic[j];
            c2 = magic[j-1];
            for (k = 0; k < c; k++)
            {
                if ((c1==combine[k][0] && c2==combine[k][1]) || (c2==combine[k][0] && c1==combine[k][1]))
                {
                    magic[j] = combine[k][2];
                    magic[j-1]='0';
                    b = true;
                }
            }
            if (!b)
            {
               con = false;
               for (k = 0; k < j; k++)
               {
                   for (l = 0; l < d; l++)
                   {
                       if ((magic[k]==conflict[l][0]&&c1==conflict[l][1]) || (magic[k]==conflict[l][1]&&c1==conflict[l][0]))
                       {
                          for (m=0;m<=j;m++)
                              magic[m]='0';
                          con = true;
                       }
                   }
                   if (con)
                      break;
               }
            }
        }
        cout<<"Case #"<<i<<": [";
        bool first = true;
        for (j=0;j<length;j++)
        {
            if (magic[j]!='0')
            {
               if (first)
               {
                  cout<<magic[j];
                  first = false;
               }
               else cout<<", "<<magic[j];
            }
        }
        cout<<']'<<endl;
    }
    return 0;
}
