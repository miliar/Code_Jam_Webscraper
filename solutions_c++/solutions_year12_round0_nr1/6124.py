#include<iostream>
#include<string>
#include<cstdio>
using namespace std;

/*
Goolerese:

ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv


English:

our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up

*/

char eng[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q',};

int main()
{

	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);

	int t,c=1;
	cin>>t;
	cin.get();
	//getch();
	while(t--){
		string g;
		getline(cin,g);
		int len=g.length();
		cout<<"Case #"<<c++<<": ";
		for(int i=0;i<len;i++){
			if(g[i]==' ')
				cout<<" ";
			else
				cout<<eng[g[i]-97];
		}
		cout<<endl;
	}
}
