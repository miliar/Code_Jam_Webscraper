#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>

using namespace std ;

const int Base=100000000;
const int Capacity=200;
typedef long long huge ;

int T , Ncase ;

struct BigInt{
    int Len;
    int Data[Capacity];
    BigInt() : Len(0) {}
    BigInt (const BigInt &V) : Len(V.Len) { memcpy (Data, V.Data, Len*sizeof*Data);}
    BigInt(int V) : Len(0) {for(;V>0;V/=Base) Data[Len++]=V%Base;}
    BigInt &operator=(const BigInt &V) {Len=V.Len; memcpy(Data, V.Data, Len*sizeof*Data); return *this;}
    int &operator[] (int Index) {return Data[Index];}
    int operator[] (int Index) const {return Data[Index];}
};

bool compare(const BigInt &A, const BigInt &B){
     if(A.Len!=B.Len) return A.Len>B.Len ? true:false;
     int i;
     for(i=A.Len-1;i>=0 && A[i]==B[i];i--);
     if(i<0)return false;
     return A[i]>B[i] ? true:false;
}

BigInt operator+(const BigInt &A,const BigInt &B){
    int i,Carry(0);
    BigInt R;
    for(i=0;i<A.Len||i<B.Len||Carry>0;i++){
        if(i<A.Len) Carry+=A[i];
        if(i<B.Len) Carry+=B[i];;
        R[i]=Carry%Base;
        Carry/=Base;
    }
    R.Len=i;
    return R;
}

BigInt operator-(const BigInt &A,const BigInt &B){
    int i,Carry(0);
    BigInt R;
    R.Len=A.Len;
    for(i=0;i<R.Len;i++){
        R[i]=A[i]-Carry;
        if(i<B.Len) R[i]-=B[i];
        if(R[i]<0) Carry=1,R[i]+=Base;
        else Carry=0;
    }
    while(R.Len>0&&R[R.Len-1]==0) R.Len--;
    return R;
}

BigInt operator*(const BigInt &A,const int &B){
    int i;
    huge Carry(0);
    BigInt R;
    for(i=0;i<A.Len||Carry>0;i++){
        if(i<A.Len) Carry+=huge(A[i])*B;
        R[i]=Carry%Base;
        Carry/=Base;
    }
    R.Len=i;
    return R;
}

BigInt operator%(const BigInt &A,const BigInt &B){
    int i,l,r,m,ans;
    BigInt Remain(0);
	if( compare( B , A ) || !compare( B , 0 ) ) return A ;
	for(i=A.Len-1;i>=0;i--){
		Remain=Remain*Base+A[i];
		l=0;r=Base;
		while(l<r)
		{
			m=(l+r)/2;
			if(compare(B*m,Remain))
				  r=m-1;
			else {ans=m;l=m+1;}
		}
		Remain=Remain-B*ans;
	}
	return Remain;
}

istream &operator>>(istream &In,BigInt &V){
    char Ch;
    for(V=0;In>>Ch;){
        V=V*10+(Ch-'0');
        if(In.peek()<=' ') break;
    }
    return In;
}

ostream &operator<<(ostream &Out,const BigInt &V){
    int i;
    Out<<(V.Len==0 ? 0:V[V.Len-1]);
    for(i=V.Len-2;i>=0;i--) for(int j=Base/10;j>0;j/=10) Out<<V[i]/j%10;
    return Out;
}

int X[ 1010 ] ;

int main( )
{
    int x , y , t ;
	//freopen( "input.txt" , "r" , stdin ) ;
	//freopen( "out.txt" , "w" , stdout ) ;
	cin >> Ncase ;
	for( T = 1 ; T <= Ncase ; T ++ )
	{
		int n ;
		cout << "Case #" << T << ": " ;
		cin >> n ;
		for( int i = 0 ; i < n ; i ++ )
			 cin >> X[ i ] ;
		sort( X , X + n ) ;
		x = 0 ;
		for( int i = 1 ; i < n ; i ++ )
		{
			y = X[ i ] - X[ i - 1 ] ;
			while( y )
			{
				t = x % y ;
				x = y ;
				y = t ;
			}
		}
		if( X[ 0 ] % x == 0 ) x = 0 ;
		else x = x - ( X[ 0 ] % x ) ;
		cout << x << endl ;
	}
	return 0 ;
}
