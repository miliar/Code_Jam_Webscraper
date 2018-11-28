#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>

char map[4][4]={0};
int countX=0, countO=0, countv=0;
	

char Analize(){
	char r='u';
	countX=0, countO=0;
	for(int i=0;i<4;i++)
	if( (map[0][i]==map[1][i] && map[0][i]==map[2][i] && map[0][i]==map[3][i] && map[0][i]!='.') ||
	 	(map[0][i]==map[1][i] && map[0][i]==map[2][i] && map[3][i]=='T' && map[0][i]!='.') ||
	 	(map[0][i]==map[1][i] && map[0][i]==map[3][i] && map[2][i]=='T' && map[0][i]!='.') ||
	 	(map[0][i]==map[2][i] && map[0][i]==map[3][i] && map[1][i]=='T' && map[0][i]!='.'))
		if(r!='u' && r!=map[0][i])
			return 'd';
		else
			r=map[0][i];
	else if ((map[1][i]==map[2][i] && map[1][i]==map[3][i] && map[0][i]=='T' && map[3][i]!='.'))
		if(r!='u' && r!=map[1][i])
			return 'd';
		else
			r=map[1][i];
	for(int i=0;i<4;i++)
	if( (map[i][0]==map[i][1] && map[i][0]==map[i][2] && map[i][0]==map[i][3] && map[i][0]!='.') ||
	 	(map[i][0]==map[i][1] && map[i][0]==map[i][2] && map[i][3]=='T' && map[0][0]!='.') ||
	 	(map[i][0]==map[i][1] && map[i][0]==map[i][3] && map[i][2]=='T' && map[0][0]!='.') ||
	 	(map[i][0]==map[i][2] && map[i][0]==map[i][3] && map[i][1]=='T' && map[0][0]!='.') )
		if(r!='u' && r!=map[i][0])
			return 'd';
		else
			r=map[i][0];
	else if ((map[i][1]==map[i][2] && map[i][1]==map[i][3] && map[i][0]=='T' && map[i][3]!='.'))
		if(r!='u' && r!=map[i][1])
			return 'd';
		else
			r=map[i][1];
	if( (map[0][0]==map[1][1] && map[0][0]==map[2][2] && map[0][0]==map[3][3] && map[0][0]!='.') ||
	 	(map[0][0]==map[1][1] && map[0][0]==map[2][2] && map[3][3]=='T' && map[0][0]!='.') ||
	 	(map[0][0]==map[1][1] && map[0][0]==map[3][3] && map[2][2]=='T' && map[0][0]!='.') ||
	 	(map[0][0]==map[2][2] && map[0][0]==map[3][3] && map[1][1]=='T' && map[0][0]!='.') )
		if(r!='u' && r!=map[0][0])
			return 'd';
		else
			r=map[0][0];
	else if ((map[1][1]==map[2][2] && map[1][1]==map[3][3] && map[0][0]=='T' && map[3][3]!='.'))
		if(r!='u' && r!=map[1][1])
			return 'd';
		else
			r=map[1][1];
	if( (map[0][3]==map[1][2] && map[0][3]==map[2][1] && map[0][3]==map[3][0] && map[0][3]!='.') ||
	 	(map[0][3]==map[1][2] && map[0][3]==map[2][1] && map[3][0]=='T' && map[0][3]!='.') ||
	 	(map[0][3]==map[1][2] && map[0][3]==map[3][0] && map[2][1]=='T' && map[0][3]!='.') ||
	 	(map[0][3]==map[2][1] && map[0][0]==map[3][0] && map[1][2]=='T' && map[0][3]!='.'))
		if(r!='u' && r!=map[0][3])
			return 'd';
		else
			r=map[0][3];
	else if ((map[2][1]==map[1][2] && map[2][1]==map[3][0] && map[0][3]=='T' && map[3][0]!='.'))
		if(r!='u' && r!=map[2][1])
			return 'd';
		else
			r=map[2][1];

	if(r!='u') return r;
	if(countv!=0) return 'u';
	return 'd';
}


int main(){
	int Testcases=0;
	char output='u';
	std::string line;

	std::ifstream ifs ( "test.in" , std::ifstream::in );
	std::ofstream ofs ( "test.out" , std::ifstream::out );

	ifs >> Testcases;
	std::getline( ifs, line);
	for ( int i=0; i<Testcases;++i ){
        countv=0;
		output='u';

		for(int j=0; j<4; ++j){
            for(int k=0; k<4;++k){
				ifs>>map[j][k];
				if(map[j][k]=='.')countv++;
			}
		}
		output=Analize();

		ofs<<"Case #"<<i+1<<": "<<((output=='d')?"Draw":(output=='u')?"Game has not completed":(output=='X')?"X won": "O won")<<std::endl;

	}

	ifs.close();
	ofs.close();

	//std::cin.get();
}
