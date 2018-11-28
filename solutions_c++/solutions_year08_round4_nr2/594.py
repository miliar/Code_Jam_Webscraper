#include <fstream>
#include <cmath>
using namespace std;

ifstream fin("bin.txt");
ofstream fou("bou.txt");

int N , M , A;


void work()
{
	bool fi = false;
	int a1 ,a2, b1, b2 ,tmp;
	int i1 , i2, j1 , j2;

	for (a1=0; !fi && a1<=N; a1++)
	for (a2=a1;!fi && a2<=N; a2++)
	for (b1=0; !fi && b1<=M; b1++)
	for (b2=b1;!fi && b2<=M; b2++){
		tmp = a1*b2-a2*b1;
		if (abs(tmp) == A){
			fi = true;
			i1=a1; i2=a2; j1=b1; j2=b2;
			break;
		}
	}

	if (!fi){
		fou <<"IMPOSSIBLE"<<endl;
	}
	else{
		fou << 0 << ' ' << 0 << ' ' << i1 << ' ' << j1 << ' ' << i2 << ' ' << j2 << endl;
	}
}


int main()
{
	int CaseNum;
	fin >> CaseNum;

	for (int T=1; T<=CaseNum; T++){
		fin >> N >> M >> A;

		fou << "Case #"<<T<<": ";
		work();


	}
}
