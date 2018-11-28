#include <iostream>
#include <string>
#include <conio.h>
using namespace std;
void main(){
	string fname = "A-small-attempt1";
	freopen((fname+".in").c_str(), "r", stdin);
	freopen((fname+".out").c_str(), "w", stdout);

	int n; cin>>n; cin.ignore(1);
	string tmp;
	char google[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	for (int i=1; i<=n; i++){
		getline(cin,tmp);
		cout<<"Case #"<<i<<": ";
		for (int j=0;j<=tmp.length()-1;j++)
			if (tmp[j]!=' ') cout<<google[int(tmp[j])-97]; else
				cout<<" ";
		cout<<"\n";
	}
}