// Ireyoner
// 92misiu@gmail.com
// Michal Bartecki
// ul. Jana Keplera 4F/15
// 60-158 Poznan
// Poland

#include<iostream>
#include<string>
using namespace std;
char translate[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main(){
    int no;
    string a;
    cin>>no;
    getline(cin,a);
    for( int i=0; i<no; i++){
        getline(cin,a);
        cout<<"Case #"<<i+1<<": ";
        for(int j=0; j<a.size(); j++)
            if(a[j]==' ')
                cout<<' ';
            else
                cout<<translate[(int)a[j]-'a'];
        cout<<endl;
    }
    return 0;
}
