#include<iostream>
#include<cstdio>
#include<string>
#include<fstream>
using namespace std;
char X[26] = {'y','h','e','s','o','c','v','x',
							'd','u','i','g','l','b','k','r',
							'z','t','n','w','j','p','f','m',
							'a','q'};

int main()
{
	//freopen("myresult.txt","w+",stdout);
	char data[105];
	int n;
	int x = 0;
	scanf("%d",&n);
	getchar();
	for (int i(1); i<=n; ++i) {
		x = 0;
		while ((data[x] = getchar()) != '\n') {
			++x;	
		}
		data[x] = '\0';
		cout<<"Case #"<<i<<": ";
		int len = strlen(data);
		for (int j(0); j<len; ++j) {
			if ('a' <= data[j] && data[j] <= 'z') {
				cout<<X[data[j]-'a'];	
			}	else {
				cout<<data[j];	
			}
		}
		cout<<endl;	
	}
	//system("pause");
	return 0;	
}
