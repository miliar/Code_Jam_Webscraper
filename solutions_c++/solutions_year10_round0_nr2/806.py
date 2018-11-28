#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

#include<iostream>
#include<deque>
using namespace std;
 
class Integer_10{
private:
	deque<int>num;
	inline void Resize(const int n);
 
public:
	Integer_10();
	Integer_10(int);
	Integer_10(const int&,const int&);
	Integer_10(const Integer_10&);
	Integer_10(const string &s);

	inline const int  Comp(const Integer_10& a,const Integer_10& b)const;
	inline const Integer_10 operator<<(const int& n)const;
	inline const Integer_10 operator>>(const int& n)const;
	inline const int        operator[](const int keta)const;
	inline const Integer_10 operator+(const Integer_10& aOther)const;
	inline const Integer_10 operator-(const Integer_10& aOther)const;
	inline const Integer_10 operator*(const Integer_10& aOther)const;
	inline const Integer_10 operator/(const Integer_10& aOther)const;
	inline const Integer_10 operator%(const Integer_10& aOther)const;
 
	inline const Integer_10& operator++();
	inline const Integer_10& operator--();
	inline const Integer_10& operator+=(const Integer_10& aOther);
	inline const Integer_10& operator-=(const Integer_10& aOther);
	inline const Integer_10& operator*=(const Integer_10& aOther);
	inline const Integer_10& operator/=(const Integer_10& aOther);
	inline const Integer_10& operator%=(const Integer_10& aOther);
 
	inline const bool operator>(const Integer_10& aOther)const;
	inline const bool operator<(const Integer_10& aOther)const;
	inline const bool operator>=(const Integer_10& aOther)const;
	inline const bool operator<=(const Integer_10& aOther)const;
	inline const bool operator==(const Integer_10& aOther)const;
	inline const bool operator!=(const Integer_10& aOther)const;
 
	inline const int GetKeta()const;
	inline void Output()const;
};
 
//-----------------------------------------------------------------------------
//コンストラクタ 
Integer_10::Integer_10(){
}
 
//-----------------------------------------------------------------------------
//コンストラクタ 
Integer_10::Integer_10(const int& keta_size,const int& mode){
	num.resize(keta_size);
}
 
//-----------------------------------------------------------------------------
//コンストラクタ 
Integer_10::Integer_10(int i_num){
	if(i_num){
		for(;i_num>0;){
			num.push_back(i_num%10);
			i_num /= 10;
		}
	}else{
		num.push_back(0);
	}
}
 
//-----------------------------------------------------------------------------
//コンストラクタ 
Integer_10::Integer_10(const string &s){
	num.clear();
	num.resize(s.length());
	for( int i=s.length()-1;i>=0;i-- ){
		num.at( s.length()-i-1 ) = s[i]-'0';
	}
}
 
//-----------------------------------------------------------------------------
//コンストラクタ 
Integer_10::Integer_10(const Integer_10& aOther){
	num = aOther.num;
}
 
 
//-----------------------------------------------------------------------------
//もし容量が足りていないのなら、n桁まで要素を確保し、0で初期化する 
//ここでの桁数とは、clear()された状態を０桁 １つ要素が定義された状態で１となる
void Integer_10::Resize(const int n){
	const int limit = n - this->num.size();
	if(limit > 0){
		num.resize(n,0);
	}
}
 
//-----------------------------------------------------------------------------
//指定した桁の状態を返す
const int Integer_10::operator[](const int e)const{
	return this->num.at(e);
}
 
//-----------------------------------------------------------------------------
//ビットシフト １０倍
const Integer_10 Integer_10::operator<<(const int& n)const{
	Integer_10 result = (*this);
	for(int i=0;i<n;i++)result.num.push_front(0);
	return result;
}
 
//-----------------------------------------------------------------------------
//ビットシフト １／１０倍
const Integer_10 Integer_10::operator>>(const int& n)const{
	Integer_10 result = (*this);
	for(int i=0;i<n;i++)result.num.pop_front();
	return result;
}
 
//-----------------------------------------------------------------------------
//加算
const Integer_10 Integer_10::operator+(const Integer_10& aOther)const{
	const int limit = (*this)<aOther ? aOther.GetKeta() : this->GetKeta();
	Integer_10 a = (*this);
	Integer_10 b = aOther;
	Integer_10 result( limit+1,0 ); //桁数＋１だけ要素を確保
	a.Resize( limit );
	b.Resize( limit );
 
	int kuriage = 0;
	for( int i=0;i<limit;i++ ){
		result.num[i] = a[i]+b[i]+kuriage;
		kuriage = result[i]/10;
		result.num[i] %= 10;
	}
	result.num[limit] = kuriage;
	return result;
}
 
//-----------------------------------------------------------------------------
//減算
const Integer_10 Integer_10::operator-(const Integer_10& aOther)const{
	if( aOther>(*this) ){
		puts("Integer_10 Operator - Error\n");
		exit(0);
	}
	const int limit = this->GetKeta();
	Integer_10 a = (*this);
	Integer_10 b = aOther;
	Integer_10 result( limit+1,0 ); //桁数＋１だけ要素を確保
	b.Resize( limit );
 
	int kurisage = 0;
	for( int i=0;i<limit;i++ ){
		result.num[i] = a[i]-b[i]-kurisage;
		kurisage = result.num[i] < 0 ? 1:0;
		while( result[i] < 0 ){
			result.num[i] += 10;
		}
	}
	return result;
}
 
//-----------------------------------------------------------------------------
//掛け算
const Integer_10 Integer_10::operator*(const Integer_10& aOther)const{
	const int limit = aOther.GetKeta() + this->GetKeta();
	Integer_10 result( limit,0 );
 
	for( int i=0;i<aOther.GetKeta();i++ ){
		for(int j=0;j<aOther[i];j++){
			result += (*this << i);
		}
	}
	return result;
}
 
//-----------------------------------------------------------------------------
//除算
const Integer_10 Integer_10::operator/(const Integer_10& aOther)const{
	Integer_10 a = (*this);
	Integer_10 result(a.GetKeta(),0);
 
	for(;aOther<=a;){
		Integer_10 tmp = aOther;
		int diff_keta = a.GetKeta() - aOther.GetKeta();
		tmp = tmp << diff_keta;
		if( tmp > a ){
			tmp = tmp >> 1;
			diff_keta --;
		}
 
		if(diff_keta >= 0){
			for(;a >= tmp;){
				result.num[diff_keta] ++;
				a -= tmp;
			}
		}
	}
	return result;
}
 
//-----------------------------------------------------------------------------
//剰余
const Integer_10 Integer_10::operator%(const Integer_10& aOther)const{
	Integer_10 a = (*this);
 
	for(;aOther<=a;){
		Integer_10 tmp = aOther;
		int diff_keta = a.GetKeta() - aOther.GetKeta();
		tmp = tmp << diff_keta;
		if( tmp > a ){
			tmp = tmp >> 1;
			diff_keta --;
		}
		if(diff_keta >= 0){
			for(;a >= tmp;){
				a -= tmp;
			}
		}
	}
	return a;
}
 
//代入演算子のオーバーロード
const Integer_10& Integer_10::operator++(){
	*this = (*this) + Integer_10(1);
	return *this;
}
const Integer_10& Integer_10::operator--(){
	*this = (*this) - Integer_10(1);
	return *this;
}
const Integer_10& Integer_10::operator+=(const Integer_10& aOther){
	*this = (*this) + aOther;
	return *this;
}
const Integer_10& Integer_10::operator-=(const Integer_10& aOther){
	*this = (*this) - aOther;
	return *this;
}
const Integer_10& Integer_10::operator*=(const Integer_10& aOther){
	*this = (*this) * aOther;
	return *this;
}
const Integer_10& Integer_10::operator/=(const Integer_10& aOther){
	*this = (*this) / aOther;
	return *this;
}
const Integer_10& Integer_10::operator%=(const Integer_10& aOther){
	*this = (*this) % aOther;
	return *this;
}
 
//-----------------------------------------------------------------------------
//比較演算子のオーバーロード
const bool Integer_10::operator>(const Integer_10& aOther)const{
	return ( Comp( Integer_10(*this),aOther ) == 1 );
}
const bool Integer_10::operator<(const Integer_10& aOther)const{
	return ( Comp( Integer_10(*this),aOther ) == -1 );
}
const bool Integer_10::operator>=(const Integer_10& aOther)const{
	return ( Comp( Integer_10(*this),aOther ) >= 0 );
}
const bool Integer_10::operator<=(const Integer_10& aOther)const{
	return ( Comp( Integer_10(*this),aOther ) <= 0 );
}
const bool Integer_10::operator==(const Integer_10& aOther)const{
	return ( Comp( Integer_10(*this),aOther ) == 0 );
}
const bool Integer_10::operator!=(const Integer_10& aOther)const{
	return ( Comp( Integer_10(*this),aOther ) != 0 );
}
 
 
 
//-----------------------------------------------------------------------------
//桁数を得る
const int Integer_10::GetKeta()const{
	int tmp_size = this->num.end() - this->num.begin();
	for(int i=tmp_size-1;i>=0;i--){
		if( num[i] )return i+1;
	}
	return 1;
}
 
 
//-----------------------------------------------------------------------------
//数字を出力する
void Integer_10::Output() const{
	bool flag=true;
	for(int i=GetKeta()-1;i>=0;i--){
		if(this->num[i]){
			flag = false;
		}
		if(flag && num[i]==0 )continue;
		printf("%d",this->num[i]);
	}
	if( flag ){
		cout << "0";
	}
}
 
//-----------------------------------------------------------------------------
//比較関数
const int Integer_10::Comp(const Integer_10& a,const Integer_10& b)const{
	const int a_size = a.GetKeta();
	const int b_size = b.GetKeta();
 
	if(a_size > b_size){
		return 1;
	}else if(a_size < b_size){
		return -1;
	}else{
		for(int i=a_size-1;i>=0;i--){
			if( a[i]!=b[i] ){
				return a[i]>b[i]? 1: -1;
			}
		}
	}
	return 0;
}





Integer_10 gcd(Integer_10 a,Integer_10 b){
	return a%b!=Integer_10(0)?gcd(b,a%b):b;
}





int main(){
	int C,N;
	char ch[64];
	string str;
	
	Integer_10 ans,tmp;
	cin >> C;
	
	vector<Integer_10>v;
	
	
	
	for(int i=0;i<C;i++){
		v.clear();
		
		cin >> N;
		for(int j=0;j<N;j++){
			scanf(" %s ",ch);
			str = string(ch);
			v.push_back(Integer_10(str));
		}
		
		Integer_10 T(0);
		
		
		for(int j=0;j<v.size();j++){
			for(int k=j+1;k<v.size();k++){
				
				if(v[k] >= v[j]){
					tmp = v[k]-v[j];
				}else{
					tmp = v[j]-v[k];
				}
				
				if(T == Integer_10(0)){
					T = tmp;
				}
				if(tmp != Integer_10(0)){
					T = gcd(T,tmp);
				}
			}
		}
		//cout << "T=";T.Output();cout << endl;
		
		if(v[0]%T != Integer_10(0)){
			ans = T - (v[0]%T);
		}else{
			ans = 0;
		}
		
		
		printf("Case #%d: ",i+1);ans.Output();cout << endl;
	}
	return 0;
}
