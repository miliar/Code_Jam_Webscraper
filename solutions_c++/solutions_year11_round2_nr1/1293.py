#include <algorithm>  
#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <math.h>  
#include <list>  
#include <fstream>
using namespace std;  

#define fr(i,a,b) for(int i=(a);i<(b);++i)  

#define fi(b) for(int i=0;i<(b);++i)
#define fi2(a,b) for(int i=(a);i<(b);++i)  

#define fj(b) for(int j=0;j<(b);++j)  
#define fj2(a,b) for(int j=(a);j<(b);++j)  

#define fk(b) for(int k=0;k<(b);++k)  
#define fk2(a,b) for(int k=(a);k<(b);++k)  


#define pd(A) //(cout << #A << " : " << A << endl)

bool sub_solve(int c,istream &ins,ostream &outs)
	{
	cout << "case " << c << endl;

	int noteam;
	ins >> noteam;
	pd(noteam);

	int* r = new int[noteam*noteam];

	fi(noteam)
		{
		string s;
		ins >> s;
		pd(s);

		fj(noteam)
			{
			int n;
			if(s[j]=='.')
				n = -1;
			else if(s[j]=='1')
				n = 1;
			if(s[j]=='0')
				n = 0;
			r[i*noteam+j] = n;
			}

		}

	outs << "Case #" << c << ":" << endl;

	vector<double> wp(noteam,0);
	vector<double> owp(noteam,0);
	vector<double> oowp(noteam,0);

	fi(noteam)
		{
		int win = 0;
		int match = 0;
		fj(noteam)
			{
			if(r[i*noteam+j]==1)
				{
				win++;
				match++;
				}
			if(r[i*noteam+j]==0)
				{
				match++;
				}
			}
		if(match!=0)
			wp[i] = ((double)win)/match;
		}

	fi(noteam)
		{

		double sum = 0;
		int count = 0;

		fj(noteam)
		if(r[i*noteam+j]!=-1)
			{
			int win = 0;
			int match = 0;
			fk(noteam)
			if(k!=i)
				{
				if(r[j*noteam+k]==1)
					{
					win++;
					match++;
					}
				if(r[j*noteam+k]==0)
					{
					match++;
					}
				}

			if(match!=0)
				sum += ((double)win)/match;
			count++;
			}

		if(count!=0)
			owp[i] = ((double)sum)/count;
		
		}

	fi(noteam)
		{
		double sum = 0;
		int count = 0;

		fj(noteam)
		if(r[i*noteam+j]!=-1)
			{
			sum += owp[j];
			count++;
			}

		if(count!=0)
			oowp[i] = ((double)sum)/count;
		}

	fi(noteam)
		{
		double rpi = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
		outs.precision(12);
		outs << rpi << endl;
		}

	delete[] r;

	//return false;

	return true;
	}

void solve(istream &ins,ostream &outs)
	{
	int nC;
	ins >> nC;
	cout << "number of case : " << nC  << endl;
	fi(nC)
		if(!sub_solve(i+1,ins,outs))
			break;
	}

int main()
	{
	
	string input = "A-large.in";
	string output = "A-large.out";

	ifstream ins(input);
	ofstream outs(output);


	if(!ins.good())
		{
		cout << "can't open " << input << endl;
		return 1;
		}

	if(!outs.good())
		{
		cout << "can't open " << output << endl;
		return 1;
		}

	solve(ins,outs);

	ins.close();
	outs.close();

	return 0;
	}
