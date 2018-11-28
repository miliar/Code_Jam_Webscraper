#include <fstream>
#include <string>
#include <algorithm>
using namespace std;

ifstream fin("bint.in");
ofstream fou("bou1.txt");


int T;
int N[2];

int t[2][120][2];
int link[2][120];
int edge[120];
bool cover[120];

int ans[2];

const int nmax = 100000000;
const int maxtime = 25*60;


void readdata()
{
	fin >> T;
	fin >> N[0] >> N[1];

	int t1,t2,t3,t4;
	string str1,str2;

	for (int h=0; h<=1; h++){
		for (int i=1; i<=N[h]; i++){
			fin >> str1 >> str2;
			t1 = atoi(str1.substr(0,2).c_str());
			t2 = atoi(str1.substr(3,2).c_str());
			t3 = atoi(str2.substr(0,2).c_str());
			t4 = atoi(str2.substr(3,2).c_str());


			t[h][i][0]=t1*60+t2;
			t[h][i][1]=t3*60+t4;
		}
	}

	//sort by depart time.
	int tmp;
	for (int h=0; h<=1; h++){
		for (int i=1; i<=N[h]-1; i++)
		for (int k=i+1; k<=N[h]; k++){
			if (t[h][i][0]>t[h][k][0]){
				for (int x=0; x<=1; x++)
					swap( t[h][i][x] , t[h][k][x] );
			}
		}
	}


	memset(link,0,sizeof(link));
	for (int h=0; h<=1; h++)
		for (int i=1; i<=N[h]; i++){
			tmp = t[h][i][1]+T;
			for (int k=1; k<=N[(h+1)%2]; k++){
				if ( t[(h+1)%2][k][0] >= tmp ){
					link[h][i]=k;
					break;
				}
			}
		}

}



bool findmore(int h, int p )
{
	int tmp;
	for (int i=link[h][p]; i<=N[(h+1)%2]; i++){
		if (!cover[i]){
			cover[i]=true;
			tmp=edge[i];
			edge[i]=p;
			if (tmp==0 || findmore(h, tmp)) return true;
			edge[i]=tmp;
		}
	}
	return false;
}



void work()
{
	//do match
	ans[0]=0; ans[1]=0;
	for (int h=0; h<=1; h++){
		memset( edge, 0 ,sizeof(edge) );
		for (int i=1; i<=N[h]; i++){
			memset( cover , 0 ,sizeof(cover));
			findmore(h, i );
		}

		for (int i=1; i<=N[(h+1)%2]; i++)
			if (edge[i]!=0) ans[(h+1)%2]++;
	}


}



int main()
{
	int CaseNum;
	fin >> CaseNum;
	for (int i=1; i<=CaseNum; i++){
		readdata();
		work();
		fou << "Case #" << i << ": "<< N[0]-ans[0]<<' '<<N[1]-ans[1]<<endl;
	}

	return 0;
}


