#include<iostream>
#include<fstream>
#include<cassert>

using std::cerr;

bool possible(long long N, long long Pd, long long Pg)
{
	assert(N>=0);
	assert(Pd>=0);
	assert(Pd<=100);
	assert(Pg>=0);
	assert(Pg<=100);
	if(Pg==0)
	{
		return Pd==0;
	}
	else if(Pg==100)
	{
		return Pd==100;
	}
	else if(Pd==100)
	{
		return true;
	}
	else if(Pd==50)
	{
		return N>=2;
	}
	else if((Pd%25)==0)
	{
		return N>=4;
	}
	else if((Pd%20)==0)
	{
		return N>=5;
	}
	else if((Pd%10)==0)
	{
		return N>=10;
	}
	else if((Pd%5)==0)
	{
		return N>=20;
	}
	else if((Pd%4)==0)
	{
		return N>=25;
	}
	else if((Pd%2)==0)
	{
		return N>=50;
	}
	else
	{
		return N>=100;
	}
}

bool get_result(std::istream &in)
{
	long long N, Pd, Pg;
	in>>N>>Pd>>Pg;
	cerr<<"{"<<N<<","<<Pd<<","<<Pg<<"}\n";
	return possible(N, Pd, Pg);
}

void print_result(long long caseNum, bool result, std::ostream &out)
{
	out<<"Case #"<<caseNum<<": ";
	if(result)
	{
		out<<"Possible\n";
	}
	else
	{
		out<<"Broken\n";
	}
}

int main(int argc, char* argv[])
{
	if(argc!=3)
	{
		cerr<<"Usage: freecell_stats <infile> <outfile>\n";
		return 1;
	}
	try
	{
	    std::ifstream in(argv[1]);
		if(!in.good())
		{
			cerr<<"Could not open infile\n";
			return 1;
		}
		std::ofstream out(argv[2]);
		if(!out.good())
		{
			cerr<<"Could not open outfile\n";
			return 1;
		}
		in.exceptions(std::ios_base::failbit|std::ios_base::badbit);
		out.exceptions(std::ios_base::failbit|std::ios_base::badbit);
		long long numCases;
		in>>numCases;
		for(long long caseNum=1; caseNum<=numCases; ++caseNum)
		{
			print_result(caseNum,get_result(in),out);
		}
		in>>std::ws;
		if(!in.eof())
		{
			cerr<<"Unexpected training content in file\n";
		}
	}
	catch(std::exception& e)
	{
		cerr<<"Error: "<<e.what()<<"\n";
		return 1;
	}
	return 0;
}