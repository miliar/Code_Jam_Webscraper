#include<stdio.h>
#include<stdlib.h>
#include<string.h>


#define maxlen 1000
struct HP { int len , s [ maxlen ] ; } ;
void PrintHP(HP x ) { for ( int i=x.len ; i >=1; --i) printf("%d",x.s[i]);}
void Str2HP( const char * s ,HP &x )
{
	x.len=strlen ( s ) ;
	for ( int i =1; i<=x.len ; i++) x.s [i]=s [ x.len-i ]-'0' ;
}
void Int2HP( int inte ,HP &x )
{
	if ( inte ==0) { x.len =1; x.s [ 1 ]=0 ; return ; } ;
	for ( x.len=0; inte >0; ){ x.s[++x.len ]= inte %10; inte /=10;};
}
void Multi ( const HP a , const HP b ,HP &c )
{
	int i , j ; c.len=a.len+b.len ;
	for ( i =1; i<=c.len ; i++) c.s[i]=0;
	for ( i =1; i<=a.len ; i++) for ( j =1; j<=b.len ; j++) c.s [ i+j-1]+=a.s[i] * b.s[j] ;
	for ( i =1; i<c.len ; i ++) { c.s [ i+1]+=c.s[i] / 10 ; c.s[i]%=10; }
	while ( c.s[i] ) { c.s[i+1]=c.s[i] / 10; c.s[i]%=10; i ++; }
	while ( i >1 && ! c.s[i] ) i--; c.len=i ;
}
void Plus ( const HP a , const HP b ,HP &c )
{
	int i ; c.s [ 1 ]=0 ;
	for ( i =1; i<=a.len || i<=b.len || c.s[i] ; i ++) {
		if ( i<=a.len ) c.s[i]+=a.s[i] ;
		if ( i<=b.len ) c.s[i]+=b.s[i] ;
		c.s [ i+1]=c.s[i] / 10 ; c.s[i]%=10;
	}
	c.len=i -1; if ( c.len ==0 ) c.len=1;
}
void Subtract ( const HP a , const HP b ,HP &c )
{
	for ( int i =1, j =0; i<=a.len ; i ++) {
		c.s[i]=a.s[i]-j ; if ( i<=b.len ) c.s[i]-=b.s[i] ;
		if ( c.s[i] <0){ j =1 ; c.s[i]+=10; } else j =0;
	}
	c.len=a.len ; while ( c.len >1 && ! c.s[c.len] ) c.len--;
}
int HPCompare( const HP x , const HP y )
{
	if ( x.len>y.len ) return 1 ;
	if ( x.len<y.len ) return -1;
	int i=x.len ;
	while ( ( i >1)&&(x.s[i]==y.s[i] ) ) i--;
	return x.s[i]-y.s[i] ;
}

void Divide ( const HP a , const HP b , HP &c ,HP &d)
{
	int i , j ; d.len =1; d.s [ 1 ]=0 ;
	for ( i=a.len ; i >0; i--) {
		if ( ! ( d.len==1 && d.s [1]==0) )
		{ for ( j=d.len ; j >0; j--) d.s [ j+1]=d.s[j] ; ++d.len ; }
		d.s [1]=a.s[i] ; c.s[i]=0;
		while ( ( j=HPCompare(d , b))>=0 )
		{ Subtract (d , b , d ) ; c.s[i]++; if ( j==0) break ; }
	}
	c.len=a.len ; while ( ( c.len >1)&&(c.s [ c.len ]==0)) c.len --;
}


#define maxn 2010
int r, k , n;
int g[maxn];
int ttt;
int res[maxn];
HP sum[maxn];
HP ans;
int pos[maxn];

void solve(){
	int i,j;
	int tmp;
	int p;
	int tune;
	HP tuneHP;
	HP tmpHP,tmpHP2;
	scanf("%d%d%d", &r, &k ,&n);
	for(i=0;i<n;++i) scanf("%d", g+i);
	int end  =0 ;
	p = 0;
	memset(pos,-1,sizeof(pos));
	while(1){
		tmp  = 0;
		pos[p] = end;
		for(i=0;i<n;++i){
			tmp += g[p];
			if(tmp > k){
				tmp -= g[p];
				break;
			}
			p = (p+1)%n;
		}
		res[end++]=tmp;
//		printf("%d %d %d\n",end, tmp , p);
		if(pos[p] != -1){
			break;
		}
	}
	tune = end- pos[p];
//	printf("end : %d\n",tune);
	Int2HP(res[0], sum[0]);
	for(i=1;i<end;++i){
		Int2HP(res[i], tmpHP);
		Plus(tmpHP, sum[i-1], sum[i]);
	}
	
	if(r<=pos[p]){
		ans = sum[r-1];
	}else{		
		Subtract(sum[end-1] , sum[pos[p]-1],tuneHP);
		
		r-=pos[p];
		tmp = r /tune;
		Int2HP(tmp, tmpHP);
		Multi(tuneHP,tmpHP,ans);
		
		Plus(ans, sum[pos[p]-1], tmpHP);
		ans = tmpHP;
		
		r%=tune;
		if(r){
			tmpHP = ans;
		//	PrintHP(ans);
		//	PrintHP(tmpHP);
			Subtract(sum[pos[p]+r-1],sum[pos[p]-1],tmpHP2);
			Plus(tmpHP,tmpHP2,ans);
		}
	}
	printf("Case #%d: ",++ttt);
	PrintHP(ans);
	printf("\n");
}
int main(){
//	freopen("C-large.in","r",stdin);
//	freopen("C-large.out","w",stdout);
	int t;scanf("%d",&t);
	ttt=0;
	while(--t>=0) solve();
	return 0;
}


/*


4 6 4
1 4 2 1
5 5 10
2 4 2 3 4 2 1 2 1 3


100 10 1
1


*/
