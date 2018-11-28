#include <fstream>
#include <ax/ax_core.h> //libax.googlecode.com

std::ifstream	inFile;
axFile			outFile;

typedef	axArray< axArray<int, 100>, 100 >	Lawn;

axStatus	output( int c, char result ) {
	axStringA_<256>	tmp;
	
	tmp.format("Case #{?}: ", c+1 );
	
	switch( result ) {
		case 'X': tmp.append("X won");	break;
		case 'O': tmp.append("O won");	break;
		case 'D': tmp.append("Draw");	break;
		case '.': tmp.append("Game has not completed");	break;
		default:
			assert( false );
	}
	
	tmp.append("\n");
	
	outFile.writeString( tmp );
	ax_print( tmp );

	return 0;
}

class Data {
public:
	int X, O, T;
	Data() {
		X = 0;
		O = 0;
		T = 0;
	}
	
	void process( char ch ) {
		switch( ch ) {
			case 'X': X++; break;
			case 'O': O++; break;
			case 'T': T++; break;
		}
	}
	
	bool checkWinner( int c ) {
		if( X+T >= 4 ) { output( c, 'X' ); return true; }
		if( O+T >= 4 ) { output( c, 'O' ); return true; }
		return false;
	}
	
};

axStatus	doCase( int c ) {
	axStringA	buf;

	char	a[4][4];
	
	int		nDot = 0;
	
	for( int n=0; n<4; n++ ) {
		for( int m=0; m<4; m++ ) {
			inFile >> a[n][m];
			if( a[n][m] == '.' ) nDot++;
		}
	}

//--- row check
	for( int n=0; n<4; n++ ) {
		Data	data;
		for( int m=0; m<4; m++ ) {
			data.process( a[n][m] );
		}
		if( data.checkWinner(c) ) return 0;
	}
	
//--- col check
	for( int n=0; n<4; n++ ) {
		Data	data;
		for( int m=0; m<4; m++ ) {
			data.process( a[m][n] );
		}
		if( data.checkWinner(c) ) return 0;
	}
	
//---- diagonal chcek
	{
		Data	data;
		for( int m=0; m<4; m++ ) {
			data.process( a[m][m] );
		}
		if( data.checkWinner(c) ) return 0;
	}

	{
		Data	data;
		for( int m=0; m<4; m++ ) {
			data.process( a[m][3-m] );
		}
		if( data.checkWinner(c) ) return 0;
	}
	
	if( nDot == 0 ) {
		output( c, 'D' );
	}else{
		output( c, '.' );
	}
	
	return 0;
}

axStatus	run() {
	axStatus	st;
		
	inFile.open("A-large.in");
	if( ! inFile.is_open() ) return -1;
	
	st = outFile.openWrite("out.txt", true, true);		if( !st ) return st;

	axStringA	buf;
	int C;
	inFile >> C;
	for( int c=0; c<C; c++ ) {
		st = doCase( c );			if( !st ) return st;
	}



	return 0;
}


axStatus	changeDir() {
	axStatus st;
	axStringA path;
	st = axFilePath::getDirName(path, __FILE__ );		if( !st ) return st;
	st = axFileSystem::setCurrentDir(path);				if( !st ) return st;
	return 0;
}


int main(int argc, const char * argv[]) {
	axScope_NSAutoreleasePool	pool;

	changeDir();

	axStatus st = run();
	ax_log("===== end of program - return {?} =====", st );

    return 0;
}

