#include <cstdlib>
#include <iostream>
#include <map>
#include <string>

using namespace std;

char s[110][110];
bool convert(int pointR, int pointC, int R, int C){
	bool rst = true;
	if( ((pointR+1)<R) &&((pointC +1)<C) &&
		(s[pointR+1][pointC] == '#') &&
		(s[pointR][pointC+1] == '#') &&
		(s[pointR+1][pointC+1] == '#') ){

		s[pointR][pointC] ='/';
		s[pointR][pointC+1] ='\\';
		s[pointR+1][pointC] ='\\';
		s[pointR+1][pointC+1] ='/';

	}else{
		rst = false;
	}

	return rst;

}
void work(){
	int i,j,k;

	int R,C;
	cin>>R;
	cin>>C;
	for (i=0; i<R;i++)
		for(j=0; j<C; j++)
			cin>>s[i][j];

	//////////////////////////////////////////////////////////////////////////
	bool done = true;
	for (i=0; i<R; i++)
	{
		if(!done) break;
		for(j=0; j<C; j++){

			if(s[i][j] == '#'){
				done = convert(i, j, R, C);
				if(!done) break;
			}
		}
	}
	if(!done)
		cout<<"Impossible\n";
	else{
		for (i=0; i<R;i++){
			for(j=0; j<C; j++)
				cout<<s[i][j];
			cout<<"\n";
		}
	}
}

int main()
{
	freopen("A-large(2).in" , "r" , stdin);
	freopen("A-large(2).in.out" , "w" , stdout);

	int T;   
	cin>>T;

	for(int caseID = 1 ; caseID <= T ; caseID ++){
		cout<<"Case #"<<caseID<<":\n"; 
		work();
	}

	// system("PAUSE");
	return 0;
}