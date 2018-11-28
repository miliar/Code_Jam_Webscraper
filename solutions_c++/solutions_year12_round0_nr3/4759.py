#include <iostream>
#include <string>
#include <sstream>
#include <cstdio>

using namespace std;

bool misma_len(int a, int b, string &salidaa, string &salidab) {
    stringstream sa, sb;
    sa<<a; sb<<b;
    salidaa = sa.str();
    salidab = sb.str();
    return (salidaa.length() == salidab.length());
}

bool es_reciclado(string a, string b) {
    string s = a + a;
    //cout<<"es reciclado "<<s<<" y "<<b<<endl;
    if (s.find(b) != string::npos)
	return true;
    else return false;
}
    
void reciclar(int a, int b, int caso) {
    int count = 0;
    for (int n=a; n<b; ++n){
	int m = n+1;
	string sa, sb;
	//cerr<<"m: "<<m<<endl;
	while (m <= b && misma_len(n, m, sa, sb)){
	    if (es_reciclado(sa, sb))
		count++;
	    m++;
	}
    }
    cout<<"Case #"<<caso<<": "<<count<<endl;
}

int main(){
    int t, a, b;
    scanf("%d\n", &t);
    for (int i=0; i<t; ++i){
	scanf("%d %d\n", &a, &b);
	//cerr<<"t: "<<t<<" a: "<<a<<" b: "<<b<<endl;
	reciclar(a, b, i+1);
    }
    return 0;
}
