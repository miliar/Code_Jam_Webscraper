#include <fstream>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <algorithm>
#include <functional>
#include <queue>
#include <stack>
#include <ctime>
#include <cmath>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <bitset>
#include <cassert>
#include <stack>
#include <limits>

using namespace std;

//���뿪��
#define RDBUF 0x03
//#define RDBUF 0x01 //����ض���
//#define RDBUF 0x01 //�����ض���
//#define RDBUF 0x03 //��������ض���

//����
const double PI = acos(-1.0);
const double EPS = 1e-11;

//����
#define pause system("pause");
#define SET0(x) memset(x, 0, sizeof(x))

clock_t __time;
#define RETTIME __time = clock();
#define TIMEOUT cout<<clock()-__time<<endl;



template<class T> T gcd(const T &a, const T &b) {return (b == 0) ? a : gcd ( b, a%b);}
template<class T> T lcm(const T &a, const T &b) {return a*(b/gcd(a,b));}
int toInt(string s) { istringstream sin(s); int t; sin>>t; return t;}

typedef long long int64;
typedef unsigned long long uint64;
int64 toInt64(string s) { istringstream sin(s); int64 t; sin>>t; return t;}
string toString(int v ){ ostringstream sout; sout<<v; return sout.str();}
string toString(int64 v){ ostringstream sout; sout<<v; return sout.str();}

using namespace std;


int64 Next(int64 nin)
{
	string str = toString(nin);

	int ln = str.length();

	int t = 0;

	for(int i = ln - 1; i!=0; --i)
	{
		if(str[i-1] < str[i])
		{
			t = i-1;
			break;
		}
	}

	
	if(t == 0 && str[t] >=str[t+1])
	{
		string temp ="0";
		temp+=str;
		str = temp;
		//str+='0';
	//	cout <<str<<endl;
	//	return 0;
	//	min = '0';
		ln +=1;

	}
	int min = str[t+1];
	int index = t+1;
	
	for(int i = t; i < ln ;++i)
	{
		if(str[i] > str[t] && str[i] < min )
		{
			index = i;
		}
	}
	min = str[t];
	str[t]= str[index];
	str[index] = min;
	t+=1;

	for(int i = t ;i < ln;++i)
	{
		min = str[i];
		index = i;
		for(int j = i; j < ln;++j )
		{
			if(min >= str[j])
			{
				min = str[j];
				index = j;
			}
		}
		min = str[i];
		str[i] = str[index];
		str[index] = min;
	}
	cout << str<<endl;
	return 0;
}


int main()
{
	ifstream fin("A.in");
	ofstream fout("clocks.out");

#if RDBUF&0x01
	streambuf   *out = cout.rdbuf(fout.rdbuf());
#endif
#if RDBUF&0x02
	streambuf   *in = cin.rdbuf(fin.rdbuf());
#endif

	// insert you code here

	int t = 0;

	cin >> t;
	for(int i = 0; i < t;++i)
	{
		int n;
		cin >>  n;
		//cout << n<<endl;
		cout<< "Case #"<< i+1<<": "; 
		Next(n);
	}



	//
#if RDBUF&0x01
	cout.rdbuf(out);
#endif
#if RDBUF&0x02
	cin.rdbuf(in);
#endif
	fout.close();
	fin.close();
	return 0;
}

///
/*

//iomanip

setfill(ch)		// ch���հ�
setprecision()	// ���㾫����Ϊn
setw(w)			// ��дw���ַ���ֵ
cout <<setfill('#') //���
cout <<left//���뷽ʽ
	<<right
setbase(b)		// ������b���

cout << boolalpha; //������ʾtrue
		<<noboolalpha; //�ָ�
cout << internal;//���ŷ���

cout << showbase;		//��ʾ����
cout << uppercase << showbase;//������ĸ��д
cout<< nouppercase ;		//Сд
cout << showpoint<<noshowpoint;//��ʾС����
cout<< scientific;		//��ѧ������
cout <<fixed<<setprecision(8);
cout.unsetf(ostream::floatfield);//���������ûָ�


*/

