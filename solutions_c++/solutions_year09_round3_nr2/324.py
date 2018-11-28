/* Google Code Jam 2009
   Round 1C

   Problem: B

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

struct Vect3d
{   Vect3d(){x=0;y=0;z=0;}
double x,y,z;
};

double length(Vect3d v)
{
	return sqrt(v.x*v.x+v.y*v.y+v.z*v.z);
}

double scalarProduct(Vect3d u,Vect3d  v)
{
	return (u.x*v.x+u.y*v.y+u.z*v.z);
}
Vect3d vectorProduct(Vect3d u,Vect3d  v)
{
	Vect3d result;
	result.x=u.x*v.y-v.x*u.y;
	result.y=u.y*v.z-v.y*u.z;
	result.z=u.z*v.x-v.z*u.x;
	return result;
}

Vect3d sub(Vect3d u,Vect3d  v)
{
	Vect3d result;
	result.x=u.x-v.x;
	result.y=u.y-v.y;
	result.z=u.z-v.z;
	return result;
}
Vect3d add(Vect3d u,Vect3d  v)
{
	Vect3d result;
	result.x=u.x+v.x;
	result.y=u.y+v.y;
	result.z=u.z+v.z;
	return result;
}

int main() {
	int numberOfTestCases;
	int Case=0;
	string text;
	getline(std::cin,text);
	numberOfTestCases=atoi(text.c_str());
	double x,y,z,vx,vy,vz;

	// Main loop
	do{
		Case=Case+1;
		string result="";
		int fireflies;
		Vect3d M,Mv;

		double t=0,d=0;
		cin>>fireflies;
		for(int i=0;i<fireflies;++i)
		{
			cin>>x;M.x+=x;
			cin>>y;M.y+=y;
			cin>>z;M.z+=z;
			cin>>vx;Mv.x+=vx;
			cin>>vy;Mv.y+=vy;
			cin>>vz;Mv.z+=vz;
		}
		if (fireflies>0) {
		M.x/=fireflies;
		M.y/=fireflies;
		M.z/=fireflies;
		Mv.x/=fireflies;
		Mv.y/=fireflies;
		Mv.z/=fireflies;
		}
		//cout<<M.x<<" "<<M.y<<" "<<M.z<<" "<<endl;
		//cout<<Mv.x<<" "<<Mv.y<<" "<<Mv.z<<" "<<endl;

		if ((length(Mv)<=0) || (scalarProduct(M,Mv)>0)) {
			d=length(M);
			t=0;
		}else {
			//printf("else");
			Vect3d nearest,tempv,origo;
			double temp;
			temp=scalarProduct(sub(origo,M),Mv)/length(Mv)/length(Mv);
			tempv.x=temp*Mv.x;
			tempv.y=temp*Mv.y;
			tempv.z=temp*Mv.z;

			nearest=add(M,tempv);
			d=length(sub(nearest,origo));
			t=length(sub(nearest,M))/length(Mv);
		}

		cout<<"Case #"<<Case<<": ";
		printf("%0.12lf %0.12lf",d,t);
		cout<<endl;
	}
	while(Case<numberOfTestCases);
	return 0;
}
