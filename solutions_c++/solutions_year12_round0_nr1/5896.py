#include<iostream>
#include<string.h>
#include<cstdio>
using namespace std;
int main()
{
	char map[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'},g[100];
	int test,i,j=0;
	char c;
        cin>>test;
        getchar();
        while(test--)
        {
                i=0;
                cin.getline(g,100);
                cout<<"Case #"<<++j<<":"<<" ";
                while(c=g[i++])
                        if(c!=' ')
                        cout<<map[c-'a'];
                        else cout<<" ";
                cout<<endl;
         }
}
                
