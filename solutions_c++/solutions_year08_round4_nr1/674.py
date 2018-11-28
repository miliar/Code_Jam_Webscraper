#include <iostream>
#include <vector>
#include <string>
#include <numeric>
#include <sstream>


using namespace std;


vector<vector<int> > t;
vector<int> gv, changeable; // gate_val
int nint, M, V;
int cal(int n,int v) {
    if (n>nint)
	if (gv[n]==v)
	    return 0;
	else
	    return M+1;
    if (t[n].size())
	return t[n][v];
    // want false
    int gor=cal(2*n,0)+cal(2*n+1,0);
    int gand=gor;
    gand = min(gand, cal(2*n,1) + cal(2*n+1,0));
    gand = min(gand, cal(2*n,0) + cal(2*n+1,1));
    if (gv[n]==1)
	t[n].push_back( gand );
    if (gv[n]==0 && !changeable[n])
	t[n].push_back( gor );
    if (gv[n]==0 && changeable[n])
	t[n].push_back( min(gand+1,gor) );

    // want true
    gand=cal(2*n,1)+cal(2*n+1,1);
    gor=gand;
    gor = min(gor, cal(2*n,1) + cal(2*n+1,0));
    gor = min(gor, cal(2*n,0) + cal(2*n+1,1));
    if (gv[n]==0)
	t[n].push_back( gor );
    if (gv[n]==1 && !changeable[n])
	t[n].push_back( gand );
    if (gv[n]==1 && changeable[n])
	t[n].push_back( min(gor+1,gand) );
//    cout<<"# "<<n<<' '<<v<<" : "<<t[n][0]<<' '<<t[n][1]<<endl;
    return t[n][v];
    
}

string solve() {
    gv = vector<int>(1);
    changeable = vector<int>(1); 
    cin>>M>>V;
    nint = (M-1)/2;
    t = vector<vector<int> >(nint+1);
    for (int i=1; i<=M; i++) {
	int a;
	cin>>a;  gv.push_back(a);
	if (i <= nint) {
	    cin>>a;  changeable.push_back(a);
	}
    }

//     for (int i=1; i<=M; i++)
// 	cout<<gv[i];
//     cout<<endl;
//     for (int i=1; i<=nint; i++)
// 	cout<<changeable[i];
//     cout<<endl;

    int a = cal(1,V);
    if (a>M)
	return "IMPOSSIBLE";
    else {
	stringstream s;
	s<<a;
	return s.str();
    }
    
}


int main() {
    int N;
    cin>>N;  cin.ignore(99, '\n');
    for (int c=1; c<=N; c++)
	cout<<"Case #"<<c<<": "<<solve()<<endl;
    return 0;
}
