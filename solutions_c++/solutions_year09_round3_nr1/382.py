/* Google Code Jam 2009
   Round 1C

   Problem: A

   author: David Volgyes

 */

#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <stdint.h>
using namespace std;

// ----------------------------------------------------------------------------------------

#define foreach(variable,vector) for(int variable=0;i<vector.size();++variable)
#define reverse_foreach(variable,vector) for(int variable=vector.size()-1;i>=0;--variable)
#define sort(vector) sort(vector.begin(),vector.end())
#define reverse_sort(vector) sort(vector.begin(),vector.end())

template <class T>
int minimum_position(const vector<T> & vect)
{
int pos=0;
T value=vect[pos];
foreach(i,vect)	{if (vect[i]<vect[pos]) pos=i;}
return pos;
}

template <class T>
int maximum_position(const vector<T> & vect){
int pos=0;
T value=vect[pos];
foreach(i,vect)	{if (vect[i]>vect[pos]) pos=i;}
return pos;
}

template <class T>
int find_first(const vector<T> & vect, const T& value){
foreach(i,vect)	{if (vect[i]==value) return i;}
return -1;
}

template <class T>
int find_last(const vector<T> & vect, const T& value){
reverse_foreach(i,vect)	{if (vect[i]==value) return i;}
return -1;
}

template <class T>
int count(const vector<T> & vect, const T& value){
	int result=0;
reverse_foreach(i,vect)	{if (vect[i]==value) ++result;}
return result;
}


template <class T>
std::ostream & operator<<(ostream& out,vector<T>& vect)
{
	out<<"[";
	if (vect.size()) out<<vect[0];
	for(int i=1;i<vect.size();i++)
		out<<","<<vect[i];
	out<<"]"<<std::endl;
	return out;
}

template <class T>
vector<T> subvector(const vector<T>& input,int first,int last)
{
	vector<T> result;
	result.resize(last-first+1);
	for(int i=first;i<=last;++i) result[i-first]=input[i];
	return result;
}

template<class T>
class Grid
{
public:

	void resize(int i,int j)
	{
		elements.resize(i);
		foreach(i,elements) {elements[i].resize(j);}
	}

	vector<T>& operator[](int i) {return elements[i];}
private:
	vector<vector<T> > elements;
};

template<class T>
class Tree {

	Tree(){weight=1.0;}

	Tree& operator[](const T& node)
	{
		foreach(i,subtree)
		{
			if (subtree[i].isNode(node)) return subtree[i];
		}
		return *this;
	}

	bool isNode(const T& node)
	{
		return node==nodeID;
	}

private:
	T nodeID;
	double weight;
	vector<Tree<T> > subtree;
};

struct Point{
	double x,y;
};

struct Polygon {
	vector<Point> points;
	void add(Point p) {points.push_back(p);}
	void add(double x,double y) {Point p;p.x=x;p.y=y;points.push_back(p);}

	Point& operator[](int i) {return points.at(i);}

	double area(void){
		double result=0;
		for(int i=0;i<points.size()-1;i++)
			result+=points[i].x*points[i+1].y-points[i+1].x*points[i].y;
			return fabsl(0.5*result);
	}
};


vector<char> toVectorOfChar(const string& input)
{
vector<char> result;
for(int i=0;i<input.size();++i)
	result.push_back(input[i]);
return result;
}
// ----------------------------------------------------------------------------------------

long long int Power(long long int x,int exp)
{
	long long int result=1;
	for(int i=0;i<exp;++i) result*=x;
	return result;
}

long long int solve(vector<char> number)
{
vector<char> digits;
foreach(i,number) {
	if (find_first(digits,number[i])==-1)
		digits.push_back(number[i]);
}
int base=digits.size();
if (base<2) base=2;
vector<long long int> value;
value.push_back(1);
value.push_back(0);
for(int i=2;i<digits.size();++i) value.push_back(i);
long long int result=0;
foreach(i,number) {
 result+=value[find_first(digits,number[i])]*
		 Power(base,number.size()-i-1);
}
return result;
}

int main() {
	int numberOfTestCases;
	int Case=0;
	string text;
	getline(std::cin,text);
	numberOfTestCases=atoi(text.c_str());
	vector<char> chars;
	// Main loop
	do{
		Case=Case+1;
		string result="";
		getline(std::cin,text);
		//cout<<"number"<<text<<std::endl;
		//cout<<chars;
		cout<<"Case #"<<Case<<": ";
		printf("%lld",(long long int)solve(toVectorOfChar(text)));
		cout<<endl;
	}
	while(Case<numberOfTestCases);
	return 0;
}
