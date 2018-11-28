
#include <iostream.h>
using namespace std;
int main()
{

    int num;
    char b[]={'y','h','e','s','o','c','v','x','d','u','i',
                'g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    char c[110][110];
    char a;
    int date;
    freopen("A-small-attempt2.in","r",stdin);
    cin>>num;
    getchar();

    for(int i=0;i<num;i++)
    {

                gets(c[i]);
                date=strlen(c[i]);
                for(int j=0;j<date;j++)
                {
                    if(c[i][j]==' ')
                    {
                        c[i][j]=' ';
                    }
                    else
                    {
                    int d=c[i][j];
                    d=d-97;
                    c[i][j]=b[d];
                    }
                }
                c[i][date]='\0';

    }
     freopen("file.txt", "w", stdout);
    for(int i=0;i<num;i++)
    {
        cout<<"Case #"<<i+1<<": "<<c[i]<<endl;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
