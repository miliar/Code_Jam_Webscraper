#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <queue>
#include <deque>
#include <math.h>
using namespace std;

char *infilepath = "C:\\Users\\cyzhao\\Desktop\\code jam\\Round2_4\\D-small-attempt3.in";
char *outfilepath = "C:\\Users\\cyzhao\\Desktop\\code jam\\Round2_4\\out.txt";

class Circle
{
public:
    double x,y,r;
    Circle()
    {
        x = 0;
        y = 0;
        r = 0;
    }     
    
    void Set(double x, double y, double r)
    {
        this->x = x;
        this->y = y;
        this->r = r;
    }    
};    

double dist(Circle c1, Circle c2)
{
    return sqrt((c1.x - c2.x) *(c1.x - c2.x) + (c1.y - c2.y) *(c1.y - c2.y));
}   

double max2(double x, double y)
{
    return (x < y)?y:x;
}     

double Calc(Circle *plants, int N)
{
    if(N == 1)
    {
        return plants[0].r;
    }
    else if(N == 2)
    {
        return max2(plants[0].r, plants[1].r);
    }else if(N == 3)
    {
        double dist1 = max2(dist(plants[0], plants[1]) + plants[0].r + plants[1].r, plants[2].r);
        double dist2 = max2(dist(plants[0], plants[2]) + plants[0].r + plants[2].r, plants[1].r);
        double dist3 = max2(dist(plants[1], plants[2]) + plants[1].r + plants[2].r, plants[0].r);
        if(dist1 <= dist2 && dist1 <= dist3)
        {
            return dist1 / 2;
        }    
        if(dist2 <= dist1 && dist2 <= dist3)
        {
            return dist2 / 2;
        }  
        if(dist3 <= dist2 && dist3 <= dist1)
        {
            return dist3 / 2;
        }  
    }    
    
    return 0;
}    

int main()
{
	ifstream infile(infilepath);
	if(!infile)
	{
		cerr<<"File could not be open"<<endl;
		abort();
	}

	ofstream outfile;
	outfile.open(outfilepath, ios::out);
	if(!outfile)
	{
		cerr<<"File could not be open"<<'\n';
		abort();
	}
	int C, N;
	Circle *plants;
	infile>>C;
	for(int i = 0; i < C; i++)
	{
       infile>>N;
       plants = new Circle[N];
       int x, y, z;
       for(int j = 0; j < N; j++)
       {
           infile>>x>>y>>z;
           plants[j].Set(x,y,z);
       }     
       double r = Calc(plants, N);
       outfile<<setiosflags(ios::fixed)<<setprecision(6)<<"Case #"<<i + 1<<": "<<r<<endl;
       delete[] plants;
	}    

	infile.close();
	outfile.close();
}
