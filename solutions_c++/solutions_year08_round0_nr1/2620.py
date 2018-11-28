#include <iostream>
#include <fstream>
#include <set>
using namespace std;

int main(){
ifstream in("A-large.in");
ofstream out("A-large.out");
int n, s, q, a=0, i;
string pal, ig;
in>>n;
//out<<n<<endl;
set <string> t;
while(a<n){
t.clear();
a++;
int cont=0;
in>>s; getline(in,ig);
//out<<s<<' '<<ig<<endl;
//out<<s;
for (i=0; i<s; i++)getline(in,pal);
in>>q;getline(in,ig);//out<<q<<' '<<ig<<endl;
//out<<q<<endl;
for (i=0; i<q; i++){
getline(in, pal);
//out<<pal<<endl;
t.insert(pal);
if (t.size()==s){
cont++;
//out<<i<<' '<<pal<<endl;
t.clear();
t.insert(pal);
}
//else cont--;
}
out<<"Case #"<<a<<": "<<cont<<endl;
}
return 0;
}
