#include <string>
#include <iostream>

static std::string from;
static std::string to;

void resolveLanguage(const std::string& in, const std::string& out){
	for ( std::size_t i = 0; i<in.length() && i<out.length(); ++i ){
		if ( from.find(in.at(i)) != std::string::npos )
			continue;

		from += in.at(i);
		to += out.at(i);
	}
}

std::string translate(const std::string& in){
	std::string out;
	out.reserve(in.length());

	for ( std::size_t i=0; i<in.length(); ++i ){
		std::size_t pos = from.find(in.at(i));
		if ( pos == std::string::npos )
			out += in.at(i);
		else
			out += to.at(pos);
	}

	return out;
}

int main(){
	resolveLanguage("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand");
	resolveLanguage("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities");
	resolveLanguage("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up");
	resolveLanguage("zq", "qz");

	int lineCount;
	std::cin >> lineCount;

	std::string line;
	std::getline(std::cin, line);

	for ( int i=1; i<=lineCount; ++i ){
		if ( !std::cin.good() )
			break;

		std::string line;
		std::getline(std::cin, line);

		std::cout << "Case #" << i << ": " << translate(line) << std::endl;
	}

	return 0;
}
