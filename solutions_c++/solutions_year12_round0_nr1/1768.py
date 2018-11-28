
#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;

int map[26]={24, 7, 4, 18, 14, 2, 21, 23, 3, 20, 8, 6, 11, 1, 10, 17, 25, 19, 13, 22, 9, 15, 5, 12, 0, 16};

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);

	int t;
	cin>>t;
	getchar();
	char s[105];
	for(int Ci = 1; Ci<=t; Ci++)
	{
		
		cout<<"Case #"<<Ci<<": ";
		gets(s);
		for(int i=0; s[i]!='\0'; i++){
			if(s[i]==' ')
				cout<<' ';
			else
				cout<<char('a'+map[s[i]-'a']);
		}
		cout<<endl;
	}
	return 0;
}