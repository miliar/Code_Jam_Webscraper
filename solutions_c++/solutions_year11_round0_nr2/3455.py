#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>

using std::cerr;

class MagickaCase
{
	std::vector<char> elemList;
	typedef std::set<char> elem_set;
	typedef std::map<char, elem_set> elem_to_set;
	elem_to_set opposedElemMap;
	typedef std::pair<char, char> elemPair;
	typedef std::map<elemPair, char> pair_to_elem;
	pair_to_elem combiningElemMap;
public:
	void AddCombine(char base1, char base2, char combined);
	void AddOpposed(char elem1, char elem2);
	void Invoke(char elem);
	void Print(std::ostream& stream) const;
private:
	bool Combine(char elem);
	bool HasOpposed(char elem) const;
	void ClearList()
	{
		elemList.clear();
	}
	void AddElem(char elem)
	{
		elemList.push_back(elem);
	}

	// validation functions
	static bool ElemInSet(char elem, const elem_set&);
	static bool IsBase(char e)
	{
		return e=='Q' || e=='W' || e=='E' || e=='R'
			|| e=='A' || e=='S' || e=='D'  || e=='F';
	}
	static bool IsNonBase(char e)
	{
		return e>='A' && e<='Z' && !IsBase(e);
	}
	void ValidateBase(char e)
	{
		if(!IsBase(e))
			std::cerr<<"Expected base element, got '"<<e<<"'\n";
	}
	void ValidateNonBase(char e)
	{
		if(!IsNonBase(e))
			std::cerr<<"Expected non-base element, got '"<<e<<"'\n";
	}
};

void MagickaCase::AddCombine(char base1, char base2, char combined)
{
	ValidateBase(base1);
	ValidateBase(base2);
	ValidateNonBase(combined);
	if(!combiningElemMap.insert(pair_to_elem::value_type(elemPair(base1, base2), combined)).second ||
		(base1!=base2 && !combiningElemMap.insert(pair_to_elem::value_type(elemPair(base2, base1), combined)).second))
	{
		cerr<<"Multiple combine definitions for pair "<<base1<<","<<base2<<std::endl;
	}
}

void MagickaCase::AddOpposed(char elem1, char elem2)
{
	ValidateBase(elem1);
	ValidateBase(elem2);
	if(!opposedElemMap[elem1].insert(elem2).second ||
		(elem1!=elem2 && !opposedElemMap[elem2].insert(elem1).second))
	{
		cerr<<"Multiple opposed definitions for pair "<<elem1<<","<<elem2<<std::endl;
	}
}

void MagickaCase::Invoke(char elem)
{
	ValidateBase(elem);
	if(!Combine(elem))
	{
		if(HasOpposed(elem))
		{
			ClearList();
		}
		else
		{
			AddElem(elem);
		}
	}
}

bool MagickaCase::Combine(char elem)
{
	if(elemList.empty())
	{
		return false;
	}
	char& last=elemList.back();
	pair_to_elem::iterator res = combiningElemMap.find(elemPair(elem, last));
	if(res==combiningElemMap.end())
	{
		return false;
	}
	else
	{
		last = res->second;
		return true;
	}
}

bool MagickaCase::HasOpposed(char elem) const
{
	elem_to_set::const_iterator it = opposedElemMap.find(elem);
	if(it==opposedElemMap.end())
	{
		return false;
	}
	const elem_set& opposedElems=it->second;
	return std::find_if(elemList.begin(), elemList.end(), 
		std::bind2nd(std::ptr_fun(MagickaCase::ElemInSet), opposedElems))
		!=elemList.end();
}

bool MagickaCase::ElemInSet(char elem, const elem_set& s)
{
	return s.find(elem) != s.end();
}

void MagickaCase::Print(std::ostream& stream) const
{
	if(!elemList.empty())
	{
		std::vector<char>::const_iterator it=elemList.begin();
		stream<<*it;
		for(++it; it!=elemList.end(); ++it)
		{
			stream<<", "<<*it;
		}
	}
}

void ProcessFiles(const char* in_fname, const char* out_fname)
{
	std::ifstream in;
	std::ofstream out;
	using std::ios_base;
	in.exceptions(ios_base::failbit|ios_base::badbit);
	in.open(in_fname);
	out.open(out_fname);
	int numCases;
	in >> numCases;
	cerr<<"Processing "<<numCases<<" cases\n";
	for(int caseNum=1; caseNum<=numCases; ++caseNum)
	{
		MagickaCase thiscase;
		int combines;
		in>>combines;
		std::streamsize old_width=in.width(4);
		for(int i=0; i<combines; ++i)
		{
			char elems[4];
			in>>elems;
			if(strlen(elems)!=3)
			{
				std::cerr<<"Expected 3 elements for combine, got "<<strlen(elems)<<std::endl;
			}
			else
			{
				thiscase.AddCombine(elems[0], elems[1], elems[2]);
			}
		}
		in.width(old_width);
		int opposed;
		in>>opposed;
		in.width(3);
		for(int i=0; i<opposed; ++i)
		{
			char elems[3];
			in>>elems;
			if(strlen(elems)!=2)
			{
				std::cerr<<"Expected 2 elements, got "<<strlen(elems)<<std::endl;
			}
			else
			{
				thiscase.AddOpposed(elems[0], elems[1]);
			}
		}
		in.width(old_width);
		int invokes;
		in>>invokes;
		in>> std::ws;
		for(int i=0; i<invokes; ++i)
		{
			char elem = in.get();
			if(in.eof())
			{
				cerr<<"Failed to read expected element to invoke: unexpected end of file\n";
				break;
			}
			else
			{
				thiscase.Invoke(elem);
			}
		}
		out<<"Case #"<<caseNum<<": [";
		thiscase.Print(out);
		out<<"]\n";
	}
	in >> std::ws;
	if(!in.eof())
	{
		cerr<<"Unexpected trailing characters in input file\n";
	}
}

int main(int argc, char* argv[])
{
	if(argc!=3)
	{
		cerr<<"Usage: magicka <infile> <outfile>\n";
		return 1;
	}
	try
	{
	    ProcessFiles(argv[1], argv[2]);
	}
	catch(std::exception& e)
	{
		cerr<<"Error: "<<e.what()<<"\n";
		return 1;
	}
	return 0;
}