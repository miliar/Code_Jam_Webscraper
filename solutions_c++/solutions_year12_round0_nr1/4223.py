#include <iostream>
#include <string>

using namespace std;

char conv[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main(void){
	int n;
	string tmp;
	cin >> n;
	cin.ignore();
	for (int k=0;k<n;++k){
		getline(cin,tmp);
		for (int i=0;i<tmp.size();++i)
			if (tmp[i]!=' ')
				tmp[i]=conv[ tmp[i]-97 ];
		
		cout << "Case #"<<k+1<<": "<< tmp<<endl;
	}
	return 0;

}