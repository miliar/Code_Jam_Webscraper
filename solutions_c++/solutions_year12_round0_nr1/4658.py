#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <iostream>
using namespace std;
char f[27] = {'y','h','e','s','o','c','v','x','d','u','i','g','l',
'b','k','r','z','t','n','w','j','p','f','m','a','q','\0'};
int main()
{
    freopen("test.in","r",stdin);
    freopen("test.txt","w",stdout);
    char G[110];
    int T;
    scanf("%d",&T);
    cin.ignore(10,'\n');
	for(int k=1;k<=T;k++)
	{
	    cin.getline(G,110);
	    int len = strlen(G);
	    cout<<"Case #"<<k<<": ";
	    for(int i=0;i<len;i++)
	    {
            cout<<f[G[i]-'a'];
	    }
	    cout << endl;
	}
	return 0;
}
