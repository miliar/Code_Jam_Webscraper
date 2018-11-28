#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <map>
using namespace std;
typedef pair <char,char>pcc;
int main()
{
        char google[100],translate[1000];
        char langcode[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
        gets(google);
        int T=atoi(google);
        for(int google=1;google<=T;++google)
        {
                printf("Case #%d: ",google); 
                gets(translate);
                for(int i=0;i<strlen(translate);++i)
                {
                        if(translate[i]==' ')
                        {
                        cout<<" ";
                        }
                        else
                        {
                        cout<<langcode[(int)translate[i]-'a'];
                        }
                        
                }
                cout<<endl;
        }
        
        return 0;
}
