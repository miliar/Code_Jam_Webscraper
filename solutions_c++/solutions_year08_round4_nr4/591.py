#include <fstream>
#include <string>
using namespace std;


ifstream fin("din.txt");
ofstream fou("dou.txt");

string S;
int K , len;
int p[7];
int tp;
int ans;

void work()
{
	string st="";
	int i=0;
	while (i<len-1){
		for (int h=0; h<K; h++){
			st[h+i]=S[p[h]+i];
		}
		i=i+K;
	}


	int tmp=0;
	char c;

	while (!st.empty() ){
		tmp++;
		c=st[0];
		while (!st.empty() && c==st[0]){
			st.erase(0,1);
		}
	}

	if (tmp<ans) ans=tmp;
}



void pum( int x )
{
	if (x==K){
		work();
	}
	else{
		bool ta;
		for (int i=1; i<=K; i++){
			ta=false;
			for (int k=0; k<x; k++){
				if (p[k]==i){
					ta=true;
					break;
				}
			}
			if (ta) continue;
			p[x]=i;
			pum(x+1);
		}

	}


}




int main()
{
	int cn;
	fin >> cn;
	for (int t=1;t<=cn; t++){
		fin >> K;
		fin >> S;

		len = S.length();

		ans=100000000;
		pum(0);


		fou << "Case #" << t << ": " << ans << endl;
	}
}
