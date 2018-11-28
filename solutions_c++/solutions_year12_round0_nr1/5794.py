#include <iostream>
#include <fstream>
#include <string>

#define PATHIN "A-small-attempt1.in"
#define PATHOUT "A-small-attempt1.out"

using namespace std;


string g2e(string from){
	char alpha[26]={'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};
	int minus = 97;
	
	for(int i=0 ; i<from.length() ; i++){
		if(from[i]==' ')
			continue;
		
		int pos;
		for(int j=0 ; j<13 ; j++){
			if(from[i]==alpha[j])
				pos=j;
			if(from[i]==alpha[25-j])
				pos=25-j;
		}

		from[i]=(char)(pos+97);
	}

	return from;
}


void main(){
	fstream FILEIN(PATHIN);
	fstream FILEOUT(PATHOUT);

	int count;
	char input[101];

	FILEIN>>count;
	FILEIN.getline(input,1);
	for(int i=0 ; i<count ; i++){
		FILEIN.getline(input,101);

		FILEOUT<<"Case #"<<i+1<<": ";
		FILEOUT<<g2e(input)<<endl;

		//cout<<"Case #"<<i+1<<": ";
		//cout<<g2e(input)<<endl;
	}
}