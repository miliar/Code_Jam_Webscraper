#include<stdio.h>
#include<stdlib.h>
#include<memory.h>
#include<string.h>
#include<math.h>
#include<vector>
#include<iostream>
#include<sstream>
#include<fstream>
#include<algorithm>
#include <math.h>


using namespace std;

const double eps=1e-8;
const int leftEdge=0;
const int rightEdge=100;

struct point
{
  double x;
  double y;
};

struct line
{
  point a;
  point b;
};

vector<point> crossPts;
vector<line> lines;

int min(int a, int b)
{
  return (a<=b)?a:b;
}

int max(int a, int b)
{
  return (a>=b)?a:b;
}

bool zero(double x) 
{
 return (x>0?x:-x)<eps;
}

bool parallel(line u,line v){
	return zero((u.a.x-u.b.x)*(v.a.y-v.b.y)-(v.a.x-v.b.x)*(u.a.y-u.b.y));
}

point intersection(line u,line v){
	point ret=u.a;
	double t=((u.a.x-v.a.x)*(v.a.y-v.b.y)-(u.a.y-v.a.y)*(v.a.x-v.b.x))
			/((u.a.x-u.b.x)*(v.a.y-v.b.y)-(u.a.y-u.b.y)*(v.a.x-v.b.x));
	ret.x+=(u.b.x-u.a.x)*t;
	ret.y+=(u.b.y-u.a.y)*t;
	return ret;
}

bool CompareCoordinates (point p1, point p2 )
{ // compare by x first; for ties, compare by y
/*	if (fabs(p1.x, p2.x)<1e-5)
	{
		if (fabs(p1.y, p2.y)<1e-5)
		{	
			return true;
		}
		else if (p1.y<p2.y)
			return true;
	}
*/	
	if (p1.x<p2.x)
		return true;
	else 
		return false;
}

void DecomposeLine(vector<string> & Elements, string OrgnString, string
		   strSeparator)
{
  string Separator = strSeparator;//separator between elements
  
  Elements.clear();//clear element array
  
  //get separator positions, ","
  vector<int> SeparatorPos;
  string::size_type pos = 0;
  
  while(pos <= OrgnString.size())
    {
      pos=OrgnString.find_first_of(Separator,(pos+1));
      
      SeparatorPos.push_back(pos);
    }
  SeparatorPos.pop_back();
  
  if (SeparatorPos.size()==0)
    {
      Elements.push_back(OrgnString);
      return;
    }
  
  Elements.push_back(OrgnString.substr(0,SeparatorPos[0]));
  //abstract element from whole string
  for(int i=0; i<SeparatorPos.size(); i++)
    {
      Elements.push_back(OrgnString.substr((SeparatorPos[i]+1),(SeparatorPos[i+1]-SeparatorPos[i])-1));
    }
  
}

int main(int argc, char *argv[])
{
  int i=0,j=0,m=0, n=0, k=0, p=0;
  int T=0, N=0, M=0;


  ifstream infile;
  ofstream outfile;
  stringstream item[2];
  vector<string> Elements;
  
  string inputFileName=string(argv[1])+".in";
  string outputFileName=string(argv[1])+".out";
  outfile.open(outputFileName.c_str());	
  infile.open(inputFileName.c_str());
  if(!infile)
    {
      cout<<"File open problem";
      return 0;
    }
 
  infile.seekg(0,ios_base::beg);

  string tempstr, tempstr2;

  //proc first line
  getline(infile,tempstr);
  item[0]<<tempstr;
  item[0]>>T;
  cout<<"T="<<T<<endl;
  for(i=1; i<=T; i++)
    {
      cout<<"i="<<i<<endl;
      Elements.clear();
      item[0].clear();
      //item[1].clear();

      getline(infile, tempstr);
      DecomposeLine(Elements, tempstr, " ");
  
      item[0]<<Elements[0].c_str();
      item[0]>>N;
      //item[1]<<Elements[1].c_str();
      //item[1]>>M;
      lines.resize(N);
 
      for (j=0; j<N; j++)
	{
          int leftPt, rightPt;
	  item[0].clear();
	  item[1].clear();
	  
	  getline(infile, tempstr);
	  DecomposeLine(Elements, tempstr, " ");
	  
	  item[0]<<Elements[0].c_str();
	  item[0]>>leftPt;
	  item[1]<<Elements[1].c_str();
	  item[1]>>rightPt;
	  
	  lines[j].a.x=leftEdge;
          lines[j].a.y=leftPt;
          lines[j].b.x=rightEdge;
          lines[j].b.y=rightPt;
	}

      //for debug
      for (j=0; j<N; j++)
	{
	  cout<<"line"<<j<<": ("<<lines[j].a.x<<", "<<lines[j].a.y<<") ("<<lines[j].b.x<<", "<<lines[j].b.y<<")"<<endl;
	  
	}
      
      int numCrossPts=0;
      for (j=0; j<N; j++)
	{
	  for (k=j+1; k<N; k++)
	    {
	      point tmpCrossPt;

	      if (!parallel(lines[j], lines[k]))
                {
		  tmpCrossPt=intersection(lines[j], lines[k]);
		  if ((tmpCrossPt.x>=leftEdge)&&(tmpCrossPt.x<=rightEdge)&&(tmpCrossPt.y>=min(lines[j].a.y, lines[j].b.y))&&(tmpCrossPt.y<=max(lines[j].a.y, lines[j].b.y))&&(tmpCrossPt.y>=min(lines[k].a.y, lines[k].b.y))&&(tmpCrossPt.y<=max(lines[k].a.y, lines[k].b.y)))
		    {
		      crossPts.push_back(tmpCrossPt);
		      numCrossPts++;
		      cout<<"not parallel!"<<j<<", "<<k<<" crossPt=("<<tmpCrossPt.x<<","<<tmpCrossPt.y<<")"<<endl;
		    }
		}
	    }//for k
	  

	  
	}//for j
	  outfile<<"Case #"<<i<<": "<<numCrossPts<<endl;
    } //for i
  
  infile.close();
  outfile.close();
  
  return 0;
  
}

