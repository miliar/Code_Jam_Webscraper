#include <cstdio>
#include <vector>
#include <string>
#include <iostream>

using namespace std;

typedef struct Folder{

	string name;
	vector<Folder> subFolder;
}F;

F root;
int res;

void addPreFolder( string path , F &f ){

	if( path.size() == 0 )
		return;

	int i,k;
	for( i = 0 ; ; i ++ )
		if( path[i] == '/' )
			break;

	string target = path.substr( 0 , i );

	for( k = 0 ; k < f.subFolder.size() ; k ++ )
		if( f.subFolder[k].name == target )
			break;

	if( k == f.subFolder.size() ){
		Folder newFolder;
		newFolder.name = target;
		newFolder.subFolder.clear();
		f.subFolder.push_back( newFolder );
		addPreFolder( path.substr( i+1 ) , f.subFolder[k] );
	}
	else
		addPreFolder( path.substr( i+1 ) , f.subFolder[k] );

	return;
}

void addNewFolder( string path , F &f ){

	if( path.size() == 0 )
		return;

	int i,k;
	for( i = 0 ; ; i ++ )
		if( path[i] == '/' )
			break;

	string target = path.substr( 0 , i );

	for( k = 0 ; k < f.subFolder.size() ; k ++ )
		if( f.subFolder[k].name == target )
			break;

	if( k == f.subFolder.size() ){
		Folder newFolder;
		newFolder.name = target;
		newFolder.subFolder.clear();
		f.subFolder.push_back( newFolder );
		res++;
		addNewFolder( path.substr( i+1 ) , f.subFolder[k] );
	}
	else
		addNewFolder( path.substr( i+1 ) , f.subFolder[k] );

	return;
}

int main( void ){

	//freopen( "A-small-attempt0.in" , "r" , stdin );
	//freopen( "A-small-attempt0.out" , "w" , stdout );

	freopen( "A-large.in" , "r" , stdin );
	freopen( "A-large.out" , "w" , stdout );

	int cases;
	char enter;

	int n,m;

	cin>>cases;
	for( int testcases = 1 ; testcases <= cases ; testcases ++ ){

		cin>>n>>m;
		
		root.name = "root";
		root.subFolder.clear();
		string input;
		for( int i = 0 ; i < n ; i ++ ){
			cin>>input;
			//cout<<(input+"/").substr(1)<<endl;
			addPreFolder( (input+"/").substr(1) , root );
		}

		res = 0;
		for( int i = 0 ; i < m ; i ++ ){
			cin>>input;
			//cout<<input<<endl;
			addNewFolder( (input+"/").substr(1) , root );
		}

		cout<<"Case #"<<testcases<<": "<<res<<endl;
	}

	return 0;
}
