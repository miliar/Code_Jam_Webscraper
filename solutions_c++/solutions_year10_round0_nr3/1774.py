# include <iostream>
using namespace std;

int main()  {
long long g[3][1000], T, r, k, n, x, i, j, amt;
cin>>T;
for (x=1; x<=T; x++)  {
cin>>r>>k>>n;
for (i=0; i<n; i++)   cin>>g[0][i];
for (i=0; i<n; i++)  {
g[1][i]=g[0][i];
for (j=(i+1)%n; (g[1][i]+g[0][j])<=k && j!=i; j=(j+1)%n)   g[1][i]+=g[0][j];
g[2][i]=j;
}
amt=0;  i=0;
while (r--)  {
amt+=g[1][i];
i=g[2][i];
}
cout<<"Case #"<<x<<": "<<amt<<endl;
}
return 0;
}
