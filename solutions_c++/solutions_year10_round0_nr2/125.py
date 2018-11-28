#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

//typedef int Bigint;
struct Bigint
{
	vector<int> data;
	
	Bigint() { data = vector<int>(1); }
	Bigint(vector<int> vi){
		data = vi;
	}
	Bigint(string str){
		for(int i = 0; i < str.length(); i++)
		{
			data.push_back(str[i] - '0');
		}
		reverse(data.begin(), data.end());
	}
	Bigint(int i){
		do
		{
			data.push_back(i % 10);
		}
		while(i/=10);
	}
	
	friend Bigint operator+(const Bigint& a, const Bigint& b){
		vector<int> A = a.data, B = b.data;
		vector<int> C(max(A.size(), B.size()));
		for(int i = 0; i < C.size(); i++)
		{
			if(i < A.size())
				C[i] += A[i];
			if(i < B.size())
				C[i] += B[i];
		}
		Bigint c(C);
		c.form();
		return c;
	}
	friend Bigint operator-(const Bigint& a, const Bigint& b){
		vector<int> A = a.data, B = b.data;
		vector<int> C(max(A.size(), B.size()));
		for(int i = 0; i < C.size(); i++)
		{
			if(i < A.size())
				C[i] += A[i];
			if(i < B.size())
				C[i] -= B[i];
		}
		Bigint c(C);
		c.form();
		return c;
	}
	friend Bigint operator*(const Bigint& a, const Bigint& b){
		vector<int> A = a.data, B = b.data;
		vector<int> C(A.size() + B.size());
		
		for(int i = 0; i < A.size(); i++)
			for(int j = 0; j < B.size(); j++)
				C[i+j] += A[i] * B[j];
		Bigint c(C);
		c.form();
		return c;
	}
	friend Bigint operator%(const Bigint& a, const Bigint& b){
		Bigint A = 0, B = b;
		for(int i = a.data.size() - 1; i >= 0; i--)
		{
			A = A * 10 + a.data[i];
			while(A >= B)
				A = A - B;
		}
		return A;
	}
	friend bool operator<(const Bigint& a, const Bigint& b){
		if(a.data.size() != b.data.size())
			return a.data.size() < b.data.size();
		for(int i = a.data.size()-1; i >= 0; i--)
			if(a.data[i] != b.data[i])
				return a.data[i] < b.data[i];
	}
	friend bool operator<=(const Bigint& a, const Bigint& b){
		return !(a > b);
	}
	friend bool operator>(const Bigint& a, const Bigint& b){
		if(a.data.size() != b.data.size())
			return a.data.size() > b.data.size();
		for(int i = a.data.size()-1; i >= 0; i--)
			if(a.data[i] != b.data[i])
				return a.data[i] > b.data[i];
		return false;
	}
	friend bool operator==(const Bigint& a, const Bigint& b){
		if(a.data.size() != b.data.size())
			return false;
		for(int i = a.data.size()-1; i >= 0; i--)
			if(a.data[i] != b.data[i])
				return false;
		return true;
	}
	friend bool operator>=(const Bigint& a, const Bigint& b){
		return !(a < b);
	}
	
	friend istream& operator>>(istream& is, Bigint& i){
		string str;
		is >> str;
		i = Bigint(str);
		return is;
	}
	friend ostream& operator<<(ostream& os, Bigint i){
		for(int k = i.data.size() - 1; k >= 0; k--)
			os << i.data[k];
		return os;
	}
	
	void form(){
		for(int i = 0; i < data.size(); i++)
		{
			if(i == data.size() - 1)
			{
				if(data[i] > 9)
				{
					data.push_back(data[i] / 10);
					data[i] %= 10;
				}
			}
			else
			{
				if(data[i] < 0)
				{
					data[i+1] -= (-data[i] - 1) / 10 + 1;
					data[i] += ((-data[i] - 1) / 10 + 1) * 10;
				}
				else
				{
					data[i+1] += data[i] / 10;
					data[i] %= 10;
				}
			}
		}
		for(int i = data.size()-1; i > 0; i--)
		{
			if(data[i] == 0)
				data.erase(data.begin() + i);
			else
				break;
		}
	}
};


Bigint gcd(Bigint x, Bigint y){
	return y == 0 ? x : (x % y == 0 ? y : gcd(y, x % y));
}


int main()
{
	int C;
	cin >> C;
	for(int no = 1; no <= C; no++)
	{
		int N;
		cin >> N;
		vector<Bigint> lst(N);
		for(int i = 0; i < N; i++)
			cin >> lst[i];
		
		sort(lst.begin(), lst.end());
		
		Bigint _gcd = 0;
		for(int i = 1; i < lst.size(); i++)
			_gcd = gcd(_gcd, lst[i] - lst[i-1]);
		
		Bigint ans = (_gcd - (lst[0] % _gcd)) % _gcd;
		cout << "Case #" << no << ": " << ans << endl;
	}
	return 0;
}
