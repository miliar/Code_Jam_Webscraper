#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>

#define ffor(i,n) for(int i=0; i<n; i++)
#define rep(i,n) for(int i=1; i<=n; i++)
#define forit(it,n) for(typeof(n.begin()) it=n.begin(); it!=n.end(); it++)
#define scf(n) scanf("%d", &n);
#define psh push_back
#define mkp make_pair
#define frs first
#define sec second
#define pii pair<int,int>
#define INF 1000000000
#define LL long long
#define LD long double

using namespace std;
const int xam=130;
const int modulo=10000;
int swaps[xam];



int odp(vector<int> &v, int size)
{
    int wyn[25];
    ffor(i,25) wyn[i]=0;
    
    forit(it,v)
    {
	if(*it==1) {wyn[1]+=1; continue;}
	wyn[*it]=(wyn[*it]+wyn[(*it)-1])%modulo;
    }
    
    return wyn[19];
}

void inicjuj()
{
    swaps['w']=1;
    swaps['l']=3;
    swaps['t']=9;
    swaps['d']=14;
    swaps['j']=17;
    swaps['a']=18;
    swaps['e']=INF;
    swaps['c']=INF;
    swaps['o']=INF;
    swaps['m']=INF;
    swaps[' ']=INF;
}

void wczytaj(vector<int> &v)
{
    char ch;
    scanf("%c", &ch);
    while(ch!='\n')
    {
	if(swaps[ch]==0) ;
	else if(swaps[ch]==INF)
	{
	    if(ch=='e') {v.psh(2);v.psh(7);v.psh(15);}
	    else if(ch=='c') {v.psh(4);v.psh(12);}
	    else if(ch=='o') {v.psh(5);v.psh(10);v.psh(13);}
	    else if(ch=='m') {v.psh(6);v.psh(19);}
	    else if(ch==' ') {v.psh(8);v.psh(11);v.psh(16);}
	}
	else v.psh(swaps[ch]);
	if(scanf("%c", &ch)==EOF) break;
    }
}

void wypisz(vector<int> &v)
{
    forit(it,v) printf("%d ", *it); printf("\n");
}
void wypisz(int i, int a)
{
    printf("Case #%d: ", i);
    if(a<1000) printf("0");
    if(a<100) printf("0");
    if(a<10) printf("0");
    printf("%d\n", a);
}

int main()
{
    inicjuj();
    int n;
    scanf("%d%*c", &n);
    
    ffor(i,n)
    {
	vector<int> v;
	wczytaj(v);
// 	wypisz(v);
	wypisz(i+1,odp(v,v.size()));
    }

    return 0;
}