#include <fstream>
#include <vector>
#include <utility>
using namespace std;

ifstream in;

struct command{
	int who;
	int pos;
	int time;
};

int sign1( int a ){
	if( a>0 )
		return a;
	else
		return 0;
}

int solve(){
	int n;
	in>>n;
	
	vector< command > comm (n);
	

	char who;
	int pos0;

	int pos[] = { 1, 1 };

	for( int i = 0; i < n; i++){
		in>>who>>pos0;

		comm[i].who = (who=='O') ? 0 : 1;
		comm[i].pos = pos0;
		comm[i].time = abs( pos[ comm[i].who ] - comm[i].pos );

		pos[ comm[i].who ] = comm[i].pos;
	}

	int time[] = {0,0};
	int cur;
	int res = 0;
	for( int i=0;i<n;i++){
		cur = comm[i].who;
		res += sign1( comm[i].time - time[ (cur+1)%2 ] ) + 1;
		time[ cur ] += sign1( comm[i].time - time[ (cur+1)%2 ] ) + 1;
		time[ (cur+1)%2 ] = 0;
	}

	return res;
}

int main(){
	in = ifstream("A-small.in");
	ofstream out ("A-small.out");
	int T;
	in >> T;

	for( int i = 1; i <= T; i++)
		out<<"Case #"<<i<<": "<<solve()<<endl;
	out.close();
	in.close();
}