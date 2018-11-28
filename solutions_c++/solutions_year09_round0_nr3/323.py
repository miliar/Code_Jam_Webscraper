
#include <iostream>


using namespace std;

const int keylen = 19;
char key[] = "welcome to code jam";
int substr[keylen];
//char s[501];
char c;

int main()
{
    FILE* in = freopen("C-large.in", "r", stdin);
    FILE* out = freopen("C-large.out", "w+", stdout);

    int cases;
    cin>>cases;
    for(int q = 1;q<=cases;++q)
    {
        memset(substr, 0, sizeof(substr));

        do
        {
        scanf("%c", &c);
        }
        while('\n'==c);

        while('\n' != c && !feof(in))
        {
            if(c == key[0])
                substr[0] += 1;
            for(int j=keylen;j>0;--j)
            {
                if(c == key[j])
                {
                    substr[j]+=substr[j-1];
                    substr[j]%=10000;
                }
            }
            scanf("%c", &c);
        }

        int r = substr[keylen-1];
        cout<<"Case #"<<q<<": ";
        if(r<10)
            cout<<"0";
        if(r<100)
            cout<<"0";
        if(r<1000)
            cout<<"0";
        cout<<r<<'\n';
    }
}
