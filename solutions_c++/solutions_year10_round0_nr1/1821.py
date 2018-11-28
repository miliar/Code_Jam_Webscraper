# include <iostream>
using namespace std;

int main()  {
long T, n, k, v, x;
cin>>T;
for (x=1; x<=T; x++)  {
cin>>n>>k;
v=1<<n;
k%=v;
cout<<"Case #"<<x<<": ";
if (k==(v-1))  cout<<"ON"<<endl;
else  cout<<"OFF"<<endl;
}
return 0;
}
