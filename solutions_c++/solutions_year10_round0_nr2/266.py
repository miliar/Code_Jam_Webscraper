#include <iostream>
#include <fstream>
#include <string>
using namespace std;

#define maxsize 100
ofstream ofs("out.txt");
struct hp{
	hp& operator=(const hp& rhs){
		len = rhs.len;
		for(int i = 0; i <= maxsize; ++i)
			s[i] = rhs.s[i];
		return *this;
	}
	int len;
	int s[maxsize+1];
};
void input(hp &a, string str){
	int i;
	while(str[0] == '0' && str.size() != 1)
		str.erase(0, 1);
	a.len = (int)str.size();
	for(i = 1; i <= a.len; ++i)
		a.s[i] = str[a.len - i] - 48;
	for(i = a.len + 1; i <= maxsize; ++i)
		a.s[i] = 0;
}
void print(const hp &y){
	int i;
	for(i = y.len; i >= 1; i--)
		ofs<<y.s[i];
	ofs<<endl;
}

int compare(const hp& a, const hp& b){
	int len;
	if(a.len > b.len)
		len = a.len;
	else
		len = b.len;
	while(len > 0 && a.s[len] == b.s[len])len--;
	if(len == 0)
		return 0;
	else
		return a.s[len] - b.s[len];
}
void multiply10(hp &a){
	int i;
	for(i = a.len; i >= 1; i--)
		a.s[i+1] = a.s[i];
	a.s[1] = 0;
	a.len++;
	while(a.len > 1 && a.s[a.len] == 0)
		a.len--;
}
void subtract(const hp& a, const hp& b, hp &c){
	int i, len;
	for(i = 1; i <= maxsize; ++i)
		c.s[i] = 0;
	if(a.len > b.len)
		len = a.len;
	else
		len = b.len;
	for(i = 1; i <= len; ++i){
		c.s[i] += a.s[i] - b.s[i];
		if(c.s[i] < 0){
			c.s[i] += 10;
			--c.s[i + 1];
		}
	}
	while(len > 1 && c.s[len] == 0) len--;
	c.len = len;
}

void divideh(const hp& a, const hp& b, hp &c, hp &d){
	hp e;
	int i,len;
	for(i = 1; i <= maxsize; ++i){
		c.s[i] = 0;
		d.s[i] = 0;
	}
	len = a.len;
	d.len = 1;
	for(i = len; i >= 1; i--){
		multiply10(d);
		d.s[1] = a.s[i];
		while(compare(d,b) >= 0){
			subtract(d, b, e);
			d = e;
			c.s[i]++;
		}
	}
	while(len > 1 && c.s[len] == 0)
		len--;
	c.len = len;
}

void calCom(const hp& a, const hp&b, hp &c){
	hp x = a;
	hp y = b;
	hp temp;
	hp yu;
	divideh(x, y, temp, yu);
//	print(yu);
	while(1){
		if(yu.len == 1 && yu.s[1] == 0)
			break;
		x = y;
		y = yu;
		divideh(x, y, temp, yu);	
	}
	c = y;
}

hp data[1200];
hp dif[1200];
int n;
int main(){
	ifstream ifs("in.txt");

	int t;
	ifs>>t;
	int test = 1;
	while(t--){
		ifs>>n;
		for(int i = 0; i != n; ++i){
			string temp;
			ifs>>temp;
			input(data[i], temp);
		}
		int count = 0;
		for(int i = 0; i != n - 1; ++i){
			int c = compare(data[i], data[i+1]);
			if(c != 0){
				if(c > 0){
					subtract(data[i], data[i+1], dif[count++]);
				}else{
					subtract(data[i+1], data[i], dif[count++]);
				}
			}
		}
		hp com = dif[0];
		for(int i = 1; i != count; ++i){
			calCom(com, dif[i], com);
		}
		hp g1,g2;
		divideh(data[0], com, g1, g2);
		ofs<<"Case #"<<test<<": ";
		if(g2.len == 1 && g2.s[1] == 0)
			ofs<<0<<endl;
		else{
			subtract(com, g2, g1);
			print(g1);
		}
		++test;
	}
	ofs.close();
	ifs.close();
	return 0;
}