#include<iostream>
#include <map>

using namespace std;


int t;
string st;

int convert(char ch)
{
	if ( ch == '0' ) return 0;
	if ( ch == '1' ) return 1;
	if ( ch == '2' ) return 2;
	if ( ch == '3' ) return 3;
	if ( ch == '4' ) return 4;
	if ( ch == '5' ) return 5;
	if ( ch == '6' ) return 6;
	if ( ch == '7' ) return 7;
	if ( ch == '8' ) return 8;
	if ( ch == '9' ) return 9;
	return -1;
}

char revert(int ch)
{
	if ( ch == 1 ) return '1';
	if ( ch == 2 ) return '2';
	if ( ch == 3 ) return '3';
	if ( ch == 4 ) return '4';
	if ( ch == 5 ) return '5';
	if ( ch == 6 ) return '6';
	if ( ch == 7 ) return '7';
	if ( ch == 8 ) return '8';
	if ( ch == 9 ) return '9';
	if ( ch == 0 ) return '0';
	return ' ';
}


string convert_to_string(int k)
{
    string result = "";
    int u = k;
    while ( u != 0 ){
        result += revert((int)u%10);
        u = u / 10;
    }
    return result;
}

struct BigInt {
	string s;
	
	BigInt(string s1){
		s = s1;
	}
	
	BigInt(int n){
		string s1 = "";
		while ( n != 0 ){
			int du = n % 10 ;
			s1 = revert(du) + s1;
			n = n / 10;
		}
		s = s1;
	}
	~BigInt(){
		s = "";
	}
};

BigInt cong(BigInt a, BigInt b)
{
	string s= "";
	string s1 = a.s;
	string s2 = b.s;
	if ( s1.length() < s2.length() ){
		int temp = s2.length() - s1.length();
		for (int i = 0 ; i < temp  ; i ++ )
			s1 = '0' + s1;
	}
	else if ( s1.length() > s2.length() ){
		int temp = s1.length() - s2.length();
		for ( int i = 0 ; i < temp ; i ++ )
			s2 = '0' + s2;
	}
	bool nho = false;
	for (int i = s1.length() - 1 ; i >= 0 ; i -- ){
		int temp = convert(s1[i]) + convert(s2[i]);
		if ( nho ) temp ++ ;
		if ( temp > 9 ) nho = true;
		else nho = false;
		temp = temp % 10;
		s = revert(temp) + s;
	}
	if ( nho ) s = '1' + s;
	return BigInt(s);
}


BigInt nhan1(BigInt a, char ch)
{
	int k = convert(ch);
	string s = "";
	string s1 = a.s;
	int nho = 0;
	for ( int i = s1.length() - 1 ; i >= 0 ; i -- ){
		int temp = convert(s1[i] ) * k + nho;
		nho = temp / 10;
		temp = temp % 10;
		s = revert(temp) + s;
	}
	if ( nho > 0 ) s = revert(nho) + s;
	return BigInt(s);
}

BigInt nhan(BigInt b, BigInt a)
{
	string s1 = a.s;
	BigInt result("0");
	for ( int i = s1.length()-1 ; i >= 0 ; i -- ){
		BigInt temp = nhan1(b, s1[i]);
		string s = temp.s;
		for ( int j = 0 ; j < s1.length() - 1 - i ; j ++ )
			s = s + '0';
		temp = BigInt(s);
		result = cong(result, temp);
		//cout << result.s << endl;
	}
	return result;
}


BigInt coso(int k, BigInt vt)
{
    if ( vt.s[0] == '0' ) return BigInt("1");
    BigInt resl("1");
    for ( int i = 0 ; i < k ; i ++ ){
        resl = nhan(resl, vt);
    }
    return resl;
}

void process(int k)
{
    map<char, int> m;
    map<char, bool> m1;
    bool bo = false;
    int vt = 2;
    m[st[0]] = 1;
    m1[st[0]] = true;
    for ( int i = 1 ; i < st.length(); i ++ ){
        if ( m1[st[i]] == true ){
            
        }
        else{
            if ( bo == false ){ m[st[i]] = 0; bo = true ; m1[st[i]] = true;}
            else {
                m[st[i]] = vt;
                m1[st[i]] = true;
                vt ++;
            }
        }
    }
    
    int result =  0;
    //convert_to_string(vt);
    BigInt base(convert_to_string(vt));
    BigInt res("0");
    
    
    
    for ( int i = 0 ; i < st.length() ; i ++ ){
        res = cong ( res, nhan(BigInt(convert_to_string(m[st[i]])), coso(st.length()-1-i, vt)));
    }
    
    cout << "Case #" << k << ": "<< res.s << endl;    
}


void load()
{
    cin >> t ;
    for ( int i = 0 ; i < t ; i ++ ){
        cin >> st;
        process(i+ 1);
    }
}


int main()
{
    load();
    return 0;
}
