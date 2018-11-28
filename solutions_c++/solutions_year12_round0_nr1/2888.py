#include <fstream>
#include <string>
#include <iostream>

const char DECODE_MAP[]="yhesocvxduiglbkrztnwjpfmaq";
const int  MAX_LEN	= 100+1;
std::string decodeGooglerese(std::string& code)
{
	char decode[MAX_LEN];
	const char* charCode= code.c_str();
	const int	len		= code.length();
	for(int i=0;i<len;++i){
		int idx = charCode[i] -'a'; 
		if(0 <= idx && idx < 26){
			decode[i]	= DECODE_MAP[idx];
		}else{
			decode[i]	= ' ';
		}
	}
	decode[len]=0;
	return std::string(decode);
}


int main(int argc, char**argv)
{
	if(argc<2)		return -1;
	std::ifstream	ifs(argv[1]);
	if(ifs==NULL)	return -1;

	std::string		buf;
	getline	(ifs, buf);
	const int maxCount	=atoi(buf.c_str());
	std::ofstream ofs( "out.txt" );

	int count	=	0;
	while(getline(ifs, buf)) {
		ofs			<< "Case #" 
					<< (++count) 
					<< ": "
					<< decodeGooglerese(buf) 
					<< std::endl;
	}
	return 0;
}