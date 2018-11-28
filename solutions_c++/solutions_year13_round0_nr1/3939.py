#include<iostream>
#include<fstream>
#include<string>

using namespace std;
bool c_d(char a , char b , char c , char d) {
	bool result = 0;
	if( a == '.' || b == '.' || c == '.' || d == '.' )
		result = 1;
	return result;
	}


bool cc( char a , char B , char c , char d)
{
	bool result = 0;
if ( (a != '.') && (B != '.') && (c != '.') && (d != '.') ){
	if( a == B && B == c && c == d )
		result = 1;
	else if( a == 'T' ) {
		if( B == c && c == d )
			result = 1;
		}
	else if( B == 'T' ) {
		if( a == c && c == d )
			result = 1;
		}
	else if( c == 'T' ) {
		if( a == B && B == d )
			result = 1;
		}
	else if( d == 'T' ) {
		if( a == B && B == c )
			result = 1;
		}
}
else
	result = 0;

return result;
}

int main(){
	
	ifstream input("input");
	ofstream output("output");
	//input.open("input");
	string s,out;
	//getline(input,s);
	//cout<<s<<endl;
	//output<<s<<endl;
	int tours;
	input>>tours;
	char x[4][4];
	for(int i=1;i<=tours;i++) {
		input>>x[0][0]>>x[0][1]>>x[0][2]>>x[0][3];
		input>>x[1][0]>>x[1][1]>>x[1][2]>>x[1][3];
		input>>x[2][0]>>x[2][1]>>x[2][2]>>x[2][3];
		input>>x[3][0]>>x[3][1]>>x[3][2]>>x[3][3];
		getline(input,s);
		
		//check rows
		if(cc(x[0][0],x[0][1],x[0][2],x[0][3]))
		{ if(x[0][0]=='T') out = x[0][1]; else out = x[0][0]; output<<"Case #"<<i<<": "<<out<<" won"<<endl; }
		else if(cc(x[1][0],x[1][1],x[1][2],x[1][3]))
		{ if(x[1][0]=='T') out = x[1][1]; else out = x[1][0]; output<<"Case #"<<i<<": "<<out<<" won"<<endl; }
		else if(cc(x[2][0],x[2][1],x[2][2],x[2][3]))
		{ if(x[2][0]=='T') out = x[2][1]; else out = x[2][0]; output<<"Case #"<<i<<": "<<out<<" won"<<endl; }
		else if(cc(x[3][0],x[3][1],x[3][2],x[3][3]))
		{ if(x[3][0]=='T') out = x[3][1]; else out = x[3][0]; output<<"Case #"<<i<<": "<<out<<" won"<<endl; }
		// check columns
		else if(cc(x[0][0],x[1][0],x[2][0],x[3][0]))
		{ if(x[0][0]=='T') out = x[1][0]; else out = x[0][0]; output<<"Case #"<<i<<": "<<out<<" won"<<endl; }
		else if(cc(x[0][1],x[1][1],x[2][1],x[3][1]))
		{ if(x[0][1]=='T') out = x[1][1]; else out = x[0][1]; output<<"Case #"<<i<<": "<<out<<" won"<<endl; }
		else if(cc(x[0][2],x[1][2],x[2][2],x[3][2]))
		{ if(x[0][2]=='T') out = x[1][2]; else out = x[0][2]; output<<"Case #"<<i<<": "<<out<<" won"<<endl; }
		else if(cc(x[0][3],x[1][3],x[2][3],x[3][3]))
		{ if(x[0][3]=='T') out = x[1][3]; else out = x[0][3]; output<<"Case #"<<i<<": "<<out<<" won"<<endl; }
		// check diameters
		else if(cc(x[0][0],x[1][1],x[2][2],x[3][3]))
		{ if(x[0][0]=='T') out = x[1][1]; else out = x[0][0]; output<<"Case #"<<i<<": "<<out<<" won"<<endl; }
		else if(cc(x[3][0],x[2][1],x[1][2],x[0][3]))
		{ if(x[3][0]=='T') out = x[2][1]; else out = x[3][0]; output<<"Case #"<<i<<": "<<out<<" won"<<endl; }
		// not completed
		else if(c_d(x[0][0],x[0][1],x[0][2],x[0][3]) || c_d(x[1][0],x[1][1],x[1][2],x[1][3]) || c_d(x[2][0],x[2][1],x[2][2],x[2][3]) || c_d(x[3][0],x[3][1],x[3][2],x[3][3]))
		{ output<<"Case #"<<i<<": "<<"Game has not completed"<<endl; }
		// draw
		else
		{ output<<"Case #"<<i<<": "<<"Draw"<<endl; }
	}
	return 0;
	
}
