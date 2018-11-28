#include <iostream>

using namespace std;

char map[26] = { 'y', 'h', 'e', 's', 'o', 'c', 'v',
                'x' , 'd', 'u', 'i', 'g', 'l', 'b',
                'k', 'r', 'z' ,'t', 'n', 'w',
                'j', 'p', 'f' , 'm' , 'a', 'q'};

int main()
{
    char g[120];
    int i,j,n;
    cin>>n;
    cin.getline(g,120,'\n');
    for(i=1;i<=n;i++)
    {
        cin.getline(g,120,'\n');
        cout<<"Case #"<<i<<": ";
        for(j=0;g[j]!=0;j++)
        {
            if(g[j]!=' ')
                cout<<map[g[j]-'a'];
            else
                cout<<" ";
        }
        cout<<endl;
    }
    return 1;
}
