// round-a.cpp : 定¨义?控?制?台?应畖用?程ì序ò的?入?口ú点?。￡
//

// codejam-test.cpp : 定¨义?控?制?台?应畖用?程ì序ò的?入?口ú点?。￡
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include<vector>
#include<algorithm>

using namespace std;

int T;
int N;
int PD;
int PG;

int Gcd(int a, int b)
{
    while(b != 0)
    {
        int r = b;
        b = a % b;
        a = r;
    }
    return a;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("D:\A-small-attempt0 (1).in");
	ofstream out("D:\A.out");

	in >> T;
	int cur = 1;
	while(T-->0){
		in >> N;
		in >> PD;
		in >> PG;

		out <<"Case #"<<cur<<": ";
		cur ++;
		
		if(PG == 0 && PD!=0)
			out << "Broken" << endl;
		else if(PG == 0 && PD == 0 )
			out << "Possible" <<endl;
		else if(PG==100 && PD != 100)
			out << "Broken" << endl;
		else if(PG == 100 && PD ==100)
			out << "Possible" <<endl;
		else{
			if(PD == 0)
				out << "Possible" <<endl;
			else{
				int gcd = Gcd(100,PD);
				int temp = 100/gcd;
				if(temp > N)
					out << "Broken" << endl;
				else
					out << "Possible" <<endl;
			}
		}

		//check gdb

	}

	in.close();
	out.close();
	return 0;
}

