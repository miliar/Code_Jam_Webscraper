#include <iostream>
#include <fstream>
using namespace std;

int main (int argc, char * const argv[]) {
	fstream file_in, file_out;
	
	int c = 0, N = 0;
	long  *t = new long;
	
	file_in.open("input.in",ios::in);
	file_out.open("output.in", ios::out);
	
	char str[36];
	
	//Getting TestBench count c
	file_in >> str;
	c = atoi(str);
    cout << c << "\n";
	
	for (int i = 0; i < c; i++) {		
		//INPUT DATA
		//Getting N Value of 
		file_in >> str;
		N = atoi(str);
		cout << N << " ";
		
		//N Values
		for (int j = 0; j < N; j++) {
			//Getting tj
			file_in >> str;
			t[j] = atol(str);
			cout << t[j] << " ";
		}
		
		cout << "\n";
		
		//COMPUTE APOCALYPSE TIME
		//file_out << "Case #" << (i+1) << ": ";
		if(N == 2) {
			long d = 0;
			if (t[0] > t[1]) {
				d = t[0] - t[1];
			}
			else {
				d = t[1] - t[0];
			}
			
			if (t[0]%d == 0) {
				d = 0;
			}
			else {
				d -= t[0]%d;
			}

			file_out << "Case #" << (i+1) << ": " << d << "\n";
		}
		else if(N == 3) {
			//Differences
			long d0, d1, d2;
			if (t[0] > t[1]) {
				d0 = t[0] - t[1];
			}
			else {
				d0 = t[1] - t[0];
			}
			if (t[1] > t[2]) {
				d1 = t[1] - t[2];
			}
			else {
				d1 = t[2] - t[1];
			}
			if (t[2] > t[0]) {
				d2 = t[2] - t[0];
			}
			else {
				d2 = t[0] - t[2];
			}
			
			if(d0 == 0 || d1 == 0 || d2 == 0)
			{
				long d = 0;
				if (t[0] == t[1]) {
					if(t[0] > t[2])
						d = t[0] - t[2];
					else 
						d = t[2] - t[0];
				}
				else if(t[1] == t[2]) {
					if(t[1] > t[0])
						d = t[1] - t[0];
					else
						d = t[0] - t[1];
				}
				else if(t[2] == t[0]) {
					if(t[2] > t[1])
						d = t[2] - t[1];
					else 
						d = t[1] - t[2];
				}
				
				if(t[0]%d == 0)
					d = 0;
				else {
					d-=t[0]%d;
				}

				file_out << "Case #" << (i+1) << ": " << d << "\n";
			}
			else
			{
			long m = d0, n = d1, r, m1, n1;
			while (m%n != 0) {
				r = m%n;
				m = n;
				n = r;
			}
			m1 = n;
			m = d2, n = d0;
			while (m%n != 0) {
				r = m%n;
				m = n;
				n = r;
			}		
			n1 = n;
			while (m1%n1 != 0) {
				r = m1%n1;
				m1 = n1;
				n1= r;
			}
				
			
				if (t[0]%n1 == 0) {
					n1 = 0;
				}
				else {
					n1 -= t[0]%n1;
				}

			file_out << "Case #" << (i+1) << ": " << n1 << "\n";
			}
		}
		
		//One Round Complete
	}
	
	file_out.close();
	file_in.close();
    return 0;
}
