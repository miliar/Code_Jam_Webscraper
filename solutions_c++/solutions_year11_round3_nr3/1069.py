#include<set>
#include<map>
#include<vector>
#include<string>
#include<algorithm>
#include<iostream>
#include<queue>
using namespace std;

#define MAX(A,B) A>B?A:B
#define MIN(A,B) A>B?B:A



unsigned gcd ( unsigned m , unsigned n ){
	if ( m % n == 0)
		return n;
	return gcd ( n , m % n) ;
}

int Euclid(int a,int b)
{
	if(a % b == 0)
		return b;
	else
		return Euclid(b,a%b);
}
int lcm(int a, int b){
    int c=(a*b)/Euclid(a,b);
    //printf("lcm:%d",c);
    return c;
}
int a[110];

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("outl.txt","w",stdout);
    
	int t;
	int n,l,h;
	cin >> t;
	for(int i=1;i<=t;i++){
		cin >> n >> l >> h;
		for(int j=0;j<n;j++){
			cin >> a[j];
		}
		bool im;
		int tag;
		
		for(int k =l;k<=h;k++){
			im=false;
			for(int j=0;j<n;j++){
				tag = k;
				if((k>a[j])?!(k%a[j]):!(a[j]%k))
					continue;
				else
				{
					im=true;
					break;
				}
			}
			if(im==false){
				break;
			}
		}
		
		if(im==false){
			cout << "Case #" << i << ": " <<  tag << endl;
		}
		else
			cout << "Case #" << i << ": " <<  "NO" << endl;

	}




}

