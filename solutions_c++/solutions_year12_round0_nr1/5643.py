#include<iostream>
using namespace std;

int main()
{
 	int t;
 	string str;
 	char arr[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
 	scanf("%d",&t);
    cin.ignore();
	for(int i=1; i<=t; i++)
	{
        getline(cin,str);
        int l=str.length();
        printf("Case #%d: ",i);
        for(int j=0; j<l; j++)
        {
            if(str[j]==' ')
              cout<<str[j];
            else
              cout<<arr[str[j]-'a'];
        }
        printf("\n");
	}

 	return 0;
}
