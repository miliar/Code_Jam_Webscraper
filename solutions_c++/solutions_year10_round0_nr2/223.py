#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <math.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int,int> ii;
typedef vector<ii> vii;
#define sz(a) int((a).size())
#define all(c) (c).begin(),(c).end()
#define loop(i,n) for(int i=0; i<(n); i++)
#define tr(it,c) for(it=(c).begin(); it!=(c).end(); it++)
#define tr2(it1,c,it2,d) for(it1=(c).begin(),it2=(d).begin(); it1!=(c).end(); it1++,it2++)

class LargeNumber
{
private:
	static const int N = 10;
	static const int over = 100000000;
	int data[N];
	const int binarydivide(const LargeNumber& A);
public:
	LargeNumber(int A);
	LargeNumber(const LargeNumber& A);
	LargeNumber(const char* str);
	bool operator<(const LargeNumber& A)const;
	bool operator>(const LargeNumber& A)const;
	bool operator==(const LargeNumber& A)const;
	bool LargeNumber::operator==(const int A)const;
	const LargeNumber operator+(const LargeNumber& A)const;
	const LargeNumber& operator+=(const LargeNumber& A);
	const LargeNumber& operator+=(const int A);
	const LargeNumber operator-(const LargeNumber& A)const;
	const LargeNumber& operator-=(const LargeNumber& A);
	const LargeNumber operator*(const int A)const;
	const LargeNumber& operator*=(const int A);
	const LargeNumber operator/(const LargeNumber& A)const;
	const LargeNumber operator%(const LargeNumber& A)const;
	void print()const;
	const string sprint()const;
	friend ostream& operator<<(ostream& out, const LargeNumber& A);
};

LargeNumber::LargeNumber(int A=0)
{memset(data, 0, sizeof(data));data[1]=A/over; data[0]=A%over;}

LargeNumber::LargeNumber(const LargeNumber& A)
{memset(data, 0, sizeof(data));loop(i, N)data[i]=A.data[i];}

LargeNumber::LargeNumber(const char* str)
{
	memset(data, 0, sizeof(data));
	int len = strlen(str);
	for(int i=0; i<len; i+=8)
	{
		int curnum = 0;
		for(int j=i+8; j>i; j--)
		{
			int pos = len-j;
			if(pos>=0)
			{
				int num = str[pos]-'0';
				curnum *= 10;
				curnum += num;
			}
		}
		data[i/8] = curnum;
	}
}

bool LargeNumber::operator<(const LargeNumber& A)const
{
	for(int i=N-1; i>=0; i--)
	{
		if(data[i]<A.data[i])return true;
		else if(data[i]>A.data[i])return false;
	}
	return false;
}

bool LargeNumber::operator>(const LargeNumber& A)const
{
	for(int i=N-1; i>=0; i--)
	{
		if(data[i]>A.data[i])return true;
		else if(data[i]<A.data[i])return false;
	}
	return false;
}

bool LargeNumber::operator==(const LargeNumber& A)const
{
	loop(i, N)
		if(data[i]!=A.data[i])return false;
	return true;
}

bool LargeNumber::operator==(const int A)const
{
	int remain = A % over;
	int in = A/over;
	for(int i=2; i<N; i++)
		if(data[i])return false;
	return (data[0]==remain && data[1]==in);
}

const LargeNumber LargeNumber::operator+(const LargeNumber& A)const
{
	LargeNumber R;
	int in = 0;
	loop(i, N)
	{
		R.data[i] = data[i]+A.data[i]+in;
		if(R.data[i] >= over)
		{
			R.data[i] -= over;
			in = 1;
		}
		else
			in = 0;
	}
	return R;
}

const LargeNumber& LargeNumber::operator+=(const LargeNumber& A)
{
	int in = 0;
	loop(i, N)
	{
		data[i] += A.data[i]+in;
		if(data[i] >= over)
		{
			data[i] -= over;
			in = 1;
		}
		else
			in = 0;
	}
	return *this;
}

const LargeNumber& LargeNumber::operator+=(const int A)
{
	int i=0;
	data[0] += A;
	while(data[i] >= over)
	{
		data[i] -= over;
		i++;
	}
	return *this;
}

const LargeNumber LargeNumber::operator-(const LargeNumber& A)const
{
	LargeNumber R;
	int bo = 0;
	loop(i, N)
	{
		R.data[i] = data[i]-A.data[i]-bo;
		if(R.data[i] < 0)
		{
			R.data[i] += over;
			bo = 1;
		}
		else
			bo = 0;
	}
	return R;
}

const LargeNumber& LargeNumber::operator-=(const LargeNumber& A)
{
	int bo = 0;
	loop(i, N)
	{
		data[i] = data[i]-A.data[i]-bo;
		if(data[i] < 0)
		{
			data[i] += over;
			bo = 1;
		}
		else
			bo = 0;
	}
	return *this;
}

const LargeNumber LargeNumber::operator*(const int A)const
{
	LargeNumber R;
	int in = 0;
	loop(i, N)
	{
		ll product = (ll)data[i]*A+in;
		R.data[i] = (int)(product%over);
		in = (int)(product/over);
	}
	return R;
}

const LargeNumber& LargeNumber::operator*=(const int A)
{
	int in = 0;
	loop(i, N)
	{
		ll product = (ll)data[i]*A+in;
		data[i] = (int)(product%over);
		in = (int)(product/over);
	}
	return *this;
}

const LargeNumber LargeNumber::operator/(const LargeNumber& A)const
{
	LargeNumber R(0), remain(0);
	for(int i=N-1; i>=0; i--)
	{
		remain *= over;
		remain += data[i];
		int div = remain.binarydivide(A);
		R *= over;
		R += div;
	}
	return R;
}

const LargeNumber LargeNumber::operator%(const LargeNumber& A)const
{
	LargeNumber R(0), remain(0);
	for(int i=N-1; i>=0; i--)
	{
		remain *= over;
		remain += data[i];
		int div = remain.binarydivide(A);
		R *= over;
		R += div;
	}
	return remain;
}

void LargeNumber::print()const
{
	int i;
	for(i=N-1; data[i]==0&&i>0; i--);
	printf("%d", data[i--]);
	for(; i>=0; i--)
		printf("%08d", data[i]);
}

const string LargeNumber::sprint()const
{
	char str[10];
	int i;
	for(i=N-1; data[i]==0&&i>0; i--);
	sprintf(str, "%d", data[i--]);
	string result = str;
	for(; i>=0; i--)
	{
		sprintf(str, "%08d", data[i]);
		result += str;
	}
	return result;
}

ostream& operator<<(ostream& out, const LargeNumber& A)
{
	A.print();
	return out;
}

const int LargeNumber::binarydivide(const LargeNumber& A)
{
	int low=0, high=over;
	LargeNumber P;
	while(high > low+1)
	{
		int mid = (high+low)/2;
		P = A*mid;
		if(operator<(P))
			high = mid;
		else if(operator>(P))
			low = mid;
		else
		{
			*this = 0;
			return mid;
		}
	}
	operator-=(A*low);
	return low;
}

template <class T>
T GreatestCommonDivisor(T a, T b)
{
	T c;
	if(a<b){c = a;a = b;b = c;}
	while(1)
	{
		c = a%b;
		if(c==0)
			break;
		a = b;
		b = c;
	}
	return b;
}

template <class T>
T GreatestCommonDivisor(const vector<T>& A)
{
	int n = sz(A);
	if(n == 0)
		return 0;
	else if(n == 1)
		return A[0];
	T gcd = A[0];
	for(int i=1; i<n; i++)
		gcd = GreatestCommonDivisor<T>(gcd, A[i]);
	return gcd;
}

string solve(const vs& time)
{
	int N = sz(time);
	vector<LargeNumber> difftime(N-1);
	LargeNumber first = time[0].c_str();
	LargeNumber next;
	for(int i=0; i<N-1; i++)
	{
		next = time[i+1].c_str();
		difftime[i] = (next>first) ? next-first : first-next;
	}
	LargeNumber gcd = GreatestCommonDivisor<LargeNumber>(difftime);
	LargeNumber n = first%gcd;
	if(n>0)
		n = gcd - n;
	return n.sprint();
}

void preprocess(){}

void readinput(vs& time)
{
	int N;
	cin>>N;
	time.resize(N);
	loop(i, N)
		cin>>time[i];
}

vs getoutput()
{
	vs time;
	readinput(time);
	string answer = solve(time);
	return vs(1, answer);
}

void main()
{
	FILE *p, *q;
//	p=freopen("in.txt", "r", stdin); q=freopen("out.txt", "w", stdout);
//	p=freopen("test\\B-small-attempt0.in", "r", stdin);q=freopen("test\\B-small-attempt0.out", "w", stdout);
	p=freopen("test\\B-large.in", "r", stdin);q=freopen("test\\B-large.out", "w", stdout);
	int testcase;
	cin>>testcase;
	preprocess();
	for (int i=1; i<=testcase; i++)
	{
		cout<<"Case #"<<i<<": ";
		vs answer = getoutput();
		loop(j, sz(answer))
			cout<<answer[j]<<endl;
		fflush(stdout);
	}
	fclose(p);
	fclose(q);
}