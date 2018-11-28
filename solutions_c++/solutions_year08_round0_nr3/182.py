#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <cmath>
#include <iostream>
#include <cstdlib>
#include <iomanip>

//#define  INFILE  "C-small.in"
//#define OUTFILE  "C-small.out"

//#define  INFILE  "C-small-attempt1.in"
//#define OUTFILE  "C-small-attempt1.out"

#define  INFILE  "C-large.in"
#define OUTFILE  "C-large.out"

using namespace std;

const long double EPSILON = 1e-12;
const long double PI=3.14159265358979323846;

class T
{
	public:
		template<typename T> static void print(const string name, const T value)
		{
			cout << name<<": " <<value<<endl;
		}
		
		template<typename T> static void print(const string name, const vector<T> v)
		{
			cout<<name<<": ";
			for(int i=0;i<v.size();++i)
			{
				cout<<v[i]<<(i==v.size()-1 ? "\n":" ");
			}
		}
		
		template<typename T> static void 
		print(const string name, const vector<vector<T> > v)
		{
			cout<<name<<":"<<endl;
			for(int i=0;i<v.size();++i)
			{
				for(int j=0;j<v[i].size();++j)
				{
					cout<<v[i][j]<<(j==v[i].size()-1 ? "\n":" ");
				}
			}		
		}		
};


bool isInCycle(long double x, long double y, long double radius)
{
	long double sign=x*x+y*y-radius*radius;
	if(sign<-EPSILON)
	{
		return true;
	}
	else
	{
		return false;
	}	
}

long double areaArc(long double x1, long double y1,long double x2, long double y2, long double ra)
{
	long double area=0;
	long double sita=2*asin(sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))/(2*ra));
//	T::print("sita",sita);
	area=sita*ra*ra/2 - ra*ra*(sin(sita))/2;
//	T::print("areaArc",area);
	return area;
}

/*
long double areaTri(long double x1,long double y1,long double x2, long double y2,long double x3, long double y3)
{
	long double a=sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1));
	long double b=sqrt((x3-x1)*(x3-x1)+(y3-y1)*(y3-y1));
	long double c=sqrt((x3-x2)*(x3-x2)+(y3-y2)*(y3-y2));
	long double s=(a+b+c)/2;
	
	return sqrt(s*(s-a)*(s-b)*(s-c));
}
*/

long double areaGrid(long double cx, long double cy, long double f,long double R,long double t,long double r, long double g)
{
	long double ra=R-t-f;
	long double side=g-2*f;
	long double halfside=side/2;
	
	if(side<EPSILON)
	{
		return 0;
	}	
	long double urx=cx+halfside, ury=cy +halfside;
	long double llx=cx - halfside, lly=cy - halfside;
	bool ur=isInCycle(urx,ury,ra);
	bool ll=isInCycle(llx,lly,ra);
//	cout <<"ll: "<<ll<<endl;
	if(ur)
	{
		return 	side*side;
	}
	else if(!ll)
	{
//		cout << "ll=false"<<endl;
		return 0;
	}
	else
	{
	}
	
	long double  lrx=cx + halfside, lry=cy - halfside;
	long double 	ulx=cx - halfside, uly=cy + halfside;	
	bool lr,ul;
	lr=isInCycle(lrx,lry,ra);
	ul=isInCycle(ulx,uly,ra);

	
	long double area=0;
	if(ll&&!lr&&!ul&&!ur)
	{
		long double ax=llx,ay=sqrt(ra*ra-llx*llx);
		long double bx=sqrt(ra*ra-lly*lly),by=lly;
				
		area=(bx-llx)*(ay-lly)/2 + areaArc(ax,ay,bx,by,ra);
//		T::print("area1",area);
	}
	else if(ll&&!lr&&ul&&!ur)
	{
		long double ax=sqrt(ra*ra-uly*uly),ay=uly;
		long double bx=sqrt(ra*ra-lly*lly),by=lly;
		
		area=(uly-lly)*(ax-ulx) + (bx-ax)*(uly-lly)/2 + areaArc(ax,ay,bx,by,ra);
//		T::print("area2",area);
	}
	else if(ll&&lr&&!ul&&!ur)
	{
		long double ax=llx,ay=sqrt(ra*ra-llx*llx);
		long double bx=lrx,by=sqrt(ra*ra-lrx*lrx);
		
		area=(lrx-llx)*(by-lry) + (lrx-llx)*(ay-by)/2 + areaArc(ax,ay,bx,by,ra);
//		T::print("area3",area);
	}
	else if(ll&&lr&&ul&&!ur)
	{
		long double ax=sqrt(ra*ra-uly*uly),ay=uly;
		long double bx=lrx,by=sqrt(ra*ra-lrx*lrx);		
		
		area=(ax-llx)*(uly-lly) + (lrx-ax)*(by-lry) + (bx-ax)*(ay-by)/2
				+ areaArc(ax,ay,bx,by,ra);
//		T::print("area4",area);
	}
	else
	{
		
	}
//	T::print("areaGrid",area);
	return area;
} 

long double areaNotHit(long double f,long double R,long double t,long double r, long double g)
{
	long double total=0;
	long double delta=2*r+g;
	long double ra=R-t-f;
	long double side=g-2*f;
	if(ra<EPSILON||side<EPSILON)
	{
		return 0;
	}
//	T::print("ra",ra);
	long double inx=(ra+ side/2 -r - g/2)/delta;
//	T::print("inx",inx);
	for(int i=0; i<=inx; ++i)
	{
		for(int j=0; j<=inx;++j)
		{
			total+=areaGrid(r + g/2 + i*delta, r + g/2 + j*delta,f,R,t,r,g);
		}
	}	
//	T::print("total",4*total);
	return 4*total;				
}


int main()
{
	ifstream fin(INFILE);
	ofstream fout(OUTFILE);
	if(!fin)cout << "can't open input file!"<<endl;
	if(!fout)cout<< "can't creat output file!"<<endl;
{
	int N;
	fin>>N;
	for(int i=1;i<=N;++i)
	{
		long double f,R,t,r,g;
		fin>>f>>R>>t>>r>>g;
		long double p=1 - areaNotHit(f,R,t,r,g)/(PI*R*R);
		
		fout<<fixed;
		setprecision(6);
		fout<<"Case #"<<i<<": "<<p<<endl;
	}
	


	
		

	
}	
	fin.close();
	fout.close();
	system("pause");
	
	return 0;
}
