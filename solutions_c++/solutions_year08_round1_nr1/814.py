#include <iostream>
#include <fstream>

using namespace std;
bool comp (int a, int b){
return a>b;
}
ifstream in("A-small.in");
ofstream out("A-small.out");
int main(){
int t, n, i;
in>>t;
int a1[900], a2[900];
long long int res=0;
int k=t;
while (t>0){
res=0;
in>>n;
for (i=0; i<n; i++)in>>a1[i];
for (i=0; i<n; i++)in>>a2[i];
sort (a1, a1+n);
sort (a2, a2+n, comp);
for (i=0; i<n;i++)res+=a1[i]*a2[i];
out<<"Case #"<<k-t+1<<": ";
out<<res<<endl;
t--;
}

return 0;
}
