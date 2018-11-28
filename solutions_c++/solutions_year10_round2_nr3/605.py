#include <iostream>
#include <string>
#include <memory>
using namespace std;
int f[500][500];
/*int C(int n , int k ) {
    if (k==0) return 1;
	if (k>n)  return 0;
	if (k==n) return 1;
    int q[500];
    for (int i = 0 ; i< k; i++) q[i]= n-i;
    for (int i = k; i>1; i--) {
        int j  = 0;
        while (q[j]%i!=0) j++;
        q[j]/=i;
    }
    int tm = 1;
    for (int i = 0 ; i<k; i++) tm = tm *q[i] % 100003;
    return tm;
}
*/
int C(int n , int k ) {
    if (k ==0) return 1;
    if (k>n) return 0;
    if (k == n) return 1;
    long long ans = 1;
    for (int i = 0 ; i <k; i++)
      ans = ans *(n-i)/(i+1);
    return (int) ans ;
}
int main()
{
    int nn ; cin >> nn ; for (int n0=1; n0<=nn; n0++) {
    int q;
    cin >>q;
    memset(f,0,sizeof(f));
    for (int i =2 ; i<=q; i++) f[i][1]=1;
    for (int i =3; i<=q; i++)
    for (int k =2; k<i; k++) 
    for (int j = 1; j<k;j++)
       f[i][k]=(f[i][k]+f[k][j]*C(i-k-1,k-j-1)) %100003;
    int ans = 0 ;
    for (int j = 1; j<q; j++)
      ans = (ans + f[q][j]) %100003;
    cout <<"Case #"<<n0<<": "<<ans<<endl;
    }
}
