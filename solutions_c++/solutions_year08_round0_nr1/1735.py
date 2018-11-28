#ifndef __IOSTREAM__ 
#define __IOSTREAM__
#include <iostream>
#include <fstream>
#include <Vector>
#endif

using namespace std;

bool notin( vector<string> temp, string query ) {
	for ( int i=0;i<temp.size();i++ ) {
		if ( temp[i].compare(query)==0 ) {
			return false;
		}
	}
	return true;
}

int findnum( vector<string> engines, vector<string> querys, int n ) {

	vector<string> temp;
	int i = 1;
	int m = 1;
	temp.push_back( querys[n] );

	while ( i < engines.size() ) {
		if ( n+m==querys.size() ) return 0;
		if ( notin( temp, querys[n+m] ) ) {
			temp.push_back( querys[n+m] );
			m++;
			i++;
		} else {
			m++;
		}
	}
	/*
	if ( engines.size() == 2 ) {
		m++;
		if ( n+m==querys.size() ) return 0;
		while ( querys[n].compare(querys[n+m])==0 ) {
			m++;
			if ( n+m==querys.size() ) return 0;
		}
		m--;

	} else {

		while ( i < engines.size()-1 ) {
			m++;
			if ( n+m==querys.size() ) return 0;
			if ( notin( temp, querys[n+m] ) ) {
				temp.push_back( querys[n+m] );
				i++;
			}
		}
	}
	*/

	return n+m-1;
/*
	for ( int i=1; i<engines.size()-1; i++ ) {
		temp.push_back( querys[n+i] );
		if ( querys[n+i], 

	}
	*/
}

void main(){
	
	//path of line.txt
	char filename[100]="A-small-attempt5.in";
	int n;
	int num;
	int temp;
	int flag;

	ifstream file(filename,ios::in);
	if(file.fail()){
		cout<<"Can't open the \"A-small-attempt5.in\""<<endl; 
		file.close();
		system("pause");
		exit(0);
	} 
	ofstream ouputfile("output.txt",ios::out);


	file>>n;
	vector<string> engines;
	vector<string> querys;
	string stemp;
	char engine[100] = "";
	char query[100] = "";

	for ( int casenum = 0; casenum < n; casenum++ ) {
		engines.clear();
		querys.clear();
		file>>temp;
		file.getline(engine,100,'\n');
		for ( int enginesnum = 0; enginesnum < temp; enginesnum++ ) {
			file.getline(engine,100,'\n');
			stemp = engine;
			engines.push_back(stemp);
		}
		file>>temp;
		file.getline(query,100,'\n');
		for ( int querysnum = 0; querysnum < temp; querysnum++ ) {
			file.getline(query,100,'\n');
			stemp = query;
			querys.push_back(stemp);
		}

		if ( querys.size() == 0 ) {
			ouputfile<<"Case #"<<casenum+1<<": 0"<<endl;
		} else {

			flag = -1;
			num=0;
			do {
				num = findnum( engines, querys, num);
				flag++;
			}
			while( num>0 );
			ouputfile<<"Case #"<<casenum+1<<": "<<flag<<endl;
		}
	}
	ouputfile.close();
	file.close();
}

/*
int findnum( vector<string> engines, vector<string> querys, int *n ) {
	
	int i,j,flag,temp = 0;
	int num;

	for ( i = 0; i < engines.size(); i++ ) {
		for ( j = 0; j < querys.size(); j++ ) {
			if ( strcmp( querys[j], engines[i])=0 ) {
				temp++;
			}
		}
		if ( i=0 || temp<flag ) {
			flag = temp;
			num = i;
		}
	}
	
	temp = 0;
	if ( flag > 0 ) {
		for ( j = 0; j < querys.size(); j++ ) {
			if ( strcmp( querys[j], engines[num])=0 ) {
				temp++;
				if ( temp = 2 ) *n=j;
			}
		}
	}
	
	return flag;
}
*/
