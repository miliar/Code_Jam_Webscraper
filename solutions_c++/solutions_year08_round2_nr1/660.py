#include<iostream>
#include<iomanip>
#include<fstream>
#include<string>
#include <vector>
#include <list>

using namespace std;
ofstream outfile("outp.out");//output file
ifstream infile("test.in");//input file 

struct t{
	long long x;
	long long y;
};

bool same_integral_part (struct t a, struct t b)
{ return (( a.x==b.x )||(a.y == b.y)); }


int main()
{
	int num_cases;
	infile>>num_cases;
	int num;
	int n, A, B, C, D, x0, y0, M;
	for (int i = 1; i <= num_cases; i++){
		list<long long> num1;
		list<long long> num2;
		list<struct t> aa;
		list<long long> bb;
		list<long long>::iterator in1;
		list<long long>::iterator in2;
		list<long long>::iterator b1;
		list<long long>::iterator b2;
		list<long long>::iterator c1;
		list<long long>::iterator c2;
		int answer = 0;
		infile>>n>>A>>B>>C>>D>>x0>>y0>>M;
		if (n > 2){
			long long X = x0;
			long long Y = y0;
			num1.push_back(X);
			num2.push_back(Y);
			for (int j = 1; j <= n-1; j ++){
				X = (A * X + B) % M;
				Y = (C * Y + D) % M;
				num1.push_back(X);
				num2.push_back(Y);
			}
			in1=num1.begin();
			in2=num2.begin();
			for (int j = 0; j < n; j++){
				b1=in1;
				b2=in2;
				b1++;
				b2++;
				for (int k = (j+1); k < n; k++){
					c1 = b1;
					c2 = b2;
					c1++;
					c2++;
					for (int l = (k+1); l < n; l++){
						if (((( *in1 + *b1 + *c1)% 3) == 0)&&(((*in2 + *b2 + *c2)%3)== 0 )){
							answer ++;
							struct t f;
							f.x = ( *in1 + *b1 + *c1);
							f.y = (*in2 + *b2 + *c2);
							aa.push_back(f);
						}
						c1++;
						c2++;
					}
					b1++;
					b2++;
				}
				in1++;
				in2++;
			}
			//aa.unique(same_integral_part);
			outfile<<"Case #"<<i<<": ";
			outfile<<answer<<endl;
		}
		else{
			outfile<<"Case #"<<i<<": ";
			outfile<<"0"<<endl;
		}

	}
}