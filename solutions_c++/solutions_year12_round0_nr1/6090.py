#include <iostream>
#include<cmath>
#include<cstdlib>
#include<string>
using namespace std;
int t;
string g; string al = "yhesocvxduiglbkrztnwjpfmaq";
char an[101];
int main(){
    freopen("A-small-attempt1.in","r", stdin);
    freopen("data.txt","w",stdout);
	cin>> t;
	for(int j = 1; j <= t; j++){
            char tm;
		cin>>tm; gets(an); g = an;
		cout<< "Case #"<< j<< ": ";
		
		cout<<al[int(tm)-int('a')];
		for(int i = 0; i < g.size(); i++){
			if(g[i] == ' ') cout<<" ";
			else cout<<al[int(g[i])-int('a')];
		}
		cout<<endl;
	}
	//system("pause");
	return 0;
}
