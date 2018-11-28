#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>


using namespace std;

#define rep(i,n) for(i=0;i<(n);i++)
#define foru(i,a,b) for(i=(a);i<=(b);i++)
#define ford(i,a,b) for(i=(a);i>=(b);i--)


int n,m;

//int a[110][110];
int b[1100000];

bool check(int x, int y){
	if (x>y) swap(x,y);
	if (x + b[x] -1 >=y) return false; else
	return true;
}

const int limit =1000000;
void prepare(){
	//memset(a,-1,sizeof(a));
	int i,j,k;
	bool flag;
	b[1]=1;
	foru(i,2,limit){
		j=i + b[i-1];
		if (j>limit) { b[i] = limit - i +1; continue;}
		b[i]=b[i-1];
		while (1){
			flag = false;
			k = j-i;
			while (k>0) {
				if (!check(i,k))
					{flag=true;
						break;
					}
				k-=i;
			}
			if (j>limit || flag) {
				b[i] = (j - 1) - i + 1 ;
				break;
			}
			b[i] = j - i + 1;
			j++;
		}
	}
//	foru(i,1,100) printf("%d ",b[i]);
//	printf("\n");
}

int a1,a2,b1,b2;

int overlap(int a, int b , int c , int d){
	if (b<c || a>d) return 0;
	a = max(a,c);
	b = min(b,d);
	return (b-a+1);
}

int main(){
   freopen("C-small-attempt0.in","r",stdin);
   freopen("output.txt","w",stdout);
   int i,j,k,test,cases;
   scanf("%d",&test);
   cases=0;
   prepare();
   //return 0;
   while (test){
		test--;
		cases++;
		printf("Case #%d: ",cases);
		scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
		long long ans=0,tot;
		
		foru(i,a1,a2)
		  foru(j,b1,b2) if (check(i,j)) ans++;
	   cout<<ans<<endl;
	   
	   /*
		
		tot = (a2-a1+1);
		tot = tot * (b2-b1+1);
		foru(i,a1,a2) {
			printf("%d\n",b[i]);
			ans += overlap( i, i+b[i]-1 , b1,b2);
		//	printf("%d: %d\n",i,overlap(i,i+b[i]-1,b1,b2));
		}
		cout<< tot - ans<<endl;
		*/
	}
   
   return 0;
}
