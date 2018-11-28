#include <iostream>
#include <fstream>
#include <vector>

int gcd(int a, int b)
{
	if(b == 0)
	{
		return a;
	}
	else
	{
		return gcd(b, a % b);
	}
}

using namespace std;
int main(int argc, char** argv)
{
	ifstream f(argv[1]);
	int T;
	f >> T;
	vector<bool> rr(T);
	for (int t=0; t<T; ++t)
	{
		int N, PD, PG;
		f >> N >> PD >> PG;
		if (PG==100)
		{
			if (PD==100) rr[t] = true;
			else rr[t] = false;
			continue;
		}
		else if (PG==0)
		{
			rr[t] = (PD==0);
			continue;
		}
		//other case
		int xd = gcd(100, PD);
		int xg = gcd(100, PG);
		int xx = gcd(100*abs(PG-PD), xd*xg);
		int k = xd*xg/ xx;
		int h = 100/ xd;
		int D = k*h;//k*h
		float D1 = PD*D/100.0;
		cout <<xd<<" "<<xg<<" k="<< k<<" D="<<D<<", D1= "<<D1<<endl;

		rr[t] = (D<=N);

	}
	

	ofstream g(argv[2]);
	for (int t=0; t<T; ++t)
	{
		g << "Case #"<<(t+1)<<": ";
		if (rr[t]) g <<"Possible"<<endl;
		else g <<"Broken"<<endl;
	}
	g.close();
	
}