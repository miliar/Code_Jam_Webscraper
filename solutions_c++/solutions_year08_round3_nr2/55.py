#include <fstream>
using namespace std;


ifstream fin("b-large.in");
ofstream fou("bou.txt");




unsigned long long d[42][2][3][5][7];
bool can[42][2][3][5][7];

int a[42];
int N;


void readdata()
{
	memset( a , 0 , sizeof(a));
	char ac[42];

	fin >> ac;
	N=strlen(ac);

	for (int i=0; i<N; i++){
		a[i+1]=ac[i]-'0';
	}

}


void find_mod( int i, int k , int& p2, int& p3, int& p5, int& p7)
{
	int b[42];

	p2=a[i]%2;
	int tmp=0;
	for (int h=1; h<=k; h++){
		b[k-h+1]=a[i-h+1];
		tmp += a[i-h+1];
	}

	p3=tmp%3;
	p5=a[i]%5;


	int rm=0;
	for (int h=1; h<=k; h++){
		rm=(rm*10+b[h])%7;
	}

	p7=rm;
}


unsigned long long work()
{
	memset( d , 0 , sizeof(d));
	memset( can , 0 , sizeof(can));
	int p2, p3, p5, p7;


	find_mod(1,1,p2,p3,p5,p7);
	can[1][p2][p3][p5][p7]=true;
	d[1][p2][p3][p5][p7]=1;

//	can[0][0][0][0][0]=true;
//	d[0][0][0][0][0]=0;

	int m2,m3,m5,m7;

	for (int i=2; i<=N; i++){

		find_mod(i,i,p2,p3,p5,p7);
		can[i][p2][p3][p5][p7]=true;
		d[i][p2][p3][p5][p7]=1;

		for (int k=1; k<=i-1; k++){
			find_mod( i , k , p2 , p3 , p5, p7);

			for (int i2=0; i2<=1; i2++)
			for (int i3=0; i3<=2; i3++)
			for (int i5=0; i5<=4; i5++)
			for (int i7=0; i7<=6; i7++){
				if (can[i-k][i2][i3][i5][i7]){
					m2=(i2+p2+4)%2;
					m3=(i3+p3+6)%3;
					m5=(i5+p5+10)%5;
					m7=(i7+p7+14)%7;

					can[i][m2][m3][m5][m7]=true;
					d[i][m2][m3][m5][m7] += d[i-k][i2][i3][i5][i7];

					m2=(i2-p2+4)%2;
					m3=(i3-p3+6)%3;
					m5=(i5-p5+10)%5;
					m7=(i7-p7+14)%7;

					can[i][m2][m3][m5][m7]=true;
					d[i][m2][m3][m5][m7] += d[i-k][i2][i3][i5][i7];

				}
			}

		}



	}



	unsigned long long ans=0 , tmp=0;

	for (int i2=0; i2<=1; i2++)
	for (int i3=0; i3<=2; i3++)
	for (int i5=0; i5<=4; i5++)
	for (int i7=0; i7<=6; i7++){
		ans += d[N][i2][i3][i5][i7];
	}

	for (int i2=1; i2<=1; i2++)
	for (int i3=1; i3<=2; i3++)
	for (int i5=1; i5<=4; i5++)
	for (int i7=1; i7<=6; i7++){
		tmp += d[N][i2][i3][i5][i7];
	}

	ans=ans-tmp;
	return ans;

}



int main()
{
	int CaseNum;
	fin >> CaseNum;
	unsigned long long ans;
	for (int T=1; T<=CaseNum; T++){
		readdata();
		ans = work();
		fou << "Case #"<<T<<": "<<ans<<endl;
	}
	return 0;
}
