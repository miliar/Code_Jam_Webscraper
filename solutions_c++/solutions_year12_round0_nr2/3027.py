#include <fstream>
#include <string>
#include <iostream>
#include <sstream>

// ti  to MAX table.
const int MAX_TABLE[31][2]=	{	//{normal max,	sup max}
									{0,	0}, //0 is ti 
									{1,	1},	//1
									{1,	2},	//2
									{1,	2},	//3
									{2,	2},	//4
									{2,	3},	//5
									{2,	3},	//6
									{3,	3},	//7
									{3,	4},	//8
									{3,	4},	//9
									{4,	4},	//10
									{4,	5},	//11
									{4,	5},	//12
									{5,	5},	//13
									{5,	6},	//14
									{5,	6},	//15
									{6,	6},	//16
									{6,	7},	//17
									{6,	7},	//18
									{7,	7},	//19
									{7,	8},	//20
									{7,	8},	//21
									{8,	8},	//22
									{8,	9},	//23
									{8,	9},	//24
									{9,	9},	//25
									{9,	10},//26
									{9,	10},//27
									{10,10},//28
									{10,10},//29
									{10,10}	//30
							};



int resolveB(std::string& code)
{
	
	std::istringstream  istr(code.data());
	int N, S, P;
	istr>>N;
	istr>>S;
	istr>>P;

	int count=0;
	for(int i=0;i<N;++i){
		int Ti;
		istr>>Ti;
		if		(MAX_TABLE[Ti][0] >= P){
			count++;
		}else if(MAX_TABLE[Ti][1] >= P && S > 0){
			count++;
			S--;
		}
	}

	return count;
}


int main(int argc, char**argv)
{
	if(argc<2)		return -1;
	std::ifstream	ifs(argv[1]);
	if(ifs==NULL)	return -1;

	std::string		buf;
	getline	(ifs, buf);
	const int T		= atoi(buf.c_str());
	std::ofstream ofs(  "B-large.out" );

	int count	=	0;
	while(getline(ifs, buf)) {
		ofs			<< "Case #" 
					<< (++count) 
					<< ": "
					<< resolveB(buf) 
					<< std::endl;
	}
	return 0;
}