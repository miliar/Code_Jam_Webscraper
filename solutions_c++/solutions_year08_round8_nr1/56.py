// Problem A - 
// StevieT's Solution
// ------------------
// Google Code Jam: Europe, Middle East, Africa Regional Semi-finals
// 6th October 2008, Google London


#include <cmath>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <string>

using namespace std;

// Outputting code
void output(const pair <double,double> & x,ostream &out,const int & testCase){
	out << "Case #" << testCase << ": " << x.first << " " << x.second << endl;
	if (&out != &cout) output(x,cout,testCase);
}

void rotate(vector <double> &v){
	for (int i=0;i<v.size();i++)
		swap(v[i],v[(i+1) % v.size()]);
};

double dist(double x1,double y1,double x2,double y2){
	return sqrt((x2-x1) * (x2-x1) + (y2-y1) * (y2-y1));
}

void tsearch2(const vector <double> & x1,const vector <double> &y1, vector <double> &x2, vector <double> &y2,double &xmin,double &ymin){
	double xmax = x2[2],ymax = y2[2];	
	if (false){
		double x = xmin;
		double y = ymin;
		double d1 = dist(x1[0],y1[0],x,y);
		double d2 = dist(x1[2],y1[2],x,y);
		double d3 = dist(x2[0],y2[0],x,y);
		double d4 = dist(x2[2],y2[2],x,y);
		if (d3/d4 < d1/d2) { swap (xmin,xmax);swap(ymin,ymax);}
	}
	for (int i=0;i<200;i++){
		double x = (xmin + xmax) / 2.0;
		double y = (ymin + ymax) / 2.0;
		double d1 = dist(x1[0],y1[0],x,y);
		double d2 = dist(x1[2],y1[2],x,y);
		double d3 = dist(x2[0],y2[0],x,y);
		double d4 = dist(x2[2],y2[2],x,y);
		//cout << x << " " << y << " "<< d1 << " " << d2  << " " << d3 << " "<< d4 << endl;

		if (d1 / d3 > d2 / d4) {
			xmin = x,ymin = y;
		} else {
			xmax = x;ymax = y;
		}
		
	}
}



pair <double,double> tsearch1(const vector <double> & x1,const vector <double> &y1, vector <double> &x2, vector <double> &y2){
	double xmin = x2[0],xmax = x2[1];
	double ymin = y2[0],ymax = y2[1];
	if (false){
		double d1 = dist(x1[0],y1[0],xmin,ymin);
		double d2 = dist(x1[1],y1[1],xmin,ymin);
		double d3 = dist(x2[0],y2[0],xmin,ymin);
		double d4 = dist(x2[1],y2[1],xmin,ymin);
		if (d1/d3<d2/d4){
			swap (xmin,xmax);
			swap(ymin,ymax);
		}
	}

	for (int i=0;i<200;i++){
		double x = (xmin + xmax) / 2.0;
		double y = (ymin + ymax) / 2.0;
		tsearch2(x1,y1,x2,y2,x,y);
		double d1 = dist(x1[0],y1[0],x,y);
		double d2 = dist(x1[1],y1[1],x,y);
		double d3 = dist(x2[0],y2[0],x,y);
		double d4 = dist(x2[1],y2[1],x,y);
		
		//cout << d1/d3 << " "<< d2/d4 << endl;

		if (d1/d3 > d2/d4) {
			xmin = (xmin + xmax) / 2.0;ymin = (ymin + ymax) / 2.0;
		} else {
			xmax = (xmin + xmax) / 2.0;ymax = (ymin + ymax) / 2.0;
		}
		
	}
		tsearch2(x1,y1,x2,y2,xmin,ymin);

		double d1 = dist(x1[0],y1[0],xmin,ymin);
		double d2 = dist(x1[1],y1[1],xmin,ymin);
		double d3 = dist(x1[2],y1[2],xmin,ymin);
		double d4 = dist(x2[0],y2[0],xmin,ymin);
		double d5 = dist(x2[1],y2[1],xmin,ymin);
		double d6 = dist(x2[2],y2[2],xmin,ymin);
		//cout << d1 / d4 << " " << d2/d5  << " " << d3 / d6 << " " << d6/d5  << " " <<d1 / d3 << " " << d4/d6  <<endl;
		return make_pair (xmin,ymin);
}

// Solution code
pair <double,double> solve(const vector <double> & x1,const vector <double> &y1, vector <double> &x2, vector <double> &y2){
		//rotate(x2);
		//rotate(y2);
	for (int iter = 0;iter < 3;iter++){
		vector <long long> s1(3),s2(3);
		for (int i=0;i<3;i++)
			s1[i] = (x1[(i+1) % 3] - x1[i]) * (x1[(i+1) % 3] - x1[i]) + (y1[(i+1) % 3] - y1[i]) * (y1[(i+1) % 3] - y1[i]);
		for (int i=0;i<3;i++)
			s2[i] = (x2[(i+1) % 3] - x2[i]) * (x2[(i+1) % 3] - x2[i]) + (y2[(i+1) % 3] - y2[i]) * (y2[(i+1) % 3] - y2[i]);
		bool bad = false;
		for (int i=0;i<3;i++)
			if (s1[i] * s2[(i+1)%3] != s2[i] * s1[(i+1)%3]) bad = true;
		if (bad){cout << "bad" << endl; continue;}
		return tsearch1(x1,y1,x2,y2);
		rotate(x2);
		rotate(y2);

	}
};

// A few utility I/O functions
vector <string> split(const string &s,const char &separator=' '){vector <string> ret;int p1=0,p2;for (p2 = 0;p2 < s.size();p2++)if (s[p2]==separator){if (p2-p1>0) ret.push_back(s.substr(p1,p2-p1));p1=p2+1;}if (p2-p1 > 0) ret.push_back(s.substr(p1,p2-p1));return ret;}
template <class T> T get(istream &fin){string s;getline(fin,s);stringstream ss(s);T ret;ss >> ret;return ret;}
template <class T> vector <T> getv(istream &fin,const char &separator = ' '){string s;getline(fin,s);vector <string> convert = split(s,separator);vector <T> ret(convert.size());for (int i=0;i<convert.size();i++){stringstream ss(convert[i]);ss>>ret[i];}return ret;}
template <> vector <string> getv <string> (istream &fin,const char &separator){string s;getline(fin,s);return split(s,separator);}

int main(int argc,const char* argv[])
{
	try{
		istream * in__;ostream * out__;
		if (argc < 2) in__ = &cin;else in__ = new ifstream(argv[1]);if (in__->fail()) throw string("Input file could not be opened");
		if (argc < 3) out__ = &cout;else out__ = new ofstream(argv[2]);if (out__->fail()) throw string("Ouput file could not be opened");
		istream & in = *in__; ostream & out = *out__;
		
		int testCases,testCase = 1;
		for (in >> testCases;testCase <= testCases;testCase++){

	out.setf(ios::fixed,ios::floatfield);
	out.precision(8);

	cout.setf(ios::fixed,ios::floatfield);
	cout.precision(8);

// Do File input stuff here
			vector <double> x1(3),y1(3),x2(3),y2(3);
			for (int i=0;i<3;i++)
				in >> x1[i] >> y1[i];
			for (int i=0;i<3;i++)
				in >> x2[i] >> y2[i];
			output(solve(x1,y1,x2,y2),out,testCase);
		}



		if (in__ != &cin) delete in__;if (out__ != &cout) delete out__;
	} catch(string s){
		cout << "Error: " << s << endl;
	} catch(std::exception e){
		cout << "std exception: " << e.what() << endl;
	}
}
