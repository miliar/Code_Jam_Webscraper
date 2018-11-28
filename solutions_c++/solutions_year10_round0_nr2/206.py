#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define SIZE(X) ((int)(X.size()))
typedef long long int64;
#define two(X) (1<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define REP(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
const double pi=acos(-1.0); 
const double eps=1e-11; 
template<class T> inline void getmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void getmax(T &a,T b){if(b>a) a=b;}
using namespace std;
int m,n,x,y,z,ret; 
#include <iostream>
#include <string>
using namespace std;

inline int compare(string str1, string str2)
{
	if(str1.size() > str2.size()) //长度长的整数大于长度小的整数
		return 1;
	else if(str1.size() < str2.size())
		return -1;
	else
		return str1.compare(str2); //若长度相等，从头到尾按位比较，compare函数：相等返回0，大于返回1，小于返回－1
}
//高精度加法
string ADD_INT(string str1, string str2)
{
	string MINUS_INT(string str1, string str2);
	int sign = 1; //sign 为符号位
	string str;
	if(str1[0] == '-') {
		if(str2[0] == '-') {
			sign = -1;
			str = ADD_INT(str1.erase(0, 1), str2.erase(0, 1));
		}else {
			str = MINUS_INT(str2, str1.erase(0, 1));
		}
	}else {
		if(str2[0] == '-')
			str = MINUS_INT(str1, str2.erase(0, 1));
		else {
			//把两个整数对齐，短整数前面加0补齐
			string::size_type l1, l2;
			int i;
			l1 = str1.size(); l2 = str2.size();
			if(l1 < l2) {
				for(i = 1; i <= l2 - l1; i++)
					str1 = "0" + str1;
			}else {
				for(i = 1; i <= l1 - l2; i++)
					str2 = "0" + str2;
			}
			int int1 = 0, int2 = 0; //int2 记录进位
			for(i = str1.size() - 1; i >= 0; i--) {
				int1 = (int(str1[i]) - 48 + int(str2[i]) - 48 + int2) % 10;  //48 为 '0' 的ASCII 码
				int2 = (int(str1[i]) - 48 + int(str2[i]) - 48 +int2) / 10;
				str = char(int1 + 48) + str;
			}
			if(int2 != 0) str = char(int2 + 48) + str;
		}
	}
	//运算后处理符号位
	if((sign == -1) && (str[0] != '0'))
		str = "-" + str;
	return str;
}


//高精度减法
string MINUS_INT(string str1, string str2)
{
	string MULTIPLY_INT(string str1, string str2);
	int sign = 1; //sign 为符号位
	string str;
	if(str2[0] == '-')
		str = ADD_INT(str1, str2.erase(0, 1));
	else {
		int res = compare(str1, str2);
		if(res == 0) return "0";
		if(res < 0) {
			sign = -1;
			string temp = str1;
			str1 = str2;
			str2 = temp;
		} 
			// while(str2.size()<str1.size())str2='0'+str2;
			// stringstream ss(str2);
			// int s;
			// ss>>s;
			//s=s;
			// for(int i=0;i<str1.size();i++){
			//	 if(str1[i]>=str2[i]){
			//		str1[i]=str1[i]-str2[i]+'0'; 
			//	 }else{
			//		 str1[i]=str1[i]+10-str2[i]+'0';int k=1;
			//		 while(str1[i-k]=='0')
			//		 {
			//			str1[i-k]='9';k++;
			//		 }
			//		 str1[i-k]=str1[i-k]-1;
			//	 }
			// }
			// str=str1;
		string::size_type tempint;
		 stringstream ss(str2);
		 int s;
		 ss>>s;
		s=s;
		tempint = str1.size() - str2.size();
		for(int i = str2.size() - 1; i >= 0; i--) {
			if(str1[i + tempint] < str2[i]) {
				//str1[i + tempint - 1] = char(int(str1[i + tempint - 1]) - 1);
				int k=1;
				while(str1[i+tempint-k]=='0'){
					str1[i+tempint-k]='9';k++;
				}
				str1[i+tempint-k]=str1[i+tempint-k]-1;
				str = char(str1[i + tempint] - str2[i] + 58) + str;
			}
			else
				str = char(str1[i + tempint] - str2[i] + 48) + str;
		}
		for(int i = tempint - 1; i >= 0; i--)
			str = str1[i] + str;
	}
	//去除结果中多余的前导0
	str.erase(0, str.find_first_not_of('0'));
	if(str.empty()) str = "0";
	if((sign == -1) && (str[0] != '0'))
		str = "-" + str;
	return str;
}

//高精度乘法
string MULTIPLY_INT(string str1, string str2)
{
	int sign = 1; //sign 为符号位
	string str;
	if(str1[0] == '-') {
		sign *= -1;
		str1 = str1.erase(0, 1);
	}
	if(str2[0] == '-') {
		sign *= -1;
		str2 = str2.erase(0, 1);
	}
	int i, j;
	string::size_type l1, l2;
	l1 = str1.size(); l2 = str2.size();
	for(i = l2 - 1; i >= 0; i --) {  //实现手工乘法
		string tempstr;
		int int1 = 0, int2 = 0, int3 = int(str2[i]) - 48;
		if(int3 != 0) {
			for(j = 1; j <= (int)(l2 - 1 - i); j++)
				tempstr = "0" + tempstr;
			for(j = l1 - 1; j >= 0; j--) {
				int1 = (int3 * (int(str1[j]) - 48) + int2) % 10;
				int2 = (int3 * (int(str1[j]) - 48) + int2) / 10;
				tempstr = char(int1 + 48) + tempstr;
			}
			if(int2 != 0) tempstr = char(int2 + 48) + tempstr;
		}
		str = ADD_INT(str, tempstr);
	}
	//去除结果中的前导0
	str.erase(0, str.find_first_not_of('0'));
	if(str.empty()) str = "0";
	if((sign == -1) && (str[0] != '0'))
		str = "-" + str;
	return str;
}
//高精度除法
string DIVIDE_INT(string str1, string str2, int flag)
{
	//flag = 1时,返回商; flag = 0时,返回余数
	string quotient, residue; //定义商和余数
	int sign1 = 1, sign2 = 1;
	if(str2 == "0") {  //判断除数是否为0
		quotient = "ERROR!";
		residue = "ERROR!";
		if(flag == 1) return quotient;
		else return residue;
	}
	if(str1 == "0") { //判断被除数是否为0
		quotient = "0";
		residue = "0";
	}
	if(str1[0] == '-') {
		str1 = str1.erase(0, 1);
		sign1 *= -1;
		sign2 = -1;
	}
	if(str2[0] == '-') {
		str2 = str2.erase(0, 1);
		sign1 *= -1;
	}
	int res = compare(str1, str2);
	if(res < 0) {
		quotient = "0";
		residue = str1;
	}else if(res == 0) {
		quotient = "1";
		residue = "0";
	}else {
		string::size_type l1, l2;
		l1 = str1.size(); l2 = str2.size();
		string tempstr;
		tempstr.append(str1, 0, l2 - 1);
		//模拟手工除法
		for(int i = l2 - 1; i < l1; i++) {
			int k=0;while(tempstr[k]=='0')k++;
			tempstr = tempstr.substr(k);
			tempstr = tempstr + str1[i];
			for(char ch = '9'; ch >= '0'; ch --) { //试商
				string str;
				str = str + ch;
				if(compare(MULTIPLY_INT(str2, str), tempstr) <= 0) {
					quotient = quotient + ch;
					tempstr = MINUS_INT(tempstr, MULTIPLY_INT(str2, str));
					break;
				}
			}
		}
		residue = tempstr;
	}
	//去除结果中的前导0
	quotient.erase(0, quotient.find_first_not_of('0'));
	if(quotient.empty()) quotient = "0";
	if((sign1 == -1) && (quotient[0] != '0'))
		quotient = "-" + quotient;
	if((sign2 == -1) && (residue[0] != '0'))
		residue = "-" + residue;
	if(flag == 1) return quotient;
	else return residue;
}

//高精度除法,返回商
string DIV_INT(string str1, string str2)
{
	return DIVIDE_INT(str1, str2, 1);
}
//高精度除法,返回余数
string MOD_INT(string str1, string str2)
{
	return DIVIDE_INT(str1, str2, 0);
} 

bool cmp(const string& str1,const string& str2){
	if(str1.size()!=str2.size())
		return str1.size()<str2.size();
	else 
		return str1<str2;
}
//string MINUS_INT(string& str1, string& str2)
//{
//	 string res=str1;
//	 while(str2.size()<str1.size())str2='0'+str2;
//	 for(int i=0;i<str1.size();i++){
//		 if(res[i]>=str2[i]){
//			res[i]=res[i]-str2[i]+'0'; 
//		 }else{
//			 res[i]=res[i]+10-str2[i]+'0';int k=1;
//			 while(res[i-k]=='0')
//			 {
//				res[i-k]='9';k--;
//			 }
//			 res[i-k]=res[i-k]-1;
//		 }
//	 }
//	 int k=0;while(res[k]=='0')k++;
//	 res=res.substr(k);
//	 return res;
//} 
string gcd(const string& a,const string& b){
	return b=="0"?a:gcd(b,MOD_INT(a,b));
}
int main(){ 
	freopen("B-large.in","r",stdin); 
	freopen("B-large.out","w",stdout); 
	vector<string> vec; 
	string tmp; cin>>n; 
	REP(testcase,n){
		vec.clear();
		cin>>m;string tmp;string res;
		REP(i,m){
			cin>>tmp;vec.push_back(tmp);
		}
		sort(vec.begin(),vec.end(),cmp); 
		vector<string> mi;
		for(int i=1;i<vec.size();i++) {
			if(vec[i]==vec[i-1])continue;
			string now=MINUS_INT(vec[i],vec[i-1]); 
			mi.push_back(now);
		} 
		string mod;
		if(mi.size()==1)
			mod=mi[0];
		else{
			mod=gcd(mi[0],mi[1]);
			for(int i=2;i<mi.size();i++)
				mod=gcd(mod,mi[i]);
		} 
		string test=MOD_INT(vec[0],mod);
		if(test=="0")res=test;
		else res=MINUS_INT(mod,test);
		cout<<"Case #"<<testcase+1<<": "<<res<<endl;
	}
	return 0;
}