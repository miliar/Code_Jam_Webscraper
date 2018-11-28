#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
    int t;
    char A[101];
    scanf("%d",&t);
    char B[27]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    for(int j=0; j<t+1; j++)
    {
        //cout<<"Estoy leendo"<<endl;
		gets(A);
		//cout<<"!!!Aqui!!"<<endl;
		if(j!=0)
		{	
			int tam;
		    tam=strlen(A);
			//cout<<A;
		    for(int i=0; i<tam; i++)
		    {
		        if(A[i]!=' ')
					A[i]=B[A[i]-'a'];
		    }
			cout<<"Case #"<<j<<": "<<A<<endl;
		}    
	}
}

