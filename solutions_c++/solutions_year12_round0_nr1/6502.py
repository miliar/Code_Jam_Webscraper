#include <iostream>
#include <utility>
#include<cstring>
#include<cstdio>
#include<cmath>
#include <vector>
#include<ctime>
#include <cstdlib>
#include <fstream>
#include <sstream>
using namespace std;

using namespace std;
char alph[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

void main2()
{
	
	string a;
	getline (cin,a);
	int n=a.size();
	
	

	for(int i=0;i<n;i++)
	if(a[i]==' ')continue;
	else a[i]=alph[a[i]-'a'];
	
	cout<<a<<endl;

	

}


int main(){

    	
    	int T,t;
        scanf("%d",&T);
		char c;c=getchar();
	for(t=0;t<T;t++){
		printf("Case #%d: ",t+1);
		main2();
	}


	return 0;
}
