#include <cstdlib>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#define MAXN 30


using namespace std;

char key[MAXN]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
string in,ans;
int main(int argc, char *argv[])
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("a.out","w",stdout);
    int size,n;
    int i,j,k;
    scanf("%d",&n);
	getline(cin,in);
    for(k=1;k<=n;k++)
    {
        getline(cin,in);
        size=in.length();
        ans.clear();
        for(i=0;i<size;i++)
        {
            if(in[i]>'z'||in[i]<'a')
            {
                ans.push_back(' ');
            }
            else
            ans.push_back(key[in[i]-'a']);
        }
        cout<<"Case #"<<k<<": "<<ans<<endl;
    }
    
   // system("PAUSE");
    return 0;
}
