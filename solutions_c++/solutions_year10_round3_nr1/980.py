# include <iostream>
using namespace std;

int sign(int a)  {
return ((a>0)?1:-1);
}

int main()  {
long n, a[1000], b[1000], t, i, j, tc, intrsec;
cin>>t;
for (tc=1; tc<=t; tc++)  {
cin>>n;
for (i=0; i<n; i++)   cin>>a[i]>>b[i];
intrsec = 0;
for (i=0; i<n-1; i++)
for (j=i+1; j<n; j++)
if (sign(a[i]-a[j])!=sign(b[i]-b[j]))  intrsec++;
cout<<"Case #"<<tc<<": "<<intrsec<<endl;
}
return 0;
}
