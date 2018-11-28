#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{

    string in[30];
    char str[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

    int T;
    cin>>T;

	int x;
	cin>>x;

    for(int i=0;i<T;i++)
	{
        getline(cin,in[i]);
    }
    
    for(int i=0;i<T;i++){
        for(int j=0;j<in[i].size();j++)
        {
            if(in[i][j]!=' ')
                in[i][j]=str[int(in[i][j])-97];
        }
        cout<<"Case #"<<i+1<<": "<<in[i]<<endl;
    }
    getchar();
    getchar();
    return 0;
}
