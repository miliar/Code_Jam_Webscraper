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



void chuli(string str)
{
	char ch[256] = {-1};

	memset(ch,-1,sizeof(ch));
	int ln = str.length();

	int t = 0;

	for(int i = 0 ; i< ln;++i)
	{
		if(ch[str[i]] == -1)
		{
			ch[str[i]]++;
			t++;
		}
	}

	

	uint64 out = 1;
	int big = 0;


	if(ln <  2 )
	{
		cout << 1 <<endl;
		return ;
	}
	memset(ch,-1,sizeof(ch));

	ch[str[0]] = 1;
	
	
	for(int i = 1; i < ln; ++i)
	{
		if(str[i] != str[0])
		{
			ch[str[i]] = 0;
			break;
		}
	}


	if(t == 1)
	{
		t = 2;

	}

	big = 2;
	out = 0;
	
	for(int i = 0 ; i < ln;++i)
	{
		if(ch[str[i]] == -1)
		{
			ch[str[i]] = big;
			big++;
		}

		out *=t;
		out += ch[str[i]];
	}

	 ostringstream sout; 
	 sout<<out;
	 cout << sout.str()<<endl;
	// return sout.str();

}
int main()
{
	ifstream fin("A.in");
	ofstream fout("A.out");

#if RDBUF&0x01
	streambuf   *out = cout.rdbuf(fout.rdbuf());
#endif
#if RDBUF&0x02
	streambuf   *in = cin.rdbuf(fin.rdbuf());
#endif


	int t = 0;
	cin >> t;

	string input;
	for(int i = 0; i < t;++i)
	{
		cin >> input;
		cout<< "Case #"<<i+1<<": ";
		chuli(input);
	}
 
	// insert you code here

	/*int64  t= 1<< 30;
	t<<=30;
	t-=1;
	cout << toString(t)<<endl;
*/

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

