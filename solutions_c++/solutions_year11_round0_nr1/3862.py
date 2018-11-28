#include<iostream>
#include<cstdio>
using namespace std;

#define loop(i,n) for(i=1; i<=n; i++)

int T, N, b, o, t[101], p[101];
char r[101];

int main ()
{
  freopen("A-large.in","r",stdin);
  freopen("output.txt","w",stdout);
  cin >> T; int i, n;
  loop(i, T) {
    cin >> N; t[0]=0; p[0]=1; b=0; o=0; loop(n,N) {
      cin >> r[n] >> p[n];
      if(r[n]=='B') {
	t[n]=t[b]+p[b]-p[n];
	if(t[n]<t[b]+p[n]-p[b]) { t[n]=t[b]+p[n]-p[b]; }
	if(t[n]<t[n-1]) { t[n]=t[n-1]; }
	b=n;
      }
      if(r[n]=='O') {
	t[n]=t[o]+p[o]-p[n];
	if(t[n]<t[o]+p[n]-p[o]) { t[n]=t[o]+p[n]-p[o]; }
	if(t[n]<t[n-1]) { t[n]=t[n-1]; }
	o=n;
      }
      t[n]++;
    }
    cout << "Case #" << i << ": " << t[N] << endl;
  }
  return 0;
}