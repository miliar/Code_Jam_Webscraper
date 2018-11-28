#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

#define _for(i,n) for(int i = 0; i<n; i++)
#define _forlor(i,n) for(int i=n-1; i>=0; i--)
#define max(a,b) a<b?b:a

using namespace std;
char tab[4][4];
char averif[10][4];

int main(){
	freopen("in.in", "r", stdin);
	freopen("out.in", "w", stdout);
	int T;
	cin>>T;
	_for(t,T){
		cin.get();
		_for(i,4){
			_for(j,4){
				tab[i][j] = cin.get();
			}
			cin.get();
		}

		bool wx=true,wo=true;
		int cnt = 0;
		_for(i,4){
			_for(j,4){
				averif[cnt][j]=tab[i][j];
			}
			cnt++;
		}
		_for(i,4){
			_for(j,4){
				averif[cnt][j]=tab[j][i];
			}
			cnt++;
		}

		_for(i,4){
			averif[cnt][i] = tab[i][i];
		}
		cnt++;
		_for(i,4){
			averif[cnt][i] = tab[i][3-i];
		}
		cnt++;

		size_t nx,no,nt,np;
		size_t mp = 0;
		bool rbx = false,
			rbo = false;
		cnt=0;
		_for(i,10){

			nx=count(averif[cnt],averif[cnt]+4,'X');
			no=count(averif[cnt],averif[cnt]+4,'O');
			nt=count(averif[cnt],averif[cnt]+4,'T');
			np=count(averif[cnt],averif[cnt]+4,'.');

			rbx = (nx+nt == 4);
			rbo = (no+nt == 4);

			if (rbx || rbo)
			{
				break;
			}
			cnt++;
			mp = max(mp,np);
		}

		if (rbx)
		{
			cout<<"Case #"<<(t+1)<<": X won"<<endl;
		}
		else if (rbo)
		{
			cout<<"Case #"<<(t+1)<<": O won"<<endl;
		}else{
			if(mp != 0)
				cout<<"Case #"<<(t+1)<<": Game has not completed"<<endl;
			else
				cout<<"Case #"<<(t+1)<<": Draw"<<endl;
		}
	}
	return 0;
}