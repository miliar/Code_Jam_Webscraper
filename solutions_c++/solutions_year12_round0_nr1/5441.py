#include <iostream>
#include <cstdlib>
#include <cstdio>
using namespace std;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);

    //now start to solve the problem

    string input;
    char newline;
    char mapping[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    int testDataNum=0;
    int index=0;

    cin>>testDataNum;
    getline(cin,input);
    while(++index<=testDataNum)
    {
        getline(cin,input);

        cout<<"Case "<<"#"<<index<<": ";
        for(int i=0;i<input.size();i++)
        {
                if(input[i]==' ')
                    cout<<input[i];
                else
                {
                    cout<<mapping[ int(input[i])-97 ];
                }
        }
        cout<<endl;

    }



    fclose(stdin);
    fclose(stdout);
    return 0;
}
