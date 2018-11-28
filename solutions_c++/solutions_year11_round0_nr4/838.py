#include <stdio.h>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <map>
using namespace std;

typedef long long LL;
typedef pair<int,int> PI;
typedef vector<int> VI;
#define ALL(a) (a).begin(),(a).end()
#define PB push_back
#define MP make_pair
#define FT first
#define SD second
#define Y first
#define X second

vector<string>token(string a) {
    vector<string>w;a.push_back(' ');
    while(!a.empty()){w.push_back(a.substr(0,a.find(" ")));a=a.substr(a.find(" ")+1,a.size()-1);}return w;
}

map<string,int> mapik;
vector<string> amapik;
int dodaj(string a) {if(mapik.count(a)==0) {mapik[a]=mapik.size()-1;amapik.PB(a);}return mapik[a];}

#define INF 1000000000

char tmp_str[1000];
string scanf_string() {
	scanf("%s",tmp_str);
	return tmp_str;
}

const int N = 1000;
int n;

int kupa(int n);

int silnia(int n) {
	int res = 1;
	for(int i=1;i<=n;i++) {
		res *= i;
	}
	return res;
}

int npok(int n, int k) {
	return silnia(n)/silnia(k)/silnia(n-k);
}

/*int kupa2(int n) {
	if(n==0) return 1;
	if(n==1) return 0;
	else if(n==2) return 1;
	return kupa(n-1)*(n-1)+kupa(n-2)*(n-2);
}*/

double prawd(int n, int ok) {
	int k = n-ok;
	return (double)(npok(n,ok)*kupa(k))/silnia(n);

}

double oczekiwana(int n) {
	double res = 1;
	if(n<=1) return 0;
	for(int i=1;i<=n;i++) {
		res += (oczekiwana(n-i))*prawd(n,i);
		printf("n=%d i=%d -> %lf ",n,i,prawd(n,i)); 
	}
	printf("%lf , prawd(n,0)=%lf ,",res,prawd(n,0));
	res *= (1/(1.0-prawd(n,0)));
	return res;
}

//(2*n)!/(n+1)!.  
int kupa(int n) {
	vector<int> w;
	for(int i=0;i<n;i++) w.PB(i);
	int res = 0;
	do{
		int ok=1;
		for(int i=0;i<n;i++) if(w[i]==i) {ok=0;break;}
		res+=ok;
	} while(next_permutation(ALL(w)));
	//return silnia(2*n)/(silnia(n+1));
	return res;
}
	
int main() {
	int d;scanf("%d",&d);
	for(int ind=1;ind<=d;ind++) {
		scanf("%d",&n);
		/*double suma = 0;
		for(int i=0;i<=n;i++) {
			printf("%lf \n", prawd(n,i));
			printf(" = kupa(%d) = %d ",i,kupa(i));
			printf(" = kupa2(%d) = %d ",i,kupa2(i));
			
			
			suma+=prawd(n,i); 
		}
		printf("{%lf}\n",oczekiwana(n));
		printf("[%lf]\n",suma); 
		*/
		int ok=0;
		for(int i=1;i<=n;i++) {
			int tmp;scanf("%d",&tmp);
			if(tmp==i) ok++;
		}
		double res = 0;
		double poz = n-ok;
		/*if(poz%2==1) {poz-=3;res+=3.25;}
		res += 2*poz/2;*/
		printf("Case #%d: ",ind);
		printf("%lf\n",poz);
	}
	return 0;
}
