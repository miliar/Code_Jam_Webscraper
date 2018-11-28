#include <fstream>
#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>

std::string long2string(const  long longval)
{
	char buf[256];
	sprintf_s(buf,"%ld",longval);
	return std::string(buf);
}

std::string mergeString(const long value, const int maxDigit)
{
	std::string merge;
	merge	=long2string(value);
	int lengthDiff = maxDigit -merge.length();
	while(lengthDiff-- > 0){
		merge = "0"+merge;
	}
	merge = merge+merge;
	return merge;
}

inline
int recycleValue(std::string& mergeStr, const int shift,const int maxDigit)
{
	long value;
	std::string substr= mergeStr.substr(shift,maxDigit);
	std::istringstream  istr(substr.data());
	istr	>> value;
	return  value;
}

int resolveC(std::string& code)
{
	std::istringstream  istr(code.data());
	long lA, lB;
	std::string  sB;
	istr	>> lA;
	istr	>> lB;
	sB		= long2string(lB);

	const int maxDigit =  sB.length();
	int count=0;
	for(long i=lA; i<=lB; ++i){
		std::vector<long> input_table;
		std::string mergeVal	= mergeString(i,maxDigit);
		for(int shift=1;shift < maxDigit;++shift){
			long value	=	recycleValue(mergeVal,shift,maxDigit);

			std::vector<long>::iterator itr		= std::find( input_table.begin(), input_table.end(), value );
			if(i < value && value <=lB && itr == input_table.end() ){
				input_table.push_back(value);
				count++;
			}
		}
	}
	return count;
}



std::string splitPath(std::string path){
	path[path.find_last_of('.')]=' ';
	std::stringstream	strm(path);
	std::string			dstName;
	strm >> dstName;
	return dstName;
}

int main(int argc, char**argv)
{
	if(argc<2)		return -1;
	std::ifstream	ifs(argv[1]);
	if(ifs==NULL)	return -1;

	std::string		buf;
	getline	(ifs, buf);
	const int T		= atoi(buf.c_str());

	std::string outName = splitPath(argv[1]) + ".out";
	std::ofstream ofs( outName );

	int count	=	0;
	while(getline(ifs, buf)) {
		ofs			<< "Case #" 
					<< (++count) 
					<< ": "
					<< resolveC(buf) 
					<< std::endl;
	}
	return 0;
}