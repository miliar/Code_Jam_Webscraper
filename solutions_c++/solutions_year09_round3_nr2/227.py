#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<sstream>
#include<string>
#include<iterator>
#include<vector>
#include<set>
#include<map>
#include<algorithm>
#include<iomanip>
#include<math.h>
using namespace std;
typedef unsigned long long ull;
struct Vector3{
	double x,y,z;
	Vector3():x(0),y(0),z(0){}
	Vector3(double x,double y,double z):x(x),y(y),z(z){}
};
Vector3&operator+=(Vector3&x,const Vector3&y){
	x.x += y.x;
	x.y += y.y;
	x.z += y.z;
	return x;
}
Vector3 operator/(Vector3 x,double y){
	return Vector3(x.x/y,x.y/y,x.z/y);
}
Vector3 operator+(const Vector3&x,const Vector3&y){
	return Vector3(x) += y;
}
double dot(Vector3 x,Vector3 y){
	return x.x*y.x + x.y*y.y + x.z*y.z;
}
double norm(Vector3 x){
	return dot(x,x);
}
double abs(Vector3 x){
	return sqrt(norm(x));
}
Vector3 operator*(const Vector3&x,double v){
	return Vector3(x.x * v , x.y * v , x.z * v);
}
istream&operator>>(istream&cin,Vector3&v){
	return cin >> v.x >> v.y >> v.z;
}
void solve(Vector3 p,Vector3 v){
	double s = -dot(p , v)*1.0 / norm(v);
	if(norm(v)==0)s = 0;
	if(s < 0)s = 0;
	printf("%.16f %.16f",abs(p + v*s),s);
}
int main(){
	int k;
	string line;
	getline(cin,line);
	cout.sync_with_stdio();
	stringstream(line) >> k;
	for(int i=1;i<=k;++i){
		int m;
		{
		getline(cin,line);
		stringstream ss(line);
		ss >> m;
		}
		Vector3 p,v;
		for(int j=0;j<m;++j){
			getline(cin,line);
			stringstream ss(line);
			Vector3 tp,tv;
			ss >> tp >> tv;
			p += tp;
			v += tv;
		}
		
		cout << "Case #"<<i<<": ";
		solve(p/m,v/m);
		cout << endl;
	}
}
